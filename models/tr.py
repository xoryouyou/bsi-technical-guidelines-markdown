from typing import List, Optional
from pydantic import BaseModel, Field, Json
import re
from pprint import pprint
from pathlib import Path

class Repository(BaseModel):
    trs: List["TR"] = Field(default_factory=list)

class TR(BaseModel):
    id: str  # e.g. "TR-03110"
    #description: str
    #url_html: str
    title: str
    url_overview_page: str
    documents: List["Document"] = Field(default_factory=list)

class Document(BaseModel):
    filename: str
    title: Optional[str] = None # TODO: extract form PDF
    description: Optional[str] = None # TODO: scrape from website
    version: Optional[str] = None # TODO extract from PDF
    url_pdf: str
    # url_html: str

trs = {}

def extract_tr_id_from_name(name: str) -> str:
    """
    Extract the TR ID from the name.
    The TR ID is typically in the format "TR-00000".
    """
    match = re.search(r"TR\-\d{5}", name)
    if match:
        return match.group(0)
    return None

# Read and parse each line from the file
with open('data/tr-overview-page-list.txt', 'r') as file:
    for line in file:
        url, name = line.strip().split(';')
        # Extract the TR ID and title from the name
        # typical format is BSI TR-00000-0 
        # we only care for the core part "TR-00000"
        id = extract_tr_id_from_name(name)
        if not id in trs:
            # split the title from the id
            title = name.split(id)[1]
            # remove leading non-alphanumeric characters which are sometimes used
            title = re.sub("^[\W\d]*", "", title)
            print(f"Found id: {id} and title: {title}")
            trs[id] = TR(id=id, title=title, url_overview_page=url)

# pprint(trs)

        # doc = Document(name=name, url_html=url)
        # test.document_list.append(doc)
        # trs[name].document_list.append(doc)

with open('data/tr-pdf-links.txt') as file:
    for line in file:
        url, name = line.strip().split(';')
        # Extract the TR ID and title from the name
        # typical format is BSI TR-00000-0 
        # we only care for the core part "TR-00000"
        id = extract_tr_id_from_name(name)
        if id in trs:

            p = Path(url)
            filename = p.name.split('?')[0]
            print(f"Found pdf link for {id}: {url} : {filename}")
            doc = Document( filename=filename, url_pdf=url)
            
            trs[id].documents.append(doc)

c = Repository(trs=trs.values())

print(c.model_dump_json(indent=2))

with open('data/repo.json', 'w') as file:
    file.write(c.model_dump_json(indent=2))