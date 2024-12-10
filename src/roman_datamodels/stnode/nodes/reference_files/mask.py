import numpy as np

from roman_datamodels.stnode import rad

from .ref import RefCommonRef, RefTypeEntry

__all__ = ["MaskRef"]


class MaskRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MaskRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.MASK)


class MaskRef(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    DQ Mask reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/mask-1.0.0"

    def primary_array_name(self) -> str:
        return "dq"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> MaskRef_Meta:
        return self._get_node("meta", MaskRef_Meta)

    @rad.field
    def dq(self) -> np.ndarray:
        return self._get_node("dq", lambda: np.zeros(self.array_shape, dtype=np.uint32))
