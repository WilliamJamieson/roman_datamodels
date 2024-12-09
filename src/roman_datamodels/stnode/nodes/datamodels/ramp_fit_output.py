import numpy as np

from roman_datamodels.stnode import rad

from ..meta import Common

__all__ = ["RampFitOutput"]


class RampFitOutput(rad.DataModelNode):
    """
    Ramp fit output schema
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/ramp_fit_output-1.0.0"

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

    @rad.field
    def meta(self) -> Common:
        return self._get_node("meta", Common)

    @rad.field
    def slope(self) -> np.ndarray:
        return self._get_node("slope", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def sigslope(self) -> np.ndarray:
        return self._get_node("sigslope", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def yint(self) -> np.ndarray:
        return self._get_node("yint", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def sigyint(self) -> np.ndarray:
        return self._get_node("sigyint", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def pedestal(self) -> np.ndarray:
        return self._get_node("pedestal", lambda: np.zeros(self.array_shape[1:], dtype=np.float32))

    @rad.field
    def weights(self) -> np.ndarray:
        return self._get_node("weights", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def crmag(self) -> np.ndarray:
        return self._get_node("crmag", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def var_poisson(self) -> np.ndarray:
        return self._get_node("var_poisson", lambda: np.zeros(self.array_shape, dtype=np.float32))

    @rad.field
    def var_rnoise(self) -> np.ndarray:
        return self._get_node("var_rnoise", lambda: np.zeros(self.array_shape, dtype=np.float32))
