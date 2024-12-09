import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

from ..enums import RefTypeEntry
from .ref import RefCommonRef

__all__ = ["GainRef"]


class GainRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return GainRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.GAIN)


class GainRef(rad.DataModelNode):
    """
    Gain reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/gain-1.0.0"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> GainRef_Meta:
        return self._get_node("meta", GainRef_Meta)

    @rad.field
    def data(self) -> u.Quantity:
        return self._get_node(
            "data", lambda: u.Quantity(np.zeros(self.array_shape, dtype=np.float32), u.electron / u.DN, dtype=np.float32)
        )
