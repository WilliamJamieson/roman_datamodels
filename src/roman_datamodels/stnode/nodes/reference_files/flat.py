import numpy as np

from roman_datamodels.stnode import _core

from .ref import RefCommonRefOpticalElementRef

__all__ = ["FlatRef"]


class FlatRef_Meta(_core.ImpliedNodeMixin, RefCommonRefOpticalElementRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return FlatRef

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "FLAT")


class FlatRef(_core.DataModelNode):
    """
    Flat field information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/flat-1.0.0"

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
        return (4096, 4096)

    @property
    def meta(self) -> FlatRef_Meta:
        return self._get_node("meta", FlatRef_Meta)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def dq(self) -> np.ndarray:
        return self._get_node("dq", lambda: np.zeros(self.array_shape, dtype=np.uint32))

    @property
    def err(self) -> np.ndarray:
        return self._get_node("err", lambda: np.zeros(self.array_shape, dtype=np.float32))
