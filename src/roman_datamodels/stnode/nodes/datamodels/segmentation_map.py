import numpy as np

from roman_datamodels.stnode import rad

from .meta import (
    Basic,
    Program,
    Visit,
    WfiOpticalElement,
)

__all__ = ["SegmentationMap"]


class SegmentationMap_Meta(rad.ImpliedNodeMixin, Basic):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return SegmentationMap

    @rad.field
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", lambda: WfiOpticalElement.F158)

    @rad.field
    def program(self) -> Program:
        return self._get_node("program", Program)

    @rad.field
    def visit(self) -> Visit:
        return self._get_node("visit", Visit)


class SegmentationMap(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Segmentation map computed by the Source Catalog Step
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/segmentation_map-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/segmentation_map-1.0.0"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8)

    @rad.field
    def meta(self) -> SegmentationMap_Meta:
        return self._get_node("meta", SegmentationMap_Meta)

    @rad.field
    def data(self) -> np.ndarray:
        return self._get_node("data", lambda: np.zeros(self.array_shape, dtype=np.uint32))
