import numpy as np
from astropy import units as u

from roman_datamodels.stnode import _core

from ..enums import RefTypeEntry
from .ref import (
    RefCommonRef,
    RefExposureTypeRef,
)

__all__ = ["ReadnoiseRef"]


class ReadnoiseRef_Meta(_core.ImpliedNodeMixin, RefCommonRef, RefExposureTypeRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return ReadnoiseRef

    @_core.rad_field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.READNOISE)


class ReadnoiseRef(_core.DataModelNode):
    """
    Read noise reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/readnoise-1.0.0"

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
    def meta(self) -> ReadnoiseRef_Meta:
        return self._get_node("meta", ReadnoiseRef_Meta)

    @_core.rad_field
    def data(self) -> u.Quantity:
        return self._get_node("data", lambda: u.Quantity(np.zeros(self.array_shape, dtype=np.float32), u.DN, dtype=np.float32))
