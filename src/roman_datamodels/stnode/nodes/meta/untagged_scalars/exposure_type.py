from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["ExposureType"]


class ExposureType(str, _core.SchemaScalarNode):
    """
    Exposure type
    """

    @classmethod
    def WFI_IMAGE(cls) -> ExposureType:
        return cls("WFI_IMAGE")

    @classmethod
    def WFI_GRISM(cls) -> ExposureType:
        return cls("WFI_GRISM")

    @classmethod
    def WFI_PRISM(cls) -> ExposureType:
        return cls("WFI_PRISM")

    @classmethod
    def WFI_DARK(cls) -> ExposureType:
        return cls("WFI_DARK")

    @classmethod
    def WFI_FLAT(cls) -> ExposureType:
        return cls("WFI_FLAT")

    @classmethod
    def WFI_WFSC(cls) -> ExposureType:
        return cls("WFI_WFSC")

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/exposure_type-1.0.0"
