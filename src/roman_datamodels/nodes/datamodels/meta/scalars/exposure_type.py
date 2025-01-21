from roman_datamodels.stnode import rad

__all__ = ["ExposureType"]


class ExposureTypeMixin(str, rad.SchemaScalarNode[str], rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/exposure_type-1.0.0",)


class ExposureType(ExposureTypeMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    WFI_IMAGE = "WFI_IMAGE"
    WFI_GRISM = "WFI_GRISM"
    WFI_PRISM = "WFI_PRISM"
    WFI_DARK = "WFI_DARK"
    WFI_FLAT = "WFI_FLAT"
    WFI_WFSC = "WFI_WFSC"
