import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

from ..enums import RefTypeEntry
from .ref import RefCommonRef

__all__ = ["SaturationRef"]


class SaturationRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return SaturationRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.SATURATION)


class SaturationRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Saturation reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/saturation-1.0.0"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> SaturationRef_Meta:
        return self._get_node("meta", SaturationRef_Meta)

    @rad.field
    def data(self) -> u.Quantity:
        return self._get_node("data", lambda: u.Quantity(np.zeros(self.array_shape, dtype=np.float32), u.DN, dtype=np.float32))

    @rad.field
    def dq(self) -> np.ndarray:
        return self._get_node("dq", lambda: np.zeros(self.array_shape, dtype=np.uint32))
