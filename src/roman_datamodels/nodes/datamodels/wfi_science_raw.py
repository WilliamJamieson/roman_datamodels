from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .meta import Common
from .meta.common import _Common

__all__ = ["WfiScienceRaw", "WfiScienceRaw_Meta"]


class WfiScienceRaw_Meta(rad.ImpliedNodeMixin, Common[_Common]):
    """
    The metadata for the WfiScienceRaw node
    -> only exists so that model_type can be correctly inferred
    """

    @classmethod
    def asdf_implied_by(cls) -> type:
        return WfiScienceRaw


_WfiScienceRaw: TypeAlias = WfiScienceRaw_Meta | npt.NDArray[np.uint16] | npt.NDArray[np.uint8]


class WfiScienceRaw(rad.TaggedObjectNode[_WfiScienceRaw], rad.ArrayFieldMixin[_WfiScienceRaw]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/wfi_science_raw-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/wfi_science_raw-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/wfi_science_raw-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int, int]:
        return (8, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int, int]:
        return (2, 8, 8)

    @rad.field
    def meta(self) -> WfiScienceRaw_Meta:
        return WfiScienceRaw_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.uint16]:
        return np.zeros(self.array_shape, dtype=np.uint16)

    @rad.field
    def amp33(self) -> npt.NDArray[np.uint16]:
        return np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16)

    @rad.field
    def resultantdq(self) -> npt.NDArray[np.uint8]:
        return np.zeros(self.array_shape, dtype=np.uint8)
