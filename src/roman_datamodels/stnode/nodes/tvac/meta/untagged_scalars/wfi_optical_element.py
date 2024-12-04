from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["TvacWfiOpticalElement"]


class TvacWfiOpticalElement(str, _core.SchemaScalarNode):
    """
    WFI Optical Element
    """

    @classmethod
    def F062(cls) -> TvacWfiOpticalElement:
        return cls("F062")

    @classmethod
    def F087(cls) -> TvacWfiOpticalElement:
        return cls("F087")

    @classmethod
    def F106(cls) -> TvacWfiOpticalElement:
        return cls("F106")

    @classmethod
    def F129(cls) -> TvacWfiOpticalElement:
        return cls("F129")

    @classmethod
    def F146(cls) -> TvacWfiOpticalElement:
        return cls("F146")

    @classmethod
    def F158(cls) -> TvacWfiOpticalElement:
        return cls("F158")

    @classmethod
    def F184(cls) -> TvacWfiOpticalElement:
        return cls("F184")

    @classmethod
    def F213(cls) -> TvacWfiOpticalElement:
        return cls("F213")

    @classmethod
    def GRISM(cls) -> TvacWfiOpticalElement:
        return cls("GRISM")

    @classmethod
    def PRISM(cls) -> TvacWfiOpticalElement:
        return cls("PRISM")

    @classmethod
    def DARK(cls) -> TvacWfiOpticalElement:
        return cls("DARK")

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/wfi_optical_element-1.0.0"
