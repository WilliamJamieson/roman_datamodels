from roman_datamodels.stnode import _core

from ..untagged_scalars import (
    TvacWfiDetector,
    TvacWfiOpticalElement,
)

__all__ = ["TvacWfiMode"]


class TvacWfiMode(_core.TaggedObjectNode):
    """
    Tvac Roman WFI Instrument
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/wfi_mode-1.0.0"

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
    def detector(self) -> TvacWfiDetector:
        return self._get_node("detector", TvacWfiDetector.WFI01)

    @property
    def optical_element(self) -> TvacWfiOpticalElement:
        return self._get_node("optical_element", TvacWfiOpticalElement.F158)
