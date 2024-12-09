import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

from ..enums import RefTypeEntry
from .ref import RefCommonRef

__all__ = ["RefpixRef"]


class RefpixRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefpixRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.REFPIX)

    @rad.field
    def input_units(self) -> u.UnitBase:
        return self._get_node("input_units", lambda: u.DN)

    @rad.field
    def output_units(self) -> u.UnitBase:
        return self._get_node("output_units", lambda: u.DN)


class RefpixRef(rad.DataModelNode):
    """
    Reference pixel correction reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/refpix-1.0.0"

    @property
    def primary_array_name(self) -> str:
        return "gamma"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (32, 286721)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (32, 840)

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

    @rad.field
    def meta(self) -> RefpixRef_Meta:
        return self._get_node("meta", RefpixRef_Meta)

    @rad.field
    def gamma(self) -> np.ndarray:
        return self._get_node("gamma", lambda: np.zeros(self.array_shape, dtype=np.complex128))

    @rad.field
    def zeta(self) -> np.ndarray:
        return self._get_node("zeta", lambda: np.zeros(self.array_shape, dtype=np.complex128))

    @rad.field
    def alpha(self) -> np.ndarray:
        return self._get_node("alpha", lambda: np.zeros(self.array_shape, dtype=np.complex128))
