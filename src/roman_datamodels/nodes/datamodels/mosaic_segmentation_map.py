from types import MappingProxyType

import numpy as np

from roman_datamodels.stnode import rad

from .meta import (
    Basic,
    MosaicBasic,
    Program,
)

__all__ = ["MosaicSegmentationMap"]


class MosaicSegmentationMap_Meta(rad.ImpliedNodeMixin, Basic):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MosaicSegmentationMap

    @rad.field
    def basic(self) -> MosaicBasic:
        return MosaicBasic()

    @rad.field
    def program(self) -> Program:
        return Program()


class MosaicSegmentationMap(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Segmentation map computed by the Source Catalog Step
    """

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
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> MosaicSegmentationMap_Meta:
        return MosaicSegmentationMap_Meta()

    @rad.field
    def data(self) -> np.ndarray:
        return np.zeros(self.array_shape, dtype=np.uint32)
