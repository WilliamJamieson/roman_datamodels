from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["WfiOpticalElement"]


class WfiOpticalElement(str, _core.SchemaScalarNode):
    """
    WFI Optical Element
    """

    @classmethod
    def F062(cls) -> WfiOpticalElement:
        return cls("F062")

    @classmethod
    def F087(cls) -> WfiOpticalElement:
        return cls("F087")

    @classmethod
    def F106(cls) -> WfiOpticalElement:
        return cls("F106")

    @classmethod
    def F129(cls) -> WfiOpticalElement:
        return cls("F129")

    @classmethod
    def F146(cls) -> WfiOpticalElement:
        return cls("F146")

    @classmethod
    def F158(cls) -> WfiOpticalElement:
        return cls("F158")

    @classmethod
    def F184(cls) -> WfiOpticalElement:
        return cls("F184")

    @classmethod
    def F213(cls) -> WfiOpticalElement:
        return cls("F213")

    @classmethod
    def GRISM(cls) -> WfiOpticalElement:
        return cls("GRISM")

    @classmethod
    def PRISM(cls) -> WfiOpticalElement:
        return cls("PRISM")

    @classmethod
    def DARK(cls) -> WfiOpticalElement:
        return cls("DARK")

    @property
    def schema_uri(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/wfi_optical_element-1.0.0"
