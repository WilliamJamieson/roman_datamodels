import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core, _default

from .ref import (
    RefCommonRef,
    RefExposureTypeRef,
    RefOpticalElementRef,
)

__all__ = ["DarkRef"]


class DarkRefMetaExposure(_core.ObjectNode):
    @property
    def required(self) -> tuple[str]:
        return (
            "ngroups",
            "nframes",
            "groupgap",
            "ma_table_name",
            "ma_table_number",
        )

    @property
    def ngroups(self) -> int:
        return self._get_node("ngroups", lambda: 6)

    @property
    def nframes(self) -> int:
        return self._get_node("nframes", lambda: 8)

    @property
    def groupgap(self) -> int:
        return self._get_node("groupgap", lambda: 0)

    @property
    def ma_table_name(self) -> str:
        return self._get_node("ma_table_name", lambda: _default.NOSTR)

    @property
    def ma_table_number(self) -> int:
        return self._get_node("ma_table_number", lambda: _default.NONUM)


class DarkRefMeta(RefCommonRef, RefExposureTypeRef, RefOpticalElementRef):
    @property
    def required(self) -> tuple[str]:
        return (
            *super().required,
            *super(RefCommonRef, self).required,
            *super(RefExposureTypeRef, self).required,
            "exposure",
        )

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "DARK")

    @property
    def exposure(self) -> DarkRefMetaExposure:
        return self._get_node("exposure", DarkRefMetaExposure)


class DarkRef(_core.DataModelNode):
    """
    Dark reference schema
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/dark-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "meta",
            "data",
            "dq",
            "dark_slope",
            "dark_slope_error",
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
        return (2, 4096, 4096)

    @property
    def meta(self) -> DarkRefMeta:
        return self._get_node("meta", DarkRefMeta)

    @property
    def data(self) -> u.Quantity:
        return self._get_node(
            "data", lambda: u.Quantity(np.zeros(self.array_shape, dtype=np.float32), unit=u.DN, dtype=np.float32)
        )

    @property
    def dq(self) -> np.ndarray:
        return self._get_node("dq", np.zeros(self.array_shape[1:], dtype=np.uint32))

    @property
    def dark_slope(self) -> u.Quantity:
        return self._get_node(
            "dark_slope", lambda: u.Quantity(np.zeros(self.array_shape[1:], dtype=np.float32), unit=u.DN / u.s, dtype=np.float32)
        )

    @property
    def dark_slope_error(self) -> u.Quantity:
        return self._get_node(
            "dark_slope_error",
            lambda: u.Quantity(np.zeros(self.array_shape[1:], dtype=np.float32), unit=u.DN / u.s, dtype=np.float32),
        )
