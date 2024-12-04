import numpy as np

from roman_datamodels.stnode import _core, _default

from ..meta import Common

__all__ = ["MsosStack"]


class MsosStack_Meta(Common):
    @property
    def image_list(self) -> str:
        return self._get_node("image_list", lambda: _default.NOSTR)


class MsosStack(_core.DataModelNode):
    """
    Level 3 schema for SSC's MSOS stack products
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/msos_stack-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "data",
            "uncertainty",
            "mask",
            "coverage",
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
    def meta(self) -> MsosStack_Meta:
        return self._get_node("meta", MsosStack_Meta)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @property
    def uncertainty(self) -> np.ndarray:
        return self._get_node("uncertainty", lambda: np.zeros(self.array_shape, dtype=np.float64))

    @property
    def mask(self) -> np.ndarray:
        return self._get_node("mask", lambda: np.zeros(self.array_shape, dtype=np.uint8))

    @property
    def coverage(self) -> np.ndarray:
        return self._get_node("coverage", lambda: np.zeros(self.array_shape, dtype=np.uint8))
