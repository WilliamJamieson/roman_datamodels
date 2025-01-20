from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry
from .ref.ref_common import _RefCommonRef

__all__ = ["MaskRef"]


class MaskRef_Meta(rad.ImpliedNodeMixin[_RefCommonRef], RefCommonRef[_RefCommonRef]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MaskRef

    @property
    @rad.field
    def reftype(self: rad.Node) -> RefTypeEntry:
        return RefTypeEntry.MASK


_MaskRef: TypeAlias = MaskRef_Meta | npt.NDArray[np.uint32]


class MaskRef(rad.TaggedObjectNode[_MaskRef], rad.ArrayFieldMixin[_MaskRef]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/mask-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/mask-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/mask-1.0.0"
            }
        )

    @property
    def primary_array_name(self) -> str:
        return "dq"

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @property
    @rad.field
    def meta(self: rad.Node) -> MaskRef_Meta:
        return MaskRef_Meta()

    @property
    @rad.field
    def dq(self: rad.Node) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape, dtype=np.uint32)
