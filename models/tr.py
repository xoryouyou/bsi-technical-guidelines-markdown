from typing import List, Optional
from datetime import datetime
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


class DocumentVersion(BaseModel):
    """Tracks historical versions of a document."""
    sha256: str
    url_pdf: str
    retrieved_at: datetime
    latest: bool = False


class Document(BaseModel):
    filename: str
    identifier: Optional[str] = None  # e.g. "BSI TR-03108-1"
    title: Optional[str] = None  
    url_pdf: str
    versions: List[DocumentVersion] = Field(default_factory=list)  # Version history
    
    @property
    def latest_version(self) -> Optional["DocumentVersion"]:
        """Get the latest version entry."""
        for v in self.versions:
            if v.latest:
                return v
        return self.versions[-1] if self.versions else None
    
    @property
    def sha256(self) -> Optional[str]:
        """Get SHA256 from latest version."""
        v = self.latest_version
        return v.sha256 if v else None
    
    @property
    def retrieved_at(self) -> Optional[datetime]:
        """Get retrieved_at from latest version."""
        v = self.latest_version
        return v.retrieved_at if v else None
