from types import MappingProxyType

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

__all__ = ["ImageSourceCatalog"]


class ImageSourceCatalog_Meta(rad.ImpliedNodeMixin, Basic):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ImageSourceCatalog

    @rad.field
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", lambda: WfiOpticalElement.F158)

    @rad.field
    def exposure(self) -> Exposure:
        return self._get_node("exposure", Exposure)

    @rad.field
    def photometry(self) -> Photometry:
        return self._get_node("photometry", Photometry)

    @rad.field
    def program(self) -> Program:
        return self._get_node("program", Program)

    @rad.field
    def visit(self) -> Visit:
        return self._get_node("visit", Visit)


class ImageSourceCatalog(rad.TaggedObjectNode):
    """
    Photometry and astrometry computed by the Source Catalog Step
    """

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

    @rad.field
    def meta(self) -> ImageSourceCatalog_Meta:
        return self._get_node("meta", ImageSourceCatalog_Meta)

    @rad.field
    def source_catalog(self) -> Table:
        return self._get_node("source_catalog", lambda: Table([range(3), range(3)], names=["a", "b"]))
