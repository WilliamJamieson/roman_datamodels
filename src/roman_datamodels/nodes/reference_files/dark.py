from types import MappingProxyType

import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

from .ref import (
    RefCommonRefOpticalElementRef,
    RefExposureTypeRef,
    RefTypeEntry,
)
from .ref.ref_exposure_type import RefExposureTypeRef_Exposure

__all__ = ["DarkRef"]


class DarkRef_Meta_Exposure(RefExposureTypeRef_Exposure, rad.ImpliedNodeMixin):
    """
    This class is the result of a very weird mixture similar to the ref_mixes but only
    applies to the dark schema.
    """

    @classmethod
    def asdf_implied_by(cls) -> type:
        return DarkRef_Meta

    @classmethod
    def asdf_required(cls) -> set[str]:
        return {
            *super().asdf_required(),
            *RefExposureTypeRef_Exposure.asdf_required(),
        }

    @rad.field
    def ngroups(self) -> int:
        return 6

    @rad.field
    def nframes(self) -> int:
        return 8

    @rad.field
    def groupgap(self) -> int:
        return 0

    @rad.field
    def ma_table_name(self) -> str:
        return rad.NOSTR

    @rad.field
    def ma_table_number(self) -> int:
        return rad.NOINT


class DarkRef_Meta(rad.ImpliedNodeMixin, RefCommonRefOpticalElementRef, RefExposureTypeRef):
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

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.DARK

    @rad.field
    def exposure(self) -> DarkRef_Meta_Exposure:
        return DarkRef_Meta_Exposure()


class DarkRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/dark-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/dark-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/dark-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int]:
        return (2, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (2, 8, 8)

    @rad.field
    def meta(self) -> DarkRef_Meta:
        return DarkRef_Meta()

    @rad.field
    def data(self) -> u.Quantity:
        return u.Quantity(np.zeros(self.array_shape, dtype=np.float32), unit=u.DN, dtype=np.float32)

    @rad.field
    def dq(self) -> np.ndarray:
        return np.zeros(self.array_shape[1:], dtype=np.uint32)

    @rad.field
    def dark_slope(self) -> u.Quantity:
        return u.Quantity(np.zeros(self.array_shape[1:], dtype=np.float32), unit=u.DN / u.s, dtype=np.float32)

    @rad.field
    def dark_slope_error(self) -> u.Quantity:
        return u.Quantity(np.zeros(self.array_shape[1:], dtype=np.float32), unit=u.DN / u.s, dtype=np.float32)
