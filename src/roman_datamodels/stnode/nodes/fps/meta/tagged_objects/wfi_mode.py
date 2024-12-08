from roman_datamodels.stnode import rad

from ....enums import InstrumentNameEntry
from ..untagged_scalars import (
    FpsWfiDetector,
    FpsWfiOpticalElement,
)

__all__ = ["FpsWfiMode"]


class FpsWfiMode(rad.TaggedObjectNode):
    """
    FPS Roman WFI Instrument
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/wfi_mode-1.0.0"

    @rad.rad_field
    def name(self) -> InstrumentNameEntry:
        return self._get_node("name", lambda: InstrumentNameEntry.WFI)

    @rad.rad_field
    def detector(self) -> FpsWfiDetector:
        return self._get_node("detector", lambda: FpsWfiDetector.WFI01)

    @rad.rad_field
    def optical_element(self) -> FpsWfiOpticalElement:
        return self._get_node("optical_element", lambda: FpsWfiOpticalElement.F158)
