from astropy.table import Table

from roman_datamodels.stnode import _core

from ..meta import (
    Basic,
    Exposure,
    Photometry,
    Program,
    Visit,
    WfiOpticalElement,
)

__all__ = ["ImageSourceCatalog"]


class ImageSourceCatalog_Meta(_core.ImpliedNodeMixin, Basic):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ImageSourceCatalog

    @_core.rad_field
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", WfiOpticalElement.F158)

    @_core.rad_field
    def exposure(self) -> Exposure:
        return self._get_node("exposure", Exposure)

    @_core.rad_field
    def photometry(self) -> Photometry:
        return self._get_node("photometry", Photometry)

    @_core.rad_field
    def program(self) -> Program:
        return self._get_node("program", Program)

    @_core.rad_field
    def visit(self) -> Visit:
        return self._get_node("visit", Visit)


class ImageSourceCatalog(_core.DataModelNode):
    """
    Photometry and astrometry computed by the Source Catalog Step
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/image_source_catalog-1.0.0"

    @property
    def array_shape(self) -> tuple[int]:
        raise NotImplementedError("This node does not have an array shape")

    @_core.rad_field
    def meta(self) -> ImageSourceCatalog_Meta:
        return self._get_node("meta", ImageSourceCatalog_Meta)

    @_core.rad_field
    def source_catalog(self) -> Table:
        return self._get_node("source_catalog", lambda: Table([range(3), range(3)], names=["a", "b"]))
