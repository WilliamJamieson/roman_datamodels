import numpy as np

from roman_datamodels.stnode import rad

from ..enums import RefTypeEntry
from .ref import RefCommonRef

__all__ = ["MaskRef"]


class MaskRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MaskRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.MASK)


class MaskRef(rad.DataModelNode):
    """
    DQ Mask reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/mask-1.0.0"

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

    @rad.field
    def meta(self) -> MaskRef_Meta:
        return self._get_node("meta", MaskRef_Meta)

    @rad.field
    def dq(self) -> np.ndarray:
        return self._get_node("dq", lambda: np.zeros(self.array_shape, dtype=np.uint32))
