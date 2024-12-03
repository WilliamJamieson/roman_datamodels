import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core, _default

from .ref import (
    RefCommonRef,
    RefOpticalElementRef,
)

__all__ = ["PixelareaRef"]


class PixelareaRefMetaPhotometry(_core.ObjectNode):
    @property
    def pixelarea_steradians(self) -> u.Quantity | None:
        return self._get_node("pixelarea_steradians", lambda: float(_default.NONUM) * u.sr)

    @property
    def pixelarea_arcsecsq(self) -> u.Quantity | None:
        return self._get_node("pixelarea_arcsecsq", lambda: float(_default.NONUM) * u.arcsec**2)


class PixelareaRefMeta(RefCommonRef, RefOpticalElementRef):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            *super(RefCommonRef, cls).asdf_required(),
            "photometry",
        )

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "PIXELAREA")

    @property
    def photometry(self) -> PixelareaRefMetaPhotometry:
        return self._get_node("photometry", PixelareaRefMetaPhotometry)


class PixelareaRef(_core.DataModelNode):
    """
    Pixel area reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/pixelarea-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "data",
        )

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("data"):
            return self.data.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (4096, 4096)

    @property
    def meta(self) -> PixelareaRefMeta:
        return self._get_node("meta", PixelareaRefMeta)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float32))
