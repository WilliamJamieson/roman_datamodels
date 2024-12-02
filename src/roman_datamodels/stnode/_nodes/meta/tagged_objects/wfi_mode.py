from __future__ import annotations

from typing import TYPE_CHECKING

from roman_datamodels.stnode import _core, _mixins

from ..untagged_scalars import WfiDetector, WfiOpticalElement

if TYPE_CHECKING:
    from typing import ClassVar

__all__ = ["WfiMode"]


class WfiMode(_mixins.WfiModeMixin, _core.TaggedObjectNode):
    """
    Roman WFI Instrument
    """

    # Every optical element is a grating or a filter
    #   There are less gratings than filters so its easier to list out the
    #   gratings.
    _GRATING_OPTICAL_ELEMENTS: ClassVar[tuple[str]] = ("GRISM", "PRISM")

    @property
    def filter(self) -> WfiOpticalElement:
        """
        Returns the filter if it is one, otherwise None
        """
        if self.optical_element in self._GRATING_OPTICAL_ELEMENTS:
            return None

        return self.optical_element

    @property
    def grating(self) -> WfiOpticalElement:
        """
        Returns the grating if it is one, otherwise None
        """
        if self.optical_element in self._GRATING_OPTICAL_ELEMENTS:
            return self.optical_element

        return None

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/wfi_mode-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "name",
            "detector",
            "optical_element",
        )

    @property
    def name(self) -> str:
        return self._get_node("name", lambda: "WFI")

    @property
    def detector(self) -> WfiDetector:
        return self._get_node("detector", WfiDetector.WFI01)

    @property
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", WfiOpticalElement.F158)
