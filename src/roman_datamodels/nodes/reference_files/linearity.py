from types import MappingProxyType

import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry

__all__ = ["LinearityRef"]


class LinearityRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return LinearityRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.LINEARITY

    @rad.field
    def input_units(self) -> u.UnitBase:
        return u.DN

    @rad.field
    def output_units(self) -> u.UnitBase:
        return u.DN


class LinearityRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/linearity-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/linearity-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/linearity-1.0.0"
            }
        )

    @property
    def primary_array_name(self) -> str:
        return "coeffs"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (2, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (2, 8, 8)

    @rad.field
    def meta(self) -> LinearityRef_Meta:
        return LinearityRef_Meta()

    @rad.field
    def coeffs(self) -> np.ndarray:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def dq(self) -> np.ndarray:
        return np.zeros(self.array_shape[1:], dtype=np.uint32)
