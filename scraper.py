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
from datetime import datetime
from typing import Optional

import pypdfium2 as pdfium
from pdftext.extraction import plain_text_output

from cache import download_file, hash_file, load_repository_from_file, move_temp_file_to_final_location, write_repository_to_file
from models.tr import TR, Document, DocumentVersion, Grundschutz, Repository


TR_OVERVIEW_PAGE = "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/technische-richtlinien_node.html"
GS_OVERVIEW_PAGE = "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/IT-Grundschutz-Bausteine/Bausteine_Download_Edition_node.html"
USER_AGENT_HEADER = {"User-Agent": "curl/7.54.1"}
FILE_REPOSITORY = "data/repository.json"
TR_PDF_LINKS_FILE = "data/tr-pdf-links.txt"
GS_PATH = Path("pdf/grundschutz")
TR_PATH = Path("pdf/tr")
SOUP_PARSER = "html.parser"

def extract_title_from_pdf(pdf_path: str) -> Optional[str]:
    """Extract the title from a PDF file using metadata or first page content."""
    try:
        pdf = pdfium.PdfDocument(pdf_path)
        
        # First try metadata
        try:
            metadata = pdf.get_metadata_dict()
            title = metadata.get('Title', '').strip()
            if title and len(title) > 5:
                pdf.close()
                return title
        except Exception:
            pass
        
        # Fall back to extracting from first page content
        try:
            text = plain_text_output(pdf_path, sort=True, hyphens=True, max_pages=1)
            first_lines = text[:500].strip().split('\n')
            
            potential_title = []
            for line in first_lines[:5]:
                line = line.strip()
                if line and len(line) > 5:
                    if any(skip in line.lower() for skip in ['version:', 'date:', 'page', 'document history']):
                        break
                    potential_title.append(line)
                    if len(potential_title) >= 2:
                        break
            
            if potential_title:
                pdf.close()
                return ' '.join(potential_title)
        except Exception:
            pass
        
        pdf.close()
    except Exception:
        pass
    
    return None


def extract_identifier_from_filename(filename: str, tr_id: str) -> str:
    """
    Extract document identifier from filename and TR id.
    
    Examples:
        TR03108-1.pdf + TR-03108 -> BSI TR-03108-1
        BSI-TR-02102-2.pdf + TR-02102 -> BSI TR-02102-2
        TR_De_Mail.pdf + TR-01201 -> BSI TR-01201
        TR-03130_TR-eID-Server_Part2.pdf + TR-03130 -> BSI TR-03130-2
    """
    stem = Path(filename).stem
    
    # Extract the TR number from tr_id (e.g., "TR-03108" -> "03108")
    tr_num_match = re.search(r'TR[-_]?(\d+)', tr_id, re.IGNORECASE)
    if not tr_num_match:
        return f"BSI {tr_id}"
    
    tr_num = tr_num_match.group(1)
    
    # Look for part/sub-document number in filename
    # Pattern 1: TR03108-1, BSI-TR-03108-2 (number directly after TR number)
    part_match = re.search(
        rf'(?:TR[-_]?)?{tr_num}[-_](\d+(?:[-_.]\d+)*)',
        stem,
        re.IGNORECASE
    )
    
    if part_match:
        part = part_match.group(1).replace("_", "-").replace(".", "-")
        return f"BSI TR-{tr_num}-{part}"
    
    # Pattern 2: _Part2, _Teil3 anywhere in filename
    part_suffix = re.search(r'[_-]?[Pp]art[-_]?(\d+)', stem)
    if part_suffix:
        return f"BSI TR-{tr_num}-{part_suffix.group(1)}"
    
    teil_suffix = re.search(r'[_-]?[Tt]eil[-_]?(\d+)', stem)
    if teil_suffix:
        return f"BSI TR-{tr_num}-{teil_suffix.group(1)}"
    
    return f"BSI TR-{tr_num}"


