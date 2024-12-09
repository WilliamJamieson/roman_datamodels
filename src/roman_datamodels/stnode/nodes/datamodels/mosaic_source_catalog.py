from astropy.table import Table

from roman_datamodels.stnode import rad

from ..meta import (
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
        return self._get_node("basic", MosaicBasic)

    @rad.field
    def photometry(self) -> Photometry:
        return self._get_node("photometry", Photometry)

    @rad.field
    def program(self) -> Program:
        return self._get_node("program", Program)


class MosaicSourceCatalog(rad.DataModelNode):
    """
    Photometry and astrometry computed by the Source Catalog Step
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_source_catalog-1.0.0"

    @property
    def default_array_shape(self) -> tuple[int]:
        raise NotImplementedError("Array shape is not defined for MosaicSourceCatalog")

    @property
    def testing_array_shape(self) -> tuple[int]:
        return self.default_array_shape

    @rad.field
    def meta(self) -> MosaicSourceCatalog_Meta:
        return self._get_node("meta", MosaicSourceCatalog_Meta)

    @rad.field
    def source_catalog(self) -> Table:
        return self._get_node("source_catalog", lambda: Table([range(3), range(3)], names=["a", "b"]))
