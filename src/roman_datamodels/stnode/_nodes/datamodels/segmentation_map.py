import numpy as np

from roman_datamodels.stnode import _core

from ..meta import (
    Basic,
    Program,
    Visit,
    WfiOpticalElement,
)

__all__ = ["SegmentationMap"]


class SegmentationMap_Meta(Basic):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            "optical_element",
            "program",
            "visit",
        )

    @property
    def optical_element(self) -> WfiOpticalElement:
        return self._coerce(WfiOpticalElement, self._get_node("optical_element", coerce=False), "optical_element")

    @optical_element.setter
    def optical_element(self, value: WfiOpticalElement) -> None:
        self._set_node("optical_element", self._coerce(WfiOpticalElement, value, "optical_element"))

    @property
    def program(self) -> Program:
        return self._coerce(Program, self._get_node("program", coerce=False), "program")

    @program.setter
    def program(self, value: Program) -> None:
        self._set_node("program", self._coerce(Program, value, "program"))

    @property
    def visit(self) -> Visit:
        return self._coerce(Visit, self._get_node("visit", coerce=False), "visit")

    @visit.setter
    def visit(self, value: Visit) -> None:
        self._set_node("visit", self._coerce(Visit, value, "visit"))


class SegmentationMap(_core.DataModelNode):
    """
    Segmentation map computed by the Source Catalog Step
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/segmentation_map-1.0.0"

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
    def meta(self) -> SegmentationMap_Meta:
        return self._get_node("meta", SegmentationMap_Meta)

    @property
    def data(self) -> np.ndarray:
        return self._get_node("data", np.zeros(self.array_shape, dtype=np.uint32))
