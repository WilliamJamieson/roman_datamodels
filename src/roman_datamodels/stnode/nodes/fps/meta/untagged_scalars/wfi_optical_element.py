from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["FpsWfiOpticalElement"]


class FpsWfiOpticalElement(str, _core.SchemaScalarNode):
    """
    WFI Optical Element
    """

    @classmethod
    def F062(cls) -> FpsWfiOpticalElement:
        return cls("F062")

    @classmethod
    def F087(cls) -> FpsWfiOpticalElement:
        return cls("F087")

    @classmethod
    def F106(cls) -> FpsWfiOpticalElement:
        return cls("F106")

    @classmethod
    def F129(cls) -> FpsWfiOpticalElement:
        return cls("F129")

    @classmethod
    def F146(cls) -> FpsWfiOpticalElement:
        return cls("F146")

    @classmethod
    def F158(cls) -> FpsWfiOpticalElement:
        return cls("F158")

    @classmethod
    def F184(cls) -> FpsWfiOpticalElement:
        return cls("F184")

    @classmethod
    def F213(cls) -> FpsWfiOpticalElement:
        return cls("F213")

    @classmethod
    def GRISM(cls) -> FpsWfiOpticalElement:
        return cls("GRISM")

    @classmethod
    def PRISM(cls) -> FpsWfiOpticalElement:
        return cls("PRISM")

    @classmethod
    def DARK(cls) -> FpsWfiOpticalElement:
        return cls("DARK")

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/wfi_optical_element-1.0.0"
