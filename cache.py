from models.tr import Repository
import logging
import coloredlogs

def load_pdf_links_from_cache(tr_file, grundschutz_file) -> tuple:
    # TODO: add sha256 checksum when downloaded
    logger = logging.getLogger("Cache")
    coloredlogs.install(
        level="DEBUG", fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    repository = None
    # Read the PDF links from the file
    tr_pdf_links = []
    grundschutz_pdf_links = []
    with open(tr_file, "r") as f:
        repository = Repository.model_validate_json(f.read())
        for tr in repository.trs:
            for doc in tr.documents:
                pdf_link = doc.url_pdf
                if "bundesgesundheitsministerium.de" in pdf_link or "bgbl.de" in pdf_link:
                    # Skip links that are not from BSI
                    continue
                tr_pdf_links.append((pdf_link,doc.title,doc.filename))
    logger.debug(f"Found {len(tr_pdf_links)} TR PDFs to download")
    with open(grundschutz_file, "r") as f:
        repository = Repository.model_validate_json(f.read())
        for grundschutz in repository.grundschutz_bausteine:
            for doc in grundschutz.documents:
                pdf_link = doc.url_pdf
                if "bundesgesundheitsministerium.de" in pdf_link or "bgbl.de" in pdf_link:
                    # Skip links that are not from BSI
                    continue
                grundschutz_pdf_links.append((pdf_link,doc.title,doc.filename))
    logger.debug(f"Found {len(grundschutz_pdf_links)} Grundschutz PDFs to download")

    return tr_pdf_links, grundschutz_pdf_links