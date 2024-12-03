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

__all__ = ["SourceCatalog"]


class SourceCatalogMeta(Basic):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            "optical_element",
            "exposure",
            "photometry",
            "program",
            "visit",
        )

    @property
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", WfiOpticalElement.F158)

    @property
    def exposure(self) -> Exposure:
        return self._get_node("exposure", Exposure)

    @property
    def photometry(self) -> Photometry:
        return self._get_node("photometry", Photometry)

    @property
    def program(self) -> Program:
        return self._get_node("program", Program)

    @property
    def visit(self) -> Visit:
        return self._get_node("visit", Visit)


class SourceCatalog(_core.DataModelNode):
    """
    Photometry and astrometry computed by the Source Catalog Step
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/source_catalog-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "source_catalog",
        )

    @property
    def array_shape(self) -> tuple[int]:
        raise NotImplementedError("This node does not have an array shape")

    @property
    def meta(self) -> SourceCatalogMeta:
        return self._get_node("meta", SourceCatalogMeta)

    @property
    def source_catalog(self) -> Table:
        return self._get_node("source_catalog", Table([range(3), range(3)], names=["a", "b"]))
