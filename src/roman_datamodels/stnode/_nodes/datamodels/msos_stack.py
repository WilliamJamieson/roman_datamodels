import numpy as np

from roman_datamodels.stnode import _core, _default

from ..meta import Common

__all__ = ["MsosStack"]


class MsosStackMeta(Common):
    @property
    def image_list(self) -> str:
        return self._get_node("image_list", _default.NOSTR)


class MsosStack(_core.DataModelNode):
    """
    Level 3 schema for SSC's MSOS stack products
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/msos_stack-1.0.0"

    @property
    def required(self) -> tuple[str]:
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
        if self._has_node("shape"):
            return self._data["shape"]

        # default fall-back
        return (4096, 4096)

    @property
    def meta(self) -> MsosStackMeta:
        return self._get_node("meta", MsosStackMeta)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", np.zeros(self.array_shape, dtype=np.float64))

    @property
    def uncertainty(self) -> np.ndarray:
        return self._get_node("uncertainty", np.zeros(self.array_shape, dtype=np.float64))

    @property
    def mask(self) -> np.ndarray:
        return self._get_node("mask", np.zeros(self.array_shape, dtype=np.uint8))

    @property
    def coverage(self) -> np.ndarray:
        return self._get_node("coverage", np.zeros(self.array_shape, dtype=np.uint8))
