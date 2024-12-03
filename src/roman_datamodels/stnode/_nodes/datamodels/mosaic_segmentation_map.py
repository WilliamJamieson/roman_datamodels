import numpy as np

from roman_datamodels.stnode import _core

from ..meta import (
    Basic,
    MosaicBasic,
    Program,
)

__all__ = ["MosaicSegmentationMap"]


class MosaicSegmentationMapMeta(Basic):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            "basic",
            "program",
        )

    @property
    def basic(self) -> MosaicBasic:
        return self._get_node("basic", MosaicBasic)

    @property
    def program(self) -> Program:
        return self._get_node("program", Program)


class MosaicSegmentationMap(_core.DataModelNode):
    """
    Segmentation map computed by the Source Catalog Step
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_segmentation_map-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "data",
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
        return (4096, 4096)

    @property
    def meta(self) -> MosaicSegmentationMapMeta:
        return self._get_node("meta", MosaicSegmentationMapMeta)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", np.zeros(self.array_shape, dtype=np.int32))
