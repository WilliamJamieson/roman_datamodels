from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

from ....datamodels import InstrumentNameEntry
from ..scalars import (
    TvacWfiDetector,
    TvacWfiOpticalElement,
)

__all__ = ["TvacWfiMode"]

_TvacWfiMode: TypeAlias = InstrumentNameEntry | TvacWfiDetector | TvacWfiOpticalElement


class TvacWfiMode(rad.TaggedObjectNode[_TvacWfiMode]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/wfi_mode-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/tvac/wfi_mode-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/wfi_mode-1.0.0"
            }
        )

    @property
    @rad.field
    def name(self: rad.Node) -> InstrumentNameEntry:
        return InstrumentNameEntry.WFI

    @property
    @rad.field
    def detector(self: rad.Node) -> TvacWfiDetector:
        return TvacWfiDetector.WFI01

    @property
    @rad.field
    def optical_element(self: rad.Node) -> TvacWfiOpticalElement:
        return TvacWfiOpticalElement.F158
