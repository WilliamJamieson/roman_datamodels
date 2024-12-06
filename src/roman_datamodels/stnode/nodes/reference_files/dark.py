import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core, _default

from .ref import (
    RefCommonRefOpticalElementRef,
    RefExposureTypeRef,
)
from .ref.ref_exposure_type import RefExposureTypeRef_Exposure

__all__ = ["DarkRef"]


class DarkRef_Meta_Exposure(RefExposureTypeRef_Exposure, _core.ImpliedNodeMixin):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return DarkRef_Meta

    @classmethod
    def asdf_required(cls) -> set[str]:
        return {
            *super().asdf_required(),
            *RefExposureTypeRef_Exposure.asdf_required(),
        }

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
        return self._get_node("ma_table_number", lambda: _default.NOINT)


class DarkRef_Meta(_core.ImpliedNodeMixin, RefCommonRefOpticalElementRef, RefExposureTypeRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return DarkRef

    @classmethod
    def asdf_required(cls) -> set[str]:
        return {
            *super().asdf_required(),
            *RefCommonRefOpticalElementRef.asdf_required(),
            *RefExposureTypeRef.asdf_required(),
        }

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "DARK")

    @property
    def exposure(self) -> DarkRef_Meta_Exposure:
        return self._get_node("exposure", DarkRef_Meta_Exposure)


class DarkRef(_core.DataModelNode):
    """
    Dark reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/dark-1.0.0"

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
    def meta(self) -> DarkRef_Meta:
        return self._get_node("meta", DarkRef_Meta)

    @property
    def data(self) -> u.Quantity:
        return self._get_node(
            "data", lambda: u.Quantity(np.zeros(self.array_shape, dtype=np.float32), unit=u.DN, dtype=np.float32)
        )

    @property
    def dq(self) -> np.ndarray:
        return self._get_node("dq", lambda: np.zeros(self.array_shape[1:], dtype=np.uint32))

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
