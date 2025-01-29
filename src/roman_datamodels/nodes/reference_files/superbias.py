from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry
from .ref.ref_common import _RefCommonRef

__all__ = ["SuperbiasRef", "SuperbiasRef_Meta"]


class SuperbiasRef_Meta(rad.ImpliedNodeMixin[_RefCommonRef], RefCommonRef[_RefCommonRef]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return SuperbiasRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.BIAS


_SuperbiasRef: TypeAlias = SuperbiasRef_Meta | npt.NDArray[np.float32] | npt.NDArray[np.uint32]


class SuperbiasRef(rad.TaggedObjectNode[_SuperbiasRef], rad.ArrayFieldMixin[_SuperbiasRef]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/superbias-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/superbias-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/superbias-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @rad.field
    def meta(self) -> SuperbiasRef_Meta:
        return SuperbiasRef_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def dq(self) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape, dtype=np.uint32)

    @rad.field
    def err(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)
