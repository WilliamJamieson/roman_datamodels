import numpy as np

from roman_datamodels.stnode import _core

from .ref import RefCommonRef

__all__ = ["SuperbiasRef"]


class SuperbiasRef_Meta(_core.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return SuperbiasRef

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "BIAS")


class SuperbiasRef(_core.DataModelNode):
    """
    Super-bias reference schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/superbias-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
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

        return (4096, 4096)

    @property
    def meta(self) -> SuperbiasRef_Meta:
        return self._get_node("meta", SuperbiasRef_Meta)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @property
    def dq(self) -> np.ndarray:
        return self._get_node("dq", lambda: np.zeros(self.array_shape, dtype=np.uint32))

    @property
    def err(self) -> np.ndarray:
        return self._get_node("err", lambda: np.zeros(self.array_shape, dtype=np.float32))
