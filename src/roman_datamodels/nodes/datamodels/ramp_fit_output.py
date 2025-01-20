from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .meta.common import Common, _Common

__all__ = ["RampFitOutput"]


class RampFitOutput_Meta(rad.ImpliedNodeMixin[_Common], Common[_Common]):
    """
    The metadata for the RampFitOutput node
    -> only exists so that model_type can be correctly inferred
    """

    @classmethod
    def asdf_implied_by(cls) -> type:
        return RampFitOutput


_RampFitOutput: TypeAlias = RampFitOutput_Meta | npt.NDArray[np.float32]


class RampFitOutput(rad.TaggedObjectNode[_RampFitOutput], rad.ArrayFieldMixin[_RampFitOutput]):
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
    def default_array_shape(self) -> tuple[int, int, int]:
        return (8, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int, int]:
        return (2, 8, 8)

    @property
    @rad.field
    def meta(self: rad.Node) -> RampFitOutput_Meta:
        return RampFitOutput_Meta()

    @property
    @rad.field
    def slope(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def sigslope(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def yint(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def sigyint(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def pedestal(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape[1:], dtype=np.float32)

    @property
    @rad.field
    def weights(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def crmag(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def var_poisson(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)

    @property
    @rad.field
    def var_rnoise(self: rad.Node) -> npt.NDArray[np.float32]:
        return np.zeros(self.array_shape, dtype=np.float32)
