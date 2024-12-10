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
        return self._get_node("basic", MosaicBasic)

    @rad.field
    def program(self) -> Program:
        return self._get_node("program", Program)


class MosaicSegmentationMap(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Segmentation map computed by the Source Catalog Step
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_segmentation_map-1.0.0"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> MosaicSegmentationMap_Meta:
        return self._get_node("meta", MosaicSegmentationMap_Meta)

    @rad.field
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.uint32))
