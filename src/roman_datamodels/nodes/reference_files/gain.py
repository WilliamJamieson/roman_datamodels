from types import MappingProxyType

import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry

__all__ = ["GainRef"]


class GainRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return GainRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.GAIN


class GainRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Gain reference schema
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/gain-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/gain-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/gain-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> GainRef_Meta:
        return GainRef_Meta()

    @rad.field
    def data(self) -> u.Quantity:
        return u.Quantity(np.zeros(self.array_shape, dtype=np.float32), u.electron / u.DN, dtype=np.float32)
