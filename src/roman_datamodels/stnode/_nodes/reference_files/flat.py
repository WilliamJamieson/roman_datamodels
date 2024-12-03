import numpy as np

from roman_datamodels.stnode import _core

from .ref import (
    RefCommonRef,
    RefOpticalElementRef,
)

__all__ = ["FlatRef"]


class FlatRefMeta(RefCommonRef, RefOpticalElementRef):
    @property
    def required(self) -> tuple[str]:
        return (
            *super().required,
            *super(RefCommonRef, self).required,
        )

    @property
    def reftype(self) -> str:
        return self._coerce(str, self._get_node("reftype", coerce=False), "reftype")


class FlatRef(_core.DataModelNode):
    """
    Flat field information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/flat-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "meta",
            "data",
            "dq",
            "err",
        )

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
    def meta(self) -> FlatRefMeta:
        return self._coerce(FlatRefMeta, self._get_node("meta", coerce=False), "meta")

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def dq(self) -> np.ndarray:
        return self._get_node("dq", np.zeros(self.array_shape, dtype=np.uint32))

    @property
    def err(self) -> np.ndarray:
        return self._get_node("err", np.zeros(self.array_shape, dtype=np.float32))
