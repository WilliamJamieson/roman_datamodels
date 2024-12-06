import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core

from ..enums import RefTypeEntry
from .ref import RefCommonRef

__all__ = ["RefpixRef"]


class RefpixRef_Meta(_core.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefpixRef

    @_core.rad_field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.REFPIX)

    @_core.rad_field
    def input_units(self) -> u.UnitBase:
        return self._get_node("input_units", lambda: u.DN)

    @_core.rad_field
    def output_units(self) -> u.UnitBase:
        return self._get_node("output_units", lambda: u.DN)


class RefpixRef(_core.DataModelNode):
    """
    Reference pixel correction reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/refpix-1.0.0"

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("gamma"):
            return self.gamma.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (32, 286721)

    @_core.rad_field
    def meta(self) -> RefpixRef_Meta:
        return self._get_node("meta", RefpixRef_Meta)

    @_core.rad_field
    def gamma(self) -> np.ndarray:
        return self._get_node("gamma", lambda: np.zeros(self.array_shape, dtype=np.complex128))

    @_core.rad_field
    def zeta(self) -> np.ndarray:
        return self._get_node("zeta", lambda: np.zeros(self.array_shape, dtype=np.complex128))

    @_core.rad_field
    def alpha(self) -> np.ndarray:
        return self._get_node("alpha", lambda: np.zeros(self.array_shape, dtype=np.complex128))
