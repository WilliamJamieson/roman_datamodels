from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .meta import (
    Basic,
    MosaicBasic,
    Program,
)
from .meta.basic import _Basic

__all__ = ["MosaicSegmentationMap", "MosaicSegmentationMap_Meta"]

_MosaicSegmentationMap_Meta: TypeAlias = _Basic | MosaicBasic | Program


class MosaicSegmentationMap_Meta(rad.ImpliedNodeMixin, Basic[_MosaicSegmentationMap_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MosaicSegmentationMap

    @rad.field
    def basic(self) -> MosaicBasic:
        return MosaicBasic()

    @rad.field
    def program(self) -> Program:
        return Program()


_MosaicSegmentationMap: TypeAlias = MosaicSegmentationMap_Meta | npt.NDArray[np.uint32]


class MosaicSegmentationMap(rad.TaggedObjectNode[_MosaicSegmentationMap], rad.ArrayFieldMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/mosaic_segmentation_map-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/mosaic_segmentation_map-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/mosaic_segmentation_map-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @rad.field
    def meta(self) -> MosaicSegmentationMap_Meta:
        return MosaicSegmentationMap_Meta()

    @rad.field
    def data(self) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape, dtype=np.uint32)
