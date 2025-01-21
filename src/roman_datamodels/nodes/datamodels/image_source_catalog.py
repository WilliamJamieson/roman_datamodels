from types import MappingProxyType
from typing import TypeAlias

from astropy.table import Table

from roman_datamodels.stnode import rad

from .meta import (
    Basic,
    Exposure,
    Photometry,
    Program,
    Visit,
    WfiOpticalElement,
)
from .meta.basic import _Basic

__all__ = ["ImageSourceCatalog"]

_ImageSourceCatalog_Meta: TypeAlias = _Basic | WfiOpticalElement | Exposure | Photometry | Program | Visit


class ImageSourceCatalog_Meta(rad.ImpliedNodeMixin[_ImageSourceCatalog_Meta], Basic[_ImageSourceCatalog_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ImageSourceCatalog

    @property
    @rad.field
    def optical_element(self: rad.Node) -> WfiOpticalElement:
        return WfiOpticalElement.F158

    @property
    @rad.field
    def exposure(self: rad.Node) -> Exposure:
        return Exposure()

    @property
    @rad.field
    def photometry(self: rad.Node) -> Photometry:
        return Photometry()

    @property
    @rad.field
    def program(self: rad.Node) -> Program:
        return Program()

    @property
    @rad.field
    def visit(self: rad.Node) -> Visit:
        return Visit()


_ImageSourceCatalog: TypeAlias = ImageSourceCatalog_Meta | Table


class ImageSourceCatalog(rad.TaggedObjectNode[_ImageSourceCatalog]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/image_source_catalog-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/image_source_catalog-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/image_source_catalog-1.0.0"
            }
        )

    @property
    @rad.field
    def meta(self: rad.Node) -> ImageSourceCatalog_Meta:
        return ImageSourceCatalog_Meta()

    @property
    @rad.field
    def source_catalog(self: rad.Node) -> Table:
        # Astropy has not implemented type hints for Table so MyPy will complain about this
        # until they do.
        return Table([range(3), range(3)], names=["a", "b"])  # type: ignore[no-untyped-call]
