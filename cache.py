from models.tr import Repository
import logging
import coloredlogs
import hashlib
import tempfile
import requests
import shutil

def load_pdf_links_from_cache(tr_file, grundschutz_file) -> tuple:
    logger = logging.getLogger("Cache")
    coloredlogs.install(
        level="DEBUG", fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    # Read the PDF links from the file
    tr_pdf_links = []
    grundschutz_pdf_links = []
    tr_repository = load_repository_from_file(tr_file)

    for tr in tr_repository.trs:
        for doc in tr.documents:
            pdf_link = doc.url_pdf
            if (
                "bundesgesundheitsministerium.de" in pdf_link
                or "bgbl.de" in pdf_link
            ):
                # Skip links that are not from BSI
                continue
            tr_pdf_links.append((pdf_link, doc.title, doc.filename))
    logger.debug(f"Found {len(tr_pdf_links)} TR PDFs to download")

    grundschutz_repository = load_repository_from_file(grundschutz_file)
    for grundschutz in grundschutz_repository.grundschutz_bausteine:
        for doc in grundschutz.documents:
            pdf_link = doc.url_pdf
            if (
                "bundesgesundheitsministerium.de" in pdf_link
                or "bgbl.de" in pdf_link
            ):
                # Skip links that are not from BSI
                continue
            grundschutz_pdf_links.append((pdf_link, doc.title, doc.filename))
    logger.debug(f"Found {len(grundschutz_pdf_links)} Grundschutz PDFs to download")

    return tr_pdf_links, grundschutz_pdf_links

def load_repository_from_file(file) -> Repository:
    # Read the PDF links from the file
    repository = None
    with open(file, "r") as f:
        repository = Repository.model_validate_json(f.read())
    return repository

def write_repository_to_file(repository: Repository, file):
    import os
    content = repository.model_dump_json(indent=2)
    tmp_path = str(file) + ".tmp"
    with open(tmp_path, "w") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, file)

def hash_file(file) -> str:
    # Create a hash object
    sha256_hash = hashlib.sha256()

    # Open the file in binary mode
    with open(file, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def download_file(url: str) -> tuple:
    # Download the file from the URL and save it to the specified filename
    response = requests.get(url, stream=True, timeout=(10, 60))
    if response.status_code == 200:
        # Create a temporary file
        hashsum = hashlib.sha256()
        temp_file =  tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        for chunk in response.iter_content(chunk_size=8192):
            temp_file.write(chunk)
            hashsum.update(chunk)
        
        return temp_file, hashsum.hexdigest()
    else:
        raise FileNotFoundError(f"Failed to download file: {response.status_code}")
    
def move_temp_file_to_final_location(temp_file, final_file_path):
    # Move the temporary file to the final location
    # spool back the temporary file
    temp_file.seek(0)
    # copy the temp file to the final location
    shutil.copy(temp_file.name, final_file_path)
    # remove the temp file
    temp_file.close()

