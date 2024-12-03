import numpy as np

from roman_datamodels.stnode import _core

from ..meta import Common

__all__ = ["WfiScienceRaw"]


class WfiScienceRaw(_core.DataModelNode):
    """
    Basic Roman Raw Science
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/wfi_science_raw-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "data",
            "amp33",
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
        return (8, 4096, 4096)

    @property
    def meta(self) -> Common:
        return self._get_node("meta", Common)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", np.zeros(self.array_shape, dtype=np.uint16))

    @property
    def amp33(self) -> np.ndarray:
        return self._get_node("amp33", np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16))

    @property
    def resultantdq(self) -> np.ndarray:
        return self._get_node("resultantdq", np.zeros(self.array_shape, dtype=np.uint8))
