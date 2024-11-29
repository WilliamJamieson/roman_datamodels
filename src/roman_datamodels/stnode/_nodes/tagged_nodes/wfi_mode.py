"""
This module as been automatically generated, do not edit by hand.
"""

from roman_datamodels.stnode import _core, _mixins
from roman_datamodels.stnode._nodes.untagged_scalars import WfiDetector, WfiOpticalElement

__all__ = ["WfiMode"]


class WfiMode(_mixins.WfiModeMixin, _core.TaggedNode):
    """
    Roman WFI Instrument
    """

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
        if not self._has_node("name"):
            self.name = "WFI"
        return self._get_node("name")

    @property
    def detector(self) -> WfiDetector:
        if not self._has_node("detector"):
            self.detector = WfiDetector.WFI01()
        return self._get_node("detector")

    @property
    def optical_element(self) -> WfiOpticalElement:
        if not self._has_node("optical_element"):
            self.optical_element = WfiOpticalElement.F158()
        return self._get_node("optical_element")
