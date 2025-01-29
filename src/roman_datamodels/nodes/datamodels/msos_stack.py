from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .meta.common import Common, _Common

__all__ = ["MsosStack", "MsosStack_Meta"]


_MsosStack_Meta: TypeAlias = _Common | str


class MsosStack_Meta(rad.ImpliedNodeMixin[_MsosStack_Meta], Common[_MsosStack_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MsosStack

    @rad.field
    def image_list(self) -> str:
        return rad.NOSTR


_MsosStack: TypeAlias = MsosStack_Meta | npt.NDArray[np.float64] | npt.NDArray[np.uint8]


class MsosStack(rad.TaggedObjectNode[_MsosStack_Meta], rad.ArrayFieldMixin[_MsosStack]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/msos_stack-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/msos_stack-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/msos_stack-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @rad.field
    def meta(self) -> MsosStack_Meta:
        return MsosStack_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.float64]:
        return np.zeros(self.array_shape, dtype=np.float64)

    @rad.field
    def uncertainty(self) -> npt.NDArray[np.float64]:
        return np.zeros(self.array_shape, dtype=np.float64)

    @rad.field
    def mask(self) -> npt.NDArray[np.uint8]:
        return np.zeros(self.array_shape, dtype=np.uint8)

    @rad.field
    def coverage(self) -> npt.NDArray[np.uint8]:
        return np.zeros(self.array_shape, dtype=np.uint8)
