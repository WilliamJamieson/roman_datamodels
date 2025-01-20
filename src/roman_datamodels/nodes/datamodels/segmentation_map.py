from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

from roman_datamodels.stnode import rad

from .meta import (
    Basic,
    Program,
    Visit,
    WfiOpticalElement,
)
from .meta.basic import _Basic

__all__ = ["SegmentationMap"]


_SegmentationMap_Meta: TypeAlias = _Basic | Program | Visit | WfiOpticalElement


class SegmentationMap_Meta(rad.ImpliedNodeMixin[_SegmentationMap_Meta], Basic[_SegmentationMap_Meta]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return SegmentationMap

    @property
    @rad.field
    def optical_element(self: rad.Node) -> WfiOpticalElement:
        return WfiOpticalElement.F158

    @property
    @rad.field
    def program(self: rad.Node) -> Program:
        return Program()

    @property
    @rad.field
    def visit(self: rad.Node) -> Visit:
        return Visit()


_SegmentationMap: TypeAlias = SegmentationMap_Meta | npt.NDArray[np.uint32]


class SegmentationMap(rad.TaggedObjectNode[_SegmentationMap], rad.ArrayFieldMixin[_SegmentationMap]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/segmentation_map-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/segmentation_map-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/segmentation_map-1.0.0"
            }
        )

    @property
    def default_array_shape(self) -> tuple[int, int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int, int]:
        return (8, 8)

    @property
    @rad.field
    def meta(self: rad.Node) -> SegmentationMap_Meta:
        return SegmentationMap_Meta()

    @property
    @rad.field
    def data(self: rad.Node) -> npt.NDArray[np.uint32]:
        return np.zeros(self.array_shape, dtype=np.uint32)