def extract_gs_identifier_from_filename(filename: str) -> Optional[str]:
    """
    Extract Grundschutz identifier from filename.
    
    Examples:
        ISMS_1_Sicherheitsmanagement_Edition_2023.pdf -> ISMS.1
        APP_1_1_Office_Produkte_Edition_2023.pdf -> APP.1.1
        ORP_2_Personal_Editon_2023.pdf -> ORP.2
    """
    stem = Path(filename).stem
    
    # Match pattern like ISMS_1, APP_1_1, ORP_2, etc. at the start
    match = re.match(r'^([A-Z]+)_([\d_]+)', stem)
    if match:
        prefix = match.group(1)
        numbers = match.group(2).rstrip('_').replace('_', '.')
        return f"{prefix}.{numbers}"
    
    return None


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
            "--hash-pdfs",
            help="Hash all PDFs in the repository and store the checksum",
            action="store_true",
        )
        parser.add_argument(
            "--export-tr-links",
            help="Export all TR PDF links to data/tr-pdf-links.txt",
            action="store_true",
        )
        parser.add_argument(
            "--sync",
            help="Sync local PDFs with BSI website (check for updates and download new files)",
            action="store_true",
        )
        parser.add_argument(
            "--sync-tr",
            help="Sync only TR PDFs with BSI website",
            action="store_true",
        )
        parser.add_argument(
            "--sync-grundschutz",
            help="Sync only Grundschutz PDFs with BSI website",
            action="store_true",
        )
        parser.add_argument(
            "--force",
            help="Force re-download even if file exists and checksum matches",
            action="store_true",
        )
        parser.add_argument(
            "--update-identifiers",
            help="Update document identifiers in repository.json",
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

    def export_tr_links(self):
        """Export all TR PDF links to data/tr-pdf-links.txt"""
        try:
            repo_file = Path(FILE_REPOSITORY)
            if not repo_file.exists():
                self.logger.error("Repository file not found. Run --fetch-tr-pdf-links first.")
                return

            repository = load_repository_from_file(repo_file)
            links = []
            
            for tr in repository.trs:
                for document in tr.documents:
                    links.append(f"{document.url_pdf}\t{document.filename}\t{tr.title}")
            
            # Write to file
            with open(TR_PDF_LINKS_FILE, "w", encoding="utf-8") as f:
                f.write(f"# TR PDF Links - Generated at {datetime.now().isoformat()}\n")
                f.write(f"# Total: {len(links)} links\n")
                f.write("# Format: URL\\tFilename\\tTitle\n\n")
                for link in links:
                    f.write(link + "\n")
            
            self.logger.info(f"Exported {len(links)} TR PDF links to {TR_PDF_LINKS_FILE}")
        except Exception as e:
            self.logger.error(f"Error exporting TR links: {str(e)} {traceback.format_exc()}")

    def sync_document(self, document: Document, filepath: Path, force: bool = False) -> tuple[bool, str]:
        """
        Sync a single document with the BSI website.
        
        Returns:
            tuple[bool, str]: (was_updated, status_message)
            
        Logic:
        1. If file doesn't exist locally -> download it
        2. If file exists but no checksum in repo -> hash local file and store
        3. If file exists with checksum -> download from BSI, compare checksums
           - If different -> we have a newer version, update local file
           - If same -> file is up to date
        """
        local_file_exists = filepath.exists()
        repo_checksum = document.sha256
        
        # Ensure parent directory exists
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        # Case 1: File doesn't exist locally - download it
        if not local_file_exists:
            self.logger.info(f"[NEW] Downloading {document.filename}")
            try:
                temp_file, file_hashsum = download_file(document.url_pdf)
                move_temp_file_to_final_location(temp_file, filepath)
                now = datetime.now()
                
                # Add initial version entry
                initial_version = DocumentVersion(
                    sha256=file_hashsum,
                    url_pdf=document.url_pdf,
                    retrieved_at=now,
                    latest=True
                )
                document.versions.append(initial_version)
                
                # Extract title from PDF
                title = extract_title_from_pdf(str(filepath))
                if title:
                    document.title = title
                
                self.logger.info(f"[NEW] Downloaded and saved {document.filename}")
                return True, "downloaded"
            except Exception as e:
                self.logger.error(f"[ERROR] Failed to download {document.filename}: {str(e)}")
                return False, f"download_failed: {str(e)}"
        
        # Case 2: File exists but no checksum in repo - hash local file
        if local_file_exists and not repo_checksum:
            self.logger.info(f"[HASH] Computing checksum for existing file {document.filename}")
            now = datetime.now()
            file_hash = hash_file(filepath)
            
            # Add initial version entry
            initial_version = DocumentVersion(
                sha256=file_hash,
                url_pdf=document.url_pdf,
                retrieved_at=now,
                latest=True
            )
            document.versions.append(initial_version)
            
            # Extract title from PDF if not already set
            if not document.title:
                title = extract_title_from_pdf(str(filepath))
                if title:
                    document.title = title
            
            return True, "checksum_added"
        
        # Case 3: File exists with checksum - check for updates from BSI
        if local_file_exists and repo_checksum:
            local_checksum = hash_file(filepath)
            
            # Verify local file matches stored checksum
            if local_checksum != repo_checksum:
                self.logger.warning(
                    f"[MISMATCH] Local file checksum differs from repository for {document.filename}"
                )
                self.logger.warning(f"  Local:  {local_checksum}")
                self.logger.warning(f"  Stored: {repo_checksum}")
            
            # Check BSI for updates (unless force is set, then always download)
            if force:
                self.logger.info(f"[FORCE] Re-downloading {document.filename}")
            else:
                self.logger.info(f"[CHECK] Checking BSI for updates to {document.filename}")
            
            try:
                temp_file, remote_checksum = download_file(document.url_pdf)
                
                if remote_checksum != repo_checksum:
                    # BSI has a newer version!
                    self.logger.info(f"[UPDATE] New version found for {document.filename}")
                    self.logger.info(f"  Old checksum: {repo_checksum}")
                    self.logger.info(f"  New checksum: {remote_checksum}")
                    
                    # Mark all existing versions as not latest
                    for v in document.versions:
                        v.latest = False
                    
                    # Update document with new version
                    move_temp_file_to_final_location(temp_file, filepath)
                    now = datetime.now()
                    
                    # Add new version as latest
                    new_version = DocumentVersion(
                        sha256=remote_checksum,
                        url_pdf=document.url_pdf,
                        retrieved_at=now,
                        latest=True
                    )
                    document.versions.append(new_version)
                    
                    # Re-extract title from updated PDF
                    title = extract_title_from_pdf(str(filepath))
                    if title:
                        document.title = title
                    
                    self.logger.info(f"  Version history now has {len(document.versions)} entries")
                    return True, "updated"
                else:
                    # File is up to date
                    self.logger.debug(f"[OK] {document.filename} is up to date")
                    # Clean up temp file (close first, then unlink)
                    temp_path = Path(temp_file.name)
                    temp_file.close()
                    temp_path.unlink(missing_ok=True)
                    return False, "up_to_date"
                    
            except Exception as e:
                self.logger.error(f"[ERROR] Failed to check updates for {document.filename}: {str(e)}")
                return False, f"check_failed: {str(e)}"
        
        return False, "unknown"

    def sync_tr_pdfs(self, force: bool = False):
        """Sync all TR PDFs with BSI website."""
        self.logger.info("=" * 60)
        self.logger.info("Starting TR PDF sync...")
        self.logger.info("=" * 60)
        
        repo_file = Path(FILE_REPOSITORY)
        if not repo_file.exists():
            self.logger.error("Repository file not found. Run --fetch-tr-pdf-links first.")
            return
        
        repository = load_repository_from_file(repo_file)
        
        stats = {"downloaded": 0, "updated": 0, "up_to_date": 0, "failed": 0, "checksum_added": 0}
        
        for tr in repository.trs:
            self.logger.info(f"\nProcessing TR: {tr.title}")
            for document in tr.documents:
                filepath = TR_PATH / document.filename
                
                # Set identifier if not already set
                if not document.identifier:
                    document.identifier = extract_identifier_from_filename(document.filename, tr.id)
                
                # Add delay to be nice to the server
                time.sleep(randint(1, 3))
                
                _, status = self.sync_document(document, filepath, force)
                if status in stats:
                    stats[status] += 1
                elif "failed" in status:
                    stats["failed"] += 1
        
        # Save updated repository
        write_repository_to_file(repository, repo_file)
        
        self.logger.info("\n" + "=" * 60)
        self.logger.info("TR Sync Complete!")
        self.logger.info(f"  Downloaded:  {stats['downloaded']}")
        self.logger.info(f"  Updated:     {stats['updated']}")
        self.logger.info(f"  Up to date:  {stats['up_to_date']}")
        self.logger.info(f"  Checksums:   {stats['checksum_added']}")
        self.logger.info(f"  Failed:      {stats['failed']}")
        self.logger.info("=" * 60)

    def sync_grundschutz_pdfs(self, force: bool = False):
        """Sync all Grundschutz PDFs with BSI website."""
        self.logger.info("=" * 60)
        self.logger.info("Starting Grundschutz PDF sync...")
        self.logger.info("=" * 60)
        
        repo_file = Path(FILE_REPOSITORY)
        if not repo_file.exists():
            self.logger.error("Repository file not found. Run --fetch-grundschutz-pdf-links first.")
            return
        
        repository = load_repository_from_file(repo_file)
        
        stats = {"downloaded": 0, "updated": 0, "up_to_date": 0, "failed": 0, "checksum_added": 0}
        
        for baustein in repository.grundschutz_bausteine:
            self.logger.info(f"\nProcessing Grundschutz: {baustein.id} - {baustein.title}")
            for document in baustein.documents:
                filepath = GS_PATH / document.filename
                
                # Set identifier if not already set
                if not document.identifier:
                    document.identifier = extract_gs_identifier_from_filename(document.filename)
                
                # Add delay to be nice to the server
                time.sleep(randint(1, 3))
                
                _, status = self.sync_document(document, filepath, force)
                if status in stats:
                    stats[status] += 1
                elif "failed" in status:
                    stats["failed"] += 1
        
        # Save updated repository
        write_repository_to_file(repository, repo_file)
        
        self.logger.info("\n" + "=" * 60)
        self.logger.info("Grundschutz Sync Complete!")
        self.logger.info(f"  Downloaded:  {stats['downloaded']}")
        self.logger.info(f"  Updated:     {stats['updated']}")
        self.logger.info(f"  Up to date:  {stats['up_to_date']}")
        self.logger.info(f"  Checksums:   {stats['checksum_added']}")
        self.logger.info(f"  Failed:      {stats['failed']}")
        self.logger.info("=" * 60)

    def sync_all(self, force: bool = False):
        """Sync all PDFs (TR and Grundschutz) with BSI website."""
        self.sync_tr_pdfs(force)
        self.sync_grundschutz_pdfs(force)

    def hash_pdfs(self):
        """Hash all PDFs in the repository and store the checksum."""
        self.logger.info("Hashing all PDFs in the repository...")
        
        repo_file = Path(FILE_REPOSITORY)
        if not repo_file.exists():
            self.logger.error("Repository file not found. Run --fetch-tr-pdf-links first.")
            return
        
        repository = load_repository_from_file(repo_file)
        updated_count = 0
        
        def update_document_hash(document: Document, filepath: Path):
            """Helper to update document hash and version."""
            nonlocal updated_count
            if filepath.exists():
                file_hash = hash_file(filepath)
                now = datetime.now()
                if document.sha256 != file_hash:
                    self.logger.info(f"[HASH] {document.filename}: {file_hash}")
                    
                    # Mark existing versions as not latest
                    for v in document.versions:
                        v.latest = False
                    
                    # Add new version entry
                    version = DocumentVersion(
                        sha256=file_hash,
                        url_pdf=document.url_pdf,
                        retrieved_at=now,
                        latest=True
                    )
                    document.versions.append(version)
                    updated_count += 1
                else:
                    self.logger.debug(f"[OK] {document.filename} hash unchanged")
        
        # Hash TR PDFs
        for tr in repository.trs:
            for document in tr.documents:
                filepath = TR_PATH / document.filename
                update_document_hash(document, filepath)
        
        # Hash Grundschutz PDFs
        for baustein in repository.grundschutz_bausteine:
            for document in baustein.documents:
                filepath = GS_PATH / document.filename
                update_document_hash(document, filepath)
        
        # Save updated repository
        write_repository_to_file(repository, repo_file)
        self.logger.info(f"Hashing complete. Updated {updated_count} checksums.")

    def update_identifiers(self):
        """Update document identifiers in repository.json."""
        self.logger.info("Updating document identifiers...")
        
        repo_file = Path(FILE_REPOSITORY)
        if not repo_file.exists():
            self.logger.error("Repository file not found.")
            return
        
        repository = load_repository_from_file(repo_file)
        updated_count = 0
        
        # Update TR documents (always regenerate to catch pattern updates)
        for tr in repository.trs:
            for document in tr.documents:
                new_id = extract_identifier_from_filename(document.filename, tr.id)
                if document.identifier != new_id:
                    document.identifier = new_id
                    updated_count += 1
        
        # Update Grundschutz documents
        for baustein in repository.grundschutz_bausteine:
            for document in baustein.documents:
                if not document.identifier:
                    document.identifier = extract_gs_identifier_from_filename(document.filename)
                    if document.identifier:
                        updated_count += 1
        
        write_repository_to_file(repository, repo_file)
        self.logger.info(f"Updated {updated_count} document identifiers.")

    def run(self):
        args = self.parser.parse_args()
        self.logger.debug(f"ARGS: {args}")
        
        if args.fetch_tr_pdf_links:
            self.fetch_tr_pdf_links(TR_OVERVIEW_PAGE)
        
        if args.fetch_grundschutz_pdf_links:
            self.fetch_grundschutz_pdf_links(GS_OVERVIEW_PAGE)
        
        if args.export_tr_links:
            self.export_tr_links()
        
        if args.hash_pdfs:
            self.hash_pdfs()
        
        if args.sync:
            self.sync_all(force=args.force)
        
        if args.sync_tr:
            self.sync_tr_pdfs(force=args.force)
        
        if args.sync_grundschutz:
            self.sync_grundschutz_pdfs(force=args.force)
        
        if args.update_identifiers:
            self.update_identifiers()


def main():
    tools = Scraper()
    tools.run()


if __name__ == "__main__":
    main()
