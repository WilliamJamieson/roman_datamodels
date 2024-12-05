from astropy.table import Table

from roman_datamodels.stnode import _core

from ..meta import (
    Basic,
    MosaicBasic,
    Photometry,
    Program,
)

__all__ = ["MosaicSourceCatalog"]


class MosaicSourceCatalog_Meta(_core.ImpliedNodeMixin, Basic):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MosaicSourceCatalog

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            "basic",
            "photometry",
            "program",
        )

    @property
    def basic(self) -> MosaicBasic:
        return self._get_node("basic", MosaicBasic)

    @property
    def photometry(self) -> Photometry:
        return self._get_node("photometry", Photometry)

    @property
    def program(self) -> Program:
        return self._get_node("program", Program)


class MosaicSourceCatalog(_core.DataModelNode):
    """
    Photometry and astrometry computed by the Source Catalog Step
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_source_catalog-1.0.0"

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
    def meta(self) -> MosaicSourceCatalog_Meta:
        return self._get_node("meta", MosaicSourceCatalog_Meta)

    @property
    def source_catalog(self) -> Table:
        return self._get_node("source_catalog", lambda: Table([range(3), range(3)], names=["a", "b"]))
