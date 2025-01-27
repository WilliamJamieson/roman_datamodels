from types import MappingProxyType
from typing import TypeAlias

from astropy.table import Table

from roman_datamodels.stnode import rad

from .meta import (
    Basic,
    MosaicBasic,
    Photometry,
    Program,
)
from .meta.basic import _Basic

__all__ = ["MosaicSourceCatalog"]


_MosaicSourceCatalog_Meta: TypeAlias = _Basic | MosaicBasic | Photometry | Program


class MosaicSourceCatalog_Meta(rad.ImpliedNodeMixin[_MosaicSourceCatalog_Meta], Basic[_MosaicSourceCatalog_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MosaicSourceCatalog

    @rad.field
    def basic(self) -> MosaicBasic:
        return MosaicBasic()

    @rad.field
    def photometry(self) -> Photometry:
        return Photometry()

    @rad.field
    def program(self) -> Program:
        return Program()


_MosaicSourceCatalog: TypeAlias = MosaicSourceCatalog_Meta | Table


class MosaicSourceCatalog(rad.TaggedObjectNode[_MosaicSourceCatalog]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/mosaic_source_catalog-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/mosaic_source_catalog-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/mosaic_source_catalog-1.0.0"
            }
        )

    @rad.field
    def meta(self) -> MosaicSourceCatalog_Meta:
        return MosaicSourceCatalog_Meta()

    @rad.field
    def source_catalog(self) -> Table:
        # Astropy has not implemented type hints for Table so MyPy will complain about this
        # until they do.
        return Table([range(3), range(3)], names=["a", "b"])  # type: ignore[no-untyped-call]
