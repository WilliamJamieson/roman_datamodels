from roman_datamodels.stnode import _core

from ..untagged_scalars import (
    FpsWfiDetector,
    FpsWfiOpticalElement,
)

__all__ = ["FpsWfiMode"]


class FpsWfiMode(_core.TaggedObjectNode):
    """
    FPS Roman WFI Instrument
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/wfi_mode-1.0.0"

    @_core.rad_field
    def name(self) -> str:
        return self._get_node("name", lambda: "WFI")

    @_core.rad_field
    def detector(self) -> FpsWfiDetector:
        return self._get_node("detector", FpsWfiDetector.WFI01)

    @_core.rad_field
    def optical_element(self) -> FpsWfiOpticalElement:
        return self._get_node("optical_element", FpsWfiOpticalElement.F158)
