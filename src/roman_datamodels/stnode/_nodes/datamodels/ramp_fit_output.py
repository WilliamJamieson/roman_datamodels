import numpy as np

from roman_datamodels.stnode import _core

from ..meta import Common

__all__ = ["RampFitOutput"]


class RampFitOutput(_core.DataModelNode):
    """
    Ramp fit output schema
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/ramp_fit_output-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "meta",
            "slope",
            "sigslope",
            "yint",
            "sigyint",
            "pedestal",
            "weights",
            "crmag",
            "var_poisson",
            "var_rnoise",
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
    def slope(self) -> np.ndarray:
        return self._get_node("slope", np.zeros(self.array_shape, dtype=np.float32))

    @property
    def sigslope(self) -> np.ndarray:
        return self._get_node("sigslope", np.zeros(self.array_shape, dtype=np.float32))

    @property
    def yint(self) -> np.ndarray:
        return self._get_node("yint", np.zeros(self.array_shape, dtype=np.float32))

    @property
    def sigyint(self) -> np.ndarray:
        return self._get_node("sigyint", np.zeros(self.array_shape, dtype=np.float32))

    @property
    def pedestal(self) -> np.ndarray:
        return self._get_node("pedestal", np.zeros(self.array_shape[1:], dtype=np.float32))

    @property
    def weights(self) -> np.ndarray:
        return self._get_node("weights", np.zeros(self.array_shape, dtype=np.float32))

    @property
    def crmag(self) -> np.ndarray:
        return self._get_node("crmag", np.zeros(self.array_shape, dtype=np.float32))

    @property
    def var_poisson(self) -> np.ndarray:
        return self._get_node("var_poisson", np.zeros(self.array_shape, dtype=np.float32))

    @property
    def var_rnoise(self) -> np.ndarray:
        return self._get_node("var_rnoise", np.zeros(self.array_shape, dtype=np.float32))
