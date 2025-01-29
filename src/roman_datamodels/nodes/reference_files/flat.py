from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import RefCommonRefOpticalElementRef, RefTypeEntry
from .ref.ref_mixes import _RefCommonRefOpticalElementRef

__all__ = ["FlatRef", "FlatRef_Meta"]


class FlatRef_Meta(  # type: ignore[misc]
    rad.ImpliedNodeMixin, RefCommonRefOpticalElementRef[_RefCommonRefOpticalElementRef]
):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return FlatRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.FLAT


_FlatRef: TypeAlias = FlatRef_Meta | npt.NDArray[np.float32] | npt.NDArray[np.uint32]


class FlatRef(rad.TaggedObjectNode[_FlatRef], rad.ArrayFieldMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/flat-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/flat-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/flat-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @rad.field
    def meta(self) -> FlatRef_Meta:
        return FlatRef_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def dq(self) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape, dtype=np.uint32)

    @rad.field
    def err(self) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)
