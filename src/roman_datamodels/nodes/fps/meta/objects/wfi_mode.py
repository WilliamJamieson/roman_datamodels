from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

from ....datamodels import InstrumentNameEntry
from ..scalars import (
    FpsWfiDetector,
    FpsWfiOpticalElement,
)

__all__ = ["FpsWfiMode"]


_FpsWfiMode: TypeAlias = InstrumentNameEntry | FpsWfiDetector | FpsWfiOpticalElement


class FpsWfiMode(rad.TaggedObjectNode[_FpsWfiMode]):
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

    @property
    @rad.field
    def name(self: rad.Node) -> InstrumentNameEntry:
        return InstrumentNameEntry.WFI

    @property
    @rad.field
    def detector(self: rad.Node) -> FpsWfiDetector:
        return FpsWfiDetector.WFI01

    @property
    @rad.field
    def optical_element(self: rad.Node) -> FpsWfiOpticalElement:
        return FpsWfiOpticalElement.F158
