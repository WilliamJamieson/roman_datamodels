from types import MappingProxyType

from astropy.table import Table

from roman_datamodels.stnode import rad

from .meta import (
    Basic,
    MosaicBasic,
    Photometry,
    Program,
)

__all__ = ["MosaicSourceCatalog"]


class MosaicSourceCatalog_Meta(rad.ImpliedNodeMixin, Basic):
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


class MosaicSourceCatalog(rad.TaggedObjectNode):
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
        return Table([range(3), range(3)], names=["a", "b"])