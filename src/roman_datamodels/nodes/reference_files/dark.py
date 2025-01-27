from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import (
    RefCommonRefOpticalElementRef,
    RefExposureTypeRef,
    RefTypeEntry,
)
from .ref.ref_exposure_type import RefExposureTypeRef_Exposure, _RefExposureTypeRef, _RefExposureTypeRef_Exposure
from .ref.ref_mixes import _RefCommonRefOpticalElementRef

__all__ = ["DarkRef"]

_DarkRef_Meta_Exposure: TypeAlias = _RefExposureTypeRef_Exposure | str | int


class DarkRef_Meta_Exposure(RefExposureTypeRef_Exposure[_DarkRef_Meta_Exposure], rad.ImpliedNodeMixin[_DarkRef_Meta_Exposure]):
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

    @property
    def schema_required(self) -> set[str]:
        return self.asdf_required()

    @rad.field
    def ma_table_name(self) -> str:
        return rad.NOSTR

    @rad.field
    def ma_table_number(self) -> int:
        return rad.NOINT


_DarkRef_Meta: TypeAlias = _RefCommonRefOpticalElementRef | _RefExposureTypeRef | DarkRef_Meta_Exposure


class DarkRef_Meta(  # type: ignore[misc]
    rad.ImpliedNodeMixin[_DarkRef_Meta], RefCommonRefOpticalElementRef[_DarkRef_Meta], RefExposureTypeRef[_DarkRef_Meta]
):
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
    def exposure(self) -> DarkRef_Meta_Exposure:  # type: ignore[override]
        return DarkRef_Meta_Exposure()


_DarkRef: TypeAlias = DarkRef_Meta | npt.NDArray[np.float32] | npt.NDArray[np.uint32]


class DarkRef(rad.TaggedObjectNode[_DarkRef], rad.ArrayFieldMixin[_DarkRef]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/dark-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/dark-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/dark-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int, int]:
        return (2, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int, int]:
        return (2, 8, 8)

    @rad.field
    def meta(self) -> DarkRef_Meta:
        return DarkRef_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def dq(self) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape[1:], dtype=np.uint32)

    @rad.field
    def dark_slope(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape[1:], dtype=np.float32)

    @rad.field
    def dark_slope_error(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape[1:], dtype=np.float32)
