from typing import List, Optional
from pydantic import BaseModel, Field

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
