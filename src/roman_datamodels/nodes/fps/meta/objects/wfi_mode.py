from types import MappingProxyType

from roman_datamodels.stnode import rad

from ....datamodels import InstrumentNameEntry
from ..scalars import (
    FpsWfiDetector,
    FpsWfiOpticalElement,
)

__all__ = ["FpsWfiMode"]


class FpsWfiMode(rad.TaggedObjectNode):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/wfi_mode-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/fps/wfi_mode-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/fps/wfi_mode-1.0.0"
            }
        )

    @rad.field
    def name(self) -> InstrumentNameEntry:
        return InstrumentNameEntry.WFI

    @rad.field
    def detector(self) -> FpsWfiDetector:
        return FpsWfiDetector.WFI01

    @rad.field
    def optical_element(self) -> FpsWfiOpticalElement:
        return FpsWfiOpticalElement.F158
