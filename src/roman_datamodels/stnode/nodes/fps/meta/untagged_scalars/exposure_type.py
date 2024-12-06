from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["FpsExposureType"]


class FpsExposureTypeMixin(str, _core.SchemaScalarNode, _core.EnumNodeMixin):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/exposure_type-1.0.0"


class FpsExposureType(FpsExposureTypeMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Exposure type
    """

    WFI_IMAGE = "WFI_IMAGE"
    WFI_GRISM = "WFI_GRISM"
    WFI_PRISM = "WFI_PRISM"
    WFI_DARK = "WFI_DARK"
    WFI_FLAT = "WFI_FLAT"
    WFI_WFSC = "WFI_WFSC"
