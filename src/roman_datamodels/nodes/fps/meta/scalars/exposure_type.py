from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["FpsExposureType"]


class FpsExposureTypeMixin(str, rad.SchemaScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/exposure_type-1.0.0",)


class FpsExposureType(FpsExposureTypeMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Exposure type
    """

    WFI_IMAGE = "WFI_IMAGE"
    WFI_GRISM = "WFI_GRISM"
    WFI_PRISM = "WFI_PRISM"
    WFI_DARK = "WFI_DARK"
    WFI_FLAT = "WFI_FLAT"
    WFI_WFSC = "WFI_WFSC"
