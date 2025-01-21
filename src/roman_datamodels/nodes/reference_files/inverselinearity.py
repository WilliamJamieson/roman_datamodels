from types import MappingProxyType

import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry

__all__ = ["InverselinearityRef"]


class InverselinearityRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return InverselinearityRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.INVERSELINEARITY

    @rad.field
    def input_units(self) -> u.UnitBase:
        return u.DN

    @rad.field
    def output_units(self) -> u.UnitBase:
        return u.DN


class InverselinearityRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Inverse linearity correction reference schema
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/inverselinearity-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/inverselinearity-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/inverselinearity-1.0.0"
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
    def meta(self) -> InverselinearityRef_Meta:
        return InverselinearityRef_Meta()

    @rad.field
    def coeffs(self) -> np.ndarray:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def dq(self) -> np.ndarray:
        return np.zeros(self.array_shape[1:], dtype=np.uint32)
