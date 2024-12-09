import numpy as np

from roman_datamodels.stnode import rad

from ..enums import RefTypeEntry
from .ref import RefCommonRefOpticalElementRef

__all__ = ["IpcRef"]


class IpcRef_Meta(rad.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return IpcRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.IPC)


class IpcRef(rad.DataModelNode):
    """
    IPC kernel reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/ipc-1.0.0"

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("data"):
            return self.data.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (3, 3)

    @rad.field
    def meta(self) -> IpcRef_Meta:
        return self._get_node("meta", IpcRef_Meta)

    @rad.field
    def data(self) -> np.ndarray:
        def _default():
            data = np.zeros(self.array_shape, dtype=np.float32)
            data[int(np.floor(self.array_shape[0] / 2))][int(np.floor(self.array_shape[1] / 2))] = 1.0
            return data

        return self._get_node("data", _default)
