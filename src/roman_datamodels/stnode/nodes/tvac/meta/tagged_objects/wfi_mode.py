from roman_datamodels.stnode import _core

from ....enums import InstrumentNameEntry
from ..untagged_scalars import (
    TvacWfiDetector,
    TvacWfiOpticalElement,
)

__all__ = ["TvacWfiMode"]


class TvacWfiMode(_core.TaggedObjectNode):
    """
    Tvac Roman WFI Instrument
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/wfi_mode-1.0.0"

    @_core.rad_field
    def name(self) -> InstrumentNameEntry:
        return self._get_node("name", lambda: InstrumentNameEntry.WFI)

    @_core.rad_field
    def detector(self) -> TvacWfiDetector:
        return self._get_node("detector", lambda: TvacWfiDetector.WFI01)

    @_core.rad_field
    def optical_element(self) -> TvacWfiOpticalElement:
        return self._get_node("optical_element", lambda: TvacWfiOpticalElement.F158)
