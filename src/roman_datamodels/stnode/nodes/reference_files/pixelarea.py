import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core, _default

from .ref import RefCommonRefOpticalElementRef

__all__ = ["PixelareaRef"]


class PixelareaRef_Meta_Photometry(_core.ImpliedNodeMixin, _core.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return PixelareaRef_Meta

    @_core.rad_field
    def pixelarea_steradians(self) -> u.Quantity | None:
        return self._get_node("pixelarea_steradians", lambda: float(_default.NONUM) * u.sr)

    @_core.rad_field
    def pixelarea_arcsecsq(self) -> u.Quantity | None:
        return self._get_node("pixelarea_arcsecsq", lambda: float(_default.NONUM) * u.arcsec**2)


class PixelareaRef_Meta(_core.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return PixelareaRef

    @_core.rad_field
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "AREA")

    @_core.rad_field
    def photometry(self) -> PixelareaRef_Meta_Photometry:
        return self._get_node("photometry", PixelareaRef_Meta_Photometry)


class PixelareaRef(_core.DataModelNode):
    """
    Pixel area reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/pixelarea-1.0.0"

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

    @_core.rad_field
    def meta(self) -> PixelareaRef_Meta:
        return self._get_node("meta", PixelareaRef_Meta)

    @_core.rad_field
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float32))
