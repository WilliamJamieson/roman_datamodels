import numpy as np

from roman_datamodels.stnode import rad

from ..meta import (
    Basic,
    MosaicBasic,
    Program,
)

__all__ = ["MosaicSegmentationMap"]


class MosaicSegmentationMap_Meta(rad.ImpliedNodeMixin, Basic):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return MosaicSegmentationMap

    @rad.rad_field
    def basic(self) -> MosaicBasic:
        return self._get_node("basic", MosaicBasic)

    @rad.rad_field
    def program(self) -> Program:
        return self._get_node("program", Program)


class MosaicSegmentationMap(rad.DataModelNode):
    """
    Segmentation map computed by the Source Catalog Step
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_segmentation_map-1.0.0"

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
        return (4096, 4096)

    @rad.rad_field
    def meta(self) -> MosaicSegmentationMap_Meta:
        return self._get_node("meta", MosaicSegmentationMap_Meta)

    @rad.rad_field
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.uint32))
