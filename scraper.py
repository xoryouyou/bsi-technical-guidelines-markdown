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

from models.tr import TR, Document, Repository


TR_OVERVIEW_PAGE = "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/technische-richtlinien_node.html"
GRUNDSCHUTZ_OVERVIEW_PAGE = "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/IT-Grundschutz-Bausteine/Bausteine_Download_Edition_node.html"
USER_AGENT_HEADER = {"User-Agent": "curl/7.54.1"}
# USER_AGENT_HEADER = {"User-Agent": "BSI document scraper v0.1 - https://github.com/xoryouyou/bsi-technical-guidelines-markdown"} 


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
            "--scrape-pdf-list",
            help="Scrape PDF links from TR list and save to data/pdf_links.txt",
            action="store_true",
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

        return parser

    def extract_pdf_links_from_tr_page(self, url) -> list[Document]:
        """Extract all PDF links from the BSI technical guidelines page."""
        try:
            self.logger.debug(f"sending request to: {url}")

            # TODO: investigate 503 errors
            response = requests.get(url, headers=USER_AGENT_HEADER)
            response.raise_for_status()
            self.logger.debug(f"response status code: {response.status_code}")

            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.select_one("#content > div > div > div:nth-child(1) > div > div.c-intro__content > h1").get_text().strip()

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
                    self.logger.info(f"Found PDF link: {full_url}")
                    d = Document(filename=filename, url_pdf=full_url, title=title)
                    documents.append(d)
            return documents
        except Exception as e:
            self.logger.error(f"Error extracting TR links from {url}  -> {str(e)}")
            return None

    def extract_tr_id_from_name(self, name: str) -> str:
        """
        Extract the TR ID from the name.
        The TR ID is typically in the format "TR-00000".
        """
        match = re.search(r"TR\-\d{5}", name)
        if match:
            return match.group(0)
        return None

    def fetch_tr_pdf_links(self, url):
        """Extract all TR links from the BSI technical guidelines overview page.
        and extract all pdf links from the sub TR pages."""

        repository = Repository()
        try:
            # Check if cached file exists
            repo_file = Path("data/tr-overview.json")

            if repo_file.exists():
                self.logger.info("Reading cached TR links from file")
                with open(repo_file, "r") as f:
                    repository = Repository.model_validate_json(f.read())
                self.logger.debug(f"TR Repo loaded {repository}")
            else:
                self.logger.info(f"Fetching TR list from {url}")

                # Fetch the TR overview page
                response = requests.get(url, headers=USER_AGENT_HEADER)
                response.raise_for_status()

                # Extract the TR overview section
                soup = BeautifulSoup(response.text, "html.parser")
                section = soup.find("ul", {"class": "links"})

                # Find all links in the overview section
                for link in section.find_all("a"):
                    href = link.get("href", "")
                    title = link.get_text().strip()
                    # Convert relative URLs to absolute
                    full_url = urljoin("https://www.bsi.bund.de", href)
                    if "/Technische-Richtlinien/" in full_url:  # Only include TR links

                        # Extract the TR ID and title from the name
                        id = self.extract_tr_id_from_name(title)
                        tr = TR(id=id, title=title, url_overview_page=full_url)
                        repository.trs.append(tr)

                # Save the TR links to a file
                with open(repo_file, "w") as f:
                    #f.write('url;title\n')  # Write header
                    f.write(repository.model_dump_json(indent=2))
                    f.flush()  # Ensure writing to disk

            for tr in repository.trs:
                self.logger.debug(f"Processing: {tr.url_overview_page}")
                # Add delay to be nice to the server
                sleepytime = randint(5, 10)
                self.logger.debug(f"waiting for {sleepytime} seconds")
                time.sleep(sleepytime)
                # append the extracted pdf links to the list
                tr.documents = self.extract_pdf_links_from_tr_page(tr.url_overview_page)

            # Save the PDF links to a file
            with open("data/tr-overview-and-documents.json", "w") as f:
                f.write(repository.model_dump_json(indent=2))
                f.flush()


        except Exception as e:
            self.logger.error(f"Error extracting TR links: {str(e)} ")
            return []

    def download_grundschutz_pdfs(self, pdf_links):
        """Download all PDF files from the list of links."""
        try:
            # Create downloads directory
            download_dir = Path("pdf/grundschutz")
            download_dir.mkdir(parents=True, exist_ok=True)

            for pdf_link, title in pdf_links:
                filename = f"{title}.pdf"
                filepath = download_dir / filename

                # Check if file already exists
                if filepath.exists():
                    self.logger.debug(f"File {filename} already exists. Skipping download.")
                    continue

                # Download the PDF file
                response = requests.get(pdf_link, stream=True)
                response.raise_for_status()

                with open(filepath, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                self.logger.info(f"Downloaded: {filename}")

        except Exception as e:
            self.logger.error(f"Error downloading PDFs: {str(e)}")

    def download_pdfs(self):
        """Download all PDF files"""

        try:

            tr_pdf_links = []
            # Read the PDF links from the file
            with open("data/tr-pdf-links.txt", "r") as f:
                for line in f:
                    pdf_link, title = line.strip().split(";")
                    if "bundesgesundheitsministerium.de" in pdf_link or "bgbl.de" in pdf_link:
                        # Skip links that are not from BSI
                        continue
                    tr_pdf_links.append((pdf_link, title))
            self.logger.debug(f"Found {len(tr_pdf_links)} TR PDFs to download")


            grundschutz_pdf_links = []
            # Read the Grundschutz PDF links from the file
            with open("data/grundschutz-pdf-links.txt", "r") as f:
                for line in f:
                    pdf_link = line.strip()
                    grundschutz_pdf_links.append(pdf_link)
            self.logger.debug(f"Found {len(grundschutz_pdf_links)} Grundschutz PDFs to download")


            # Create TR downloads directory
            download_dir = Path("pdf/tr")
            download_dir.mkdir(parents=True, exist_ok=True)

            for pdf_link, title in tr_pdf_links:
                filename = pdf_link.split("/")[-1].split('?')[0]
                filepath = download_dir / filename

                # Check if file already exists
                if filepath.exists():
                    self.logger.debug(f"File {filename} already exists. Skipping download.")
                    continue

                # Download the PDF file
                response = requests.get(pdf_link, stream=True)
                response.raise_for_status()

                with open(filepath, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                self.logger.info(f"Downloaded: {filename}")

            # Create Grundschutz downloads directory
            download_dir = Path("pdf/grundschutz")
            download_dir.mkdir(parents=True, exist_ok=True)

            for pdf_link in grundschutz_pdf_links:
                filename = pdf_link.split("/")[-1].split('?')[0]
                filepath = download_dir / filename

                # Check if file already exists
                if filepath.exists():
                    self.logger.debug(f"File {filename} already exists. Skipping download.")
                    continue

                # Download the PDF file
                response = requests.get(pdf_link, stream=True)
                response.raise_for_status()

                with open(filepath, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                self.logger.info(f"Downloaded: {filename}")

        except Exception as e:
            self.logger.error(f"Error downloading PDFs: {str(e)}")

    def fetch_grundschutz_pdf_links(self, url):
        """Extract all Grundschutz PDF file links from the overview page."""
        try:
            self.logger.debug(f"Fetching Grundschutz list from {url}")
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            gs_links = []
            # Find all links in this section
            for link in soup.find_all("a"):
                href = link.get("href", "")
                self.logger.debug("href: {href}")
                if ".pdf" not in href:
                    continue

                # split of the url params and re-add the ".pdf?__blob=publicationFile"
                cutoff = href.rfind(".pdf")
                href = href[:cutoff] + ".pdf?__blob=publicationFile"

                # Convert relative URLs to absolute
                full_url = urljoin("https://www.bsi.bund.de", href)
                if "/Grundschutz/" in full_url:  # Only include GS links
                    gs_links.append(full_url)

            # Save the GS links to a file
            with open("data/grundschutz-pdf-links.txt", "w") as f:
                f.write("\n".join(gs_links))
                f.flush()  # Ensure writing to disk

            return gs_links

        except Exception as e:
            self.logger.error(f"Error extracting GS links: {str(e)}")
            return []

    def run(self):
        args = self.parser.parse_args()
        self.logger.debug(f"ARGS: {args}")
        if args.fetch_tr_pdf_links:
            self.fetch_tr_pdf_links(TR_OVERVIEW_PAGE)
        if args.fetch_grundschutz_pdf_links:
            gs = self.fetch_grundschutz_pdf_links(GRUNDSCHUTZ_OVERVIEW_PAGE)
            for g in gs:
                print(g)
        if args.download_pdfs:
            self.download_pdfs()


def main():
    tools = Scraper()
    tools.run()


if __name__ == "__main__":
    main()
