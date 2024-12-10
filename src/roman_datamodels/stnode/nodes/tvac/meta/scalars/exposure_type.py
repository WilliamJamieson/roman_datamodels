from __future__ import annotations

from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["TvacExposureType"]


class TvacExposureTypeMixin(str, rad.SchemaScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/exposure_type-1.0.0"


class TvacExposureType(TvacExposureTypeMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Exposure type
    """

    WFI_IMAGE = "WFI_IMAGE"
    WFI_GRISM = "WFI_GRISM"
    WFI_PRISM = "WFI_PRISM"
    WFI_DARK = "WFI_DARK"
    WFI_FLAT = "WFI_FLAT"
    WFI_WFSC = "WFI_WFSC"
