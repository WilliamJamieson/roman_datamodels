import numpy as np

from roman_datamodels.stnode import rad

from ..meta import Common

__all__ = ["WfiScienceRaw"]


class WfiScienceRaw(rad.DataModelNode):
    """
    Basic Roman Raw Science
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/wfi_science_raw-1.0.0"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (8, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8, 8)

    @rad.field
    def meta(self) -> Common:
        return self._get_node("meta", Common)

    @rad.field
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.uint16))

    @rad.field
    def amp33(self) -> np.ndarray:
        return self._get_node("amp33", lambda: np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16))

    @rad.field
    def resultantdq(self) -> np.ndarray:
        return self._get_node("resultantdq", lambda: np.zeros(self.array_shape, dtype=np.uint8))
