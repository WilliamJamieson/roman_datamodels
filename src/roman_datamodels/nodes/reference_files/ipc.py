from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .ref import RefCommonRefOpticalElementRef, RefTypeEntry
from .ref.ref_mixes import _RefCommonRefOpticalElementRef

__all__ = ["IpcRef"]


class IpcRef_Meta(  # type: ignore[misc]
    rad.ImpliedNodeMixin[_RefCommonRefOpticalElementRef], RefCommonRefOpticalElementRef[_RefCommonRefOpticalElementRef]
):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return IpcRef

    @property
    @rad.field
    def reftype(self: rad.Node) -> RefTypeEntry:
        return RefTypeEntry.IPC


_IpcRef: TypeAlias = IpcRef_Meta | npt.NDArray[np.float32]


class IpcRef(rad.TaggedObjectNode[_IpcRef], rad.ArrayFieldMixin[_IpcRef]):
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
    def default_array_shape(self) -> tuple[int, int]:
        return (3, 3)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return self.default_array_shape

    @property
    @rad.field
    def meta(self: rad.Node) -> IpcRef_Meta:
        return IpcRef_Meta()

    @property
    @rad.field
    def data(self: rad.Node) -> npt.NDArray[np.float32]:
        data = np.zeros(self.array_shape, dtype=np.float32)
        data[int(np.floor(self.array_shape[0] / 2))][int(np.floor(self.array_shape[1] / 2))] = 1.0
        return data
