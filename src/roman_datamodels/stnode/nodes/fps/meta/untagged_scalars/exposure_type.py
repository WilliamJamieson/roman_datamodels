from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["FpsExposureType"]


class FpsExposureType(str, _core.SchemaScalarNode):
    """
    Exposure type
    """

    @classmethod
    def WFI_IMAGE(cls) -> FpsExposureType:
        return cls("WFI_IMAGE")

    @classmethod
    def WFI_GRISM(cls) -> FpsExposureType:
        return cls("WFI_GRISM")

    @classmethod
    def WFI_PRISM(cls) -> FpsExposureType:
        return cls("WFI_PRISM")

    @classmethod
    def WFI_DARK(cls) -> FpsExposureType:
        return cls("WFI_DARK")

    @classmethod
    def WFI_FLAT(cls) -> FpsExposureType:
        return cls("WFI_FLAT")

    @classmethod
    def WFI_WFSC(cls) -> FpsExposureType:
        return cls("WFI_WFSC")

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/exposure_type-1.0.0"
