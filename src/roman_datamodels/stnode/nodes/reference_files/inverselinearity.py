import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core

from ..enums import RefTypeEntry
from .ref import RefCommonRef

__all__ = ["InverselinearityRef"]


class InverselinearityRef_Meta(_core.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return InverselinearityRef

    @_core.rad_field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.INVERSELINEARITY)

    @_core.rad_field
    def input_units(self) -> u.UnitBase:
        return self._get_node("input_units", lambda: u.DN)

    @_core.rad_field
    def output_units(self) -> u.UnitBase:
        return self._get_node("output_units", lambda: u.DN)


class InverselinearityRef(_core.DataModelNode):
    """
    Inverse linearity correction reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/inverselinearity-1.0.0"

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("coeffs"):
            return self.coeffs.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (2, 4096, 4096)

    @_core.rad_field
    def meta(self) -> InverselinearityRef_Meta:
        return self._get_node("meta", InverselinearityRef_Meta)

    @_core.rad_field
    def coeffs(self) -> np.ndarray:
        return self._get_node("coeffs", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @_core.rad_field
    def dq(self) -> np.ndarray:
        return self._get_node("dq", lambda: np.zeros(self.array_shape[1:], dtype=np.uint32))
