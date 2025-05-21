from typing import List, Optional
from pydantic import BaseModel, Field


class Repository(BaseModel):
    trs: List["TR"] = Field(default_factory=list)
    grundschutz_bausteine: List["Grundschutz"] = Field(default_factory=list)


class TR(BaseModel):
    id: str  # e.g. "TR-03110"

    title: str
    url_overview_page: str
    documents: List["Document"] = Field(default_factory=list)


class Grundschutz(BaseModel):
    id: str  # e.g. ORP, CON, OPS...
    title: str  # e.g. Organisation und Personal
    documents: List["Document"] = Field(default_factory=list)


class Document(BaseModel):
    filename: str
    title: Optional[str] = None  
    description: Optional[str] = None  
    version: Optional[str] = None  
    url_pdf: str
    sha256: Optional[str] = None
    # url_html: str
