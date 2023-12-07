from __future__ import annotations

from pydantic import BaseModel


class SdfOrigin(BaseModel):
    origin: str
    function: str | None = None


class Sdf(BaseModel):
    special_processing: str
    source: SdfOrigin


class ArchiveCatalog(BaseModel):
    datatype: str
    destination: list[str]


class Archive(BaseModel):
    sdf: Sdf | None = None
    archive_catalog: ArchiveCatalog | None = None
