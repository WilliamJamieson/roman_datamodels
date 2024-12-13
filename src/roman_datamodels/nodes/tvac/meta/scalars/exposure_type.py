from roman_datamodels.stnode import rad

__all__ = ["TvacExposureType"]


class TvacExposureTypeMixin(str, rad.SchemaScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/exposure_type-1.0.0",)


class TvacExposureType(TvacExposureTypeMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Exposure type
    """

    WFI_IMAGE = "WFI_IMAGE"
    WFI_GRISM = "WFI_GRISM"
    WFI_PRISM = "WFI_PRISM"
    WFI_DARK = "WFI_DARK"
    WFI_FLAT = "WFI_FLAT"
    WFI_WFSC = "WFI_WFSC"
