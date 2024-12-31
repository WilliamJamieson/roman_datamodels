from types import MappingProxyType

import numpy as np

from roman_datamodels.stnode import rad

from .ref import RefCommonRefOpticalElementRef, RefTypeEntry

__all__ = ["IpcRef"]


class IpcRef_Meta(rad.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return IpcRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.IPC


class IpcRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/ipc-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/ipc-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ipc-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int]:
        return (3, 3)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return self.default_array_shape

    @rad.field
    def meta(self) -> IpcRef_Meta:
        return IpcRef_Meta()

    @rad.field
    def data(self) -> np.ndarray:
        data = np.zeros(self.array_shape, dtype=np.float32)
        data[int(np.floor(self.array_shape[0] / 2))][int(np.floor(self.array_shape[1] / 2))] = 1.0
        return data
