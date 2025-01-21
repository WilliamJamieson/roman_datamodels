from types import MappingProxyType

import numpy as np

from roman_datamodels.stnode import rad

from .meta import Common

__all__ = ["RampFitOutput"]


class RampFitOutput_Meta(rad.ImpliedNodeMixin, Common):
    """
    The metadata for the RampFitOutput node
    -> only exists so that model_type can be correctly inferred
    """

    @classmethod
    def asdf_implied_by(cls) -> type:
        return RampFitOutput


class RampFitOutput(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Ramp fit output schema
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/ramp_fit_output-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/ramp_fit_output-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/ramp_fit_output-1.0.0"
            }
        )

    @property
    def primary_array_name(self) -> str:
        return "slope"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (8, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (2, 8, 8)

    @rad.field
    def meta(self) -> RampFitOutput_Meta:
        return self._get_node("meta", RampFitOutput_Meta)

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
