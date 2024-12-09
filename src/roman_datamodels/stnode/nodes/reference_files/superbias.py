import numpy as np

from roman_datamodels.stnode import rad

from ..enums import RefTypeEntry
from .ref import RefCommonRef

__all__ = ["SuperbiasRef"]


class SuperbiasRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return SuperbiasRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.BIAS)


class SuperbiasRef(rad.DataModelNode):
    """
    Super-bias reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/superbias-1.0.0"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> SuperbiasRef_Meta:
        return self._get_node("meta", SuperbiasRef_Meta)

    @rad.field
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def dq(self) -> np.ndarray:
        return self._get_node("dq", lambda: np.zeros(self.array_shape, dtype=np.uint32))

    @rad.field
    def err(self) -> np.ndarray:
        return self._get_node("err", lambda: np.zeros(self.array_shape, dtype=np.float32))
