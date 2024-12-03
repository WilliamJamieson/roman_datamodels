from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["TvacExposureType"]


class TvacExposureType(str, _core.SchemaScalarNode):
    """
    Exposure type
    """

    @classmethod
    def WFI_IMAGE(cls) -> TvacExposureType:
        return cls("WFI_IMAGE")

    @classmethod
    def WFI_GRISM(cls) -> TvacExposureType:
        return cls("WFI_GRISM")

    @classmethod
    def WFI_PRISM(cls) -> TvacExposureType:
        return cls("WFI_PRISM")

    @classmethod
    def WFI_DARK(cls) -> TvacExposureType:
        return cls("WFI_DARK")

    @classmethod
    def WFI_FLAT(cls) -> TvacExposureType:
        return cls("WFI_FLAT")

    @classmethod
    def WFI_WFSC(cls) -> TvacExposureType:
        return cls("WFI_WFSC")

    @property
    def schema_uri(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/exposure_type-1.0.0"
