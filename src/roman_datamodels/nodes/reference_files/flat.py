from types import MappingProxyType

import numpy as np

from roman_datamodels.stnode import rad

from .ref import RefCommonRefOpticalElementRef, RefTypeEntry

__all__ = ["FlatRef"]


class FlatRef_Meta(rad.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return FlatRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.FLAT


class FlatRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/flat-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/flat-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/flat-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> FlatRef_Meta:
        return FlatRef_Meta()

    @rad.field
    def data(self) -> np.ndarray:
        return np.zeros(self.array_shape, dtype=np.float32)

    @rad.field
    def dq(self) -> np.ndarray:
        return np.zeros(self.array_shape, dtype=np.uint32)

    @rad.field
    def err(self) -> np.ndarray:
        return np.zeros(self.array_shape, dtype=np.float32)
