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

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/wfi_mode-1.0.0"

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
    def detector(self) -> FpsWfiDetector:
        return self._get_node("detector", FpsWfiDetector.WFI01)

    @property
    def optical_element(self) -> FpsWfiOpticalElement:
        return self._get_node("optical_element", FpsWfiOpticalElement.F158)
