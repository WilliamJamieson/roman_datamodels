from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["FpsWfiOpticalElement"]


class FpsWfiOpticalElementMixin(str, _core.SchemaScalarNode, _core.EnumNodeMixin):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/wfi_optical_element-1.0.0"


class FpsWfiOpticalElement(FpsWfiOpticalElementMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    WFI Optical Element
    """

    F062 = "F062"
    F087 = "F087"
    F106 = "F106"
    F129 = "F129"
    F146 = "F146"
    F158 = "F158"
    F184 = "F184"
    F213 = "F213"
    GRISM = "GRISM"
    PRISM = "PRISM"
    DARK = "DARK"
