import numpy as np

from roman_datamodels.stnode import _core

from .ref import RefCommonRef

__all__ = ["MaskRef"]


class MaskRefMeta(RefCommonRef):
    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "MASK")


class MaskRef(_core.DataModelNode):
    """
    DQ Mask reference schema
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/mask-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "meta",
            "dq",
        )

    @property
    def array_shape(self) -> tuple[int]:
        """Return the shape of the data array"""
        # The datamodel shape is based of the data array
        if self._has_node("dq"):
            return self.dq.shape

        # Allow for one to shrink the data size default
        if self._has_node("array_shape"):
            return self._data["array_shape"]

        # default fall-back
        return (4096, 4096)

    @property
    def meta(self) -> MaskRefMeta:
        return self._get_node("meta", MaskRefMeta)

    @property
    def dq(self) -> np.ndarray:
        return self._get_node("dq", lambda: np.zeros(self.array_shape, dtype=np.uint32))
