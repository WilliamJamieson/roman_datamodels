from roman_datamodels.stnode import _core

from ....enums import InstrumentNameEntry
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
    def name(self) -> InstrumentNameEntry:
        return self._get_node("name", lambda: InstrumentNameEntry.WFI)

    @_core.rad_field
    def detector(self) -> FpsWfiDetector:
        return self._get_node("detector", lambda: FpsWfiDetector.WFI01)

    @_core.rad_field
    def optical_element(self) -> FpsWfiOpticalElement:
        return self._get_node("optical_element", lambda: FpsWfiOpticalElement.F158)
