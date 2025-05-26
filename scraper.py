#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
import time
from random import randint
from urllib.parse import urljoin
from pathlib import Path
import logging
import coloredlogs
import re
import traceback

from cache import download_file, hash_file, load_repository_from_file, move_temp_file_to_final_location, write_repository_to_file
from models.tr import TR, Document, Grundschutz, Repository


TR_OVERVIEW_PAGE = "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/technische-richtlinien_node.html"
GS_OVERVIEW_PAGE = "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/IT-Grundschutz-Bausteine/Bausteine_Download_Edition_node.html"
USER_AGENT_HEADER = {"User-Agent": "curl/7.54.1"}
FILE_REPOSITORY = "data/repository.json"
GS_PATH = Path("pdf/grundschutz")
TR_PATH = Path("pdf/tr")
SOUP_PARSER = "html.parser"

GS_ABBREVIATION_TITLE_MAPPING = {
    "ISMS": "Sicherheitsmanagement",
    "ORP": "Organisation und Personal",
    "CON": "Konzeption und Vorgehensweise",
    "OPS": "Betrieb",
    "DER": "Detektion und Reaktion",
    "APP": "Anwendungen",
    "SYS": "IT-Systeme",
    "IND": "Industrielle IT",
    "NET": "Netye und Kommunikation",
    "INF": "Infrastruktur",
}


