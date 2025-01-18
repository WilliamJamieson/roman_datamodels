from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry
from .ref.ref_common import _RefCommonRef

__all__ = ["SaturationRef"]


class SaturationRef_Meta(rad.ImpliedNodeMixin[_RefCommonRef], RefCommonRef[_RefCommonRef]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return SaturationRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.SATURATION


_SaturationRef: TypeAlias = SaturationRef_Meta | npt.NDArray[np.float32] | npt.NDArray[np.uint32]


class SaturationRef(rad.TaggedObjectNode[_SaturationRef], rad.ArrayFieldMixin[_SaturationRef]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/saturation-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/saturation-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/saturation-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @rad.field
    def meta(self) -> SaturationRef_Meta:
        return SaturationRef_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def dq(self) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape, dtype=np.uint32)