# This script scrapes the BSI website for PDF links related to technical guidelines and IT-Grundschutz.
class Scraper:
    def __init__(self):
        self.parser = self._create_parser()
        self.logger = logging.getLogger("Scraper")
        coloredlogs.install(
            level="DEBUG", fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

    def _create_parser(self):
        parser = argparse.ArgumentParser(
            description="Scraping and Conversion for BSI Technical Guidelines"
        )
        parser.add_argument(
            "--fetch-tr-pdf-links",
            help="Extracts all the TR pages from main page and scrape the sub pages for PDF links",
            action="store_true",
        )
        parser.add_argument(
            "--fetch-grundschutz-pdf-links",
            help="Fetch all the Grundschutz PDF links from the overview page",
            action="store_true",
        )
        parser.add_argument(
            "--download-pdfs",
            help="Download all PDFs from the lists in /data",
            action="store_true",
        )
        parser.add_argument(
            "--hash-pdfs",
            help="Hash all PDFs in the repository and store the checksum",
            action="store_true",
        )

        return parser

    def extract_pdf_links_from_tr_page(self, url) -> list[Document]:
        """Extract all PDF links from the BSI technical guidelines page."""
        try:
            self.logger.debug(f"sending request to: {url}")

            response = requests.get(url, headers=USER_AGENT_HEADER)
            response.raise_for_status()
            self.logger.debug(f"response status code: {response.status_code}")

            soup = BeautifulSoup(response.text, SOUP_PARSER)
            title = (
                soup.select_one(
                    "#content > div > div > div:nth-child(1) > div > div.c-intro__content > h1"
                )
                .get_text()
                .strip()
            )

            self.logger.info(f"Title: {title}")
            # Find all links
            documents = []
            for link in soup.find_all("a"):
                href = link.get("href", "")

                # only include links that contain .pdf
                if ".pdf" in href:
                    # split of the url params and re-add the ".pdf?__blob=publicationFile"
                    cutoff = href.rfind(".pdf")
                    href = href[:cutoff] + ".pdf?__blob=publicationFile"
                    filename = href.split("/")[-1].split("?")[0]
                    # Convert relative URLs to absolute
                    full_url = urljoin(url, href)
                    if "bgbl.de" in href:
                    # Skip links that are not from BSI
                        continue
                    self.logger.info(f"Found PDF link: {full_url}")
                    d = Document(filename=filename, url_pdf=full_url, title=title)
                    documents.append(d)
            return documents
        except Exception as e:
            self.logger.error(f"Error extracting TR links from {url}  -> {str(e)}")
            return []

    def extract_tr_id_from_name(self, name: str) -> str:
        """
        Extract the TR ID from the name.
        The TR ID is typically in the format "TR-00000".
        """
        match = re.search(r"TR\-\d{5}", name)
        if match:
            return match.group(0)
        return ""

    def extract_grundschutz_id_from_name(self, name: str) -> str:
        return re.match(r"([A-Z]{3,4})_", name).group(1)

    def fetch_tr_pdf_links(self, url):
        """Extract all TR links from the BSI technical guidelines overview page.
        and extract all pdf links from the sub TR pages."""

        repository = Repository()
        try:
            # Check if cached file exists
            repo_file = Path(FILE_REPOSITORY)

            if repo_file.exists():
                self.logger.info("Reading cached TR links from file")
                repository = load_repository_from_file(repo_file)
                self.logger.debug(f"TR Repo loaded trs: {len(repository.trs)}")
            else:
                self.logger.info(f"Fetching TR list from {url}")

                # Fetch the TR overview page
                response = requests.get(url, headers=USER_AGENT_HEADER)
                response.raise_for_status()

                # Extract the TR overview section
                soup = BeautifulSoup(response.text, SOUP_PARSER)
                section = soup.find("ul", {"class": "links"})

                # Find all links in the overview section
                for link in section.find_all("a"):
                    href = link.get("href", "")
                    title = link.get_text().strip()
                    # Convert relative URLs to absolute
                    full_url = urljoin("https://www.bsi.bund.de", href)
                    if "/Technische-Richtlinien/" in full_url:  # Only include TR links
                        # Extract the TR ID and title from the name
                        tr_id = self.extract_tr_id_from_name(title)
                        tr = TR(id=tr_id, title=title, url_overview_page=full_url)
                        repository.trs.append(tr)

                # Save the TR links to a file
                write_repository_to_file(repository, repo_file)

            for tr in repository.trs:
                self.logger.debug(f"Processing: {tr.url_overview_page}")
                # Add delay to be nice to the server
                sleepytime = randint(5, 10)
                self.logger.debug(f"waiting for {sleepytime} seconds")
                time.sleep(sleepytime)
                # append the extracted pdf links to the list
                tr.documents = self.extract_pdf_links_from_tr_page(tr.url_overview_page)

            # Save the PDF links to a file
            write_repository_to_file(repository, repo_file)

        except Exception as e:
            self.logger.error(f"Error extracting TR links: {str(e)} ")
            return []

    def fetch_grundschutz_pdf_links(self, url):
        """Extract all Grundschutz PDF file links from the overview page."""

        repo_file = Path(FILE_REPOSITORY)
        repository = None
        try:
            if repo_file.exists():
                self.logger.info("Reading cached Grundschutz links from file")
                repository = load_repository_from_file(repo_file)
                self.logger.debug(f"Grundschutz Repo loaded bausteine: {len(repository.grundschutz_bausteine)}")
            else:
                self.logger.debug(f"Fetching Grundschutz list from {url}")
                response = requests.get(url)
                response.raise_for_status()
                repository = Repository()
                soup = BeautifulSoup(response.text, SOUP_PARSER)

                # pre populate Grundschutz entries
                grundschutz_map = {}
                for entry in GS_ABBREVIATION_TITLE_MAPPING.keys():
                    g = Grundschutz(id=entry, title=GS_ABBREVIATION_TITLE_MAPPING[entry])
                    grundschutz_map[entry] = g

                # Find all links in this section
                for link in soup.find_all("a"):
                    href = link.get("href", "")
                    self.logger.debug(f"href: {href}")
                    if ".pdf" not in href:
                        continue

                    # Convert relative URLs to absolute
                    full_url = urljoin("https://www.bsi.bund.de", href)
                    if "/Grundschutz/" in full_url:  # Only include GS links
                        # split of the url params and re-add the ".pdf?__blob=publicationFile"

                        filename = Path(href).name.split("?")[0]

                        grundschutz_id = self.extract_grundschutz_id_from_name(filename)
                        title = GS_ABBREVIATION_TITLE_MAPPING.get(grundschutz_id, "Unknown")

                        d = Document(filename=filename, title=title, url_pdf=full_url)
                        grundschutz_map[grundschutz_id].documents.append(d)

                repository.grundschutz_bausteine = [
                    grundschutz_map[k] for k in grundschutz_map
                ]
                # Save the GS links to a file
                write_repository_to_file(repository, FILE_REPOSITORY)

        except Exception as e:
            self.logger.error(
                f"Error extracting GS links: {str(e)} {traceback.format_exc()} "
            )
            return []

    def check_if_file_matches_existing_repository_entry(self, document, filepath):
        repository_hashsum = document.sha256
        if filepath.exists():
            self.logger.debug(
                f"File {document.filename} already exists. Skipping download."
            )
            file_hashsum = hash_file(filepath)
            if file_hashsum == repository_hashsum:
                self.logger.info("Stored hash matches file hash for %s", filepath)
            else:
                self.logger.info(
                    "Hash mismatch for %s: %s != %s",
                    document.filename,
                    file_hashsum,
                    repository_hashsum,
                )

        else:
            self.logger.info(f"Downloading {document.filename} from {document.url_pdf}")
            temp_file, file_hashsum = download_file(document.url_pdf)
            self.logger.info(f"Downloaded: {document.filename}")
            if file_hashsum != repository_hashsum:
                self.logger.info(
                    "Hash mismatch for %s: %s != %s",
                    document.filename,
                    file_hashsum,
                    repository_hashsum,
                )
                # Update the repository with the new hash
                document.sha256 = file_hashsum
                self.logger.info(f"Copying temp file from {temp_file.name} to {filepath}")
                # Move the temporary file to the final location
                move_temp_file_to_final_location(temp_file, filepath)


    def download_pdfs(self):
        """Download all PDF files"""

        try:
            grundschutz = load_repository_from_file(FILE_REPOSITORY)
            # Download all Grundschutz PDFs
            for grundschutz_baustein in grundschutz.grundschutz_bausteine:
                for document in grundschutz_baustein.documents:
                    # Check if file already exists
                    filepath = GS_PATH / document.filename
                    self.check_if_file_matches_existing_repository_entry(document, filepath)


            # Save the updated repository to a file
            write_repository_to_file(grundschutz, FILE_REPOSITORY)

            tr_repository = load_repository_from_file(FILE_REPOSITORY)
            # Download all TR PDFs
            for tr in tr_repository.trs:
                for document in tr.documents:
                    # Check if file already exists
                    filepath = TR_PATH / Path(document.filename)
                    self.check_if_file_matches_existing_repository_entry(document, filepath)

            # Save the updated repository to a file
            write_repository_to_file(tr_repository, FILE_REPOSITORY)

        except Exception as e:
            self.logger.error(
                f"Error downloading PDFs: {str(e)} {traceback.format_exc()} "
            )

    def run(self):
        args = self.parser.parse_args()
        self.logger.debug(f"ARGS: {args}")
        if args.fetch_tr_pdf_links:
            self.fetch_tr_pdf_links(TR_OVERVIEW_PAGE)
        if args.fetch_grundschutz_pdf_links:
            self.fetch_grundschutz_pdf_links(GS_OVERVIEW_PAGE)
        if args.download_pdfs:
            self.download_pdfs()
        if args.hash_pdfs:
            self.hash_pdfs()
        


def main():
    tools = Scraper()
    tools.run()


if __name__ == "__main__":
    main()
