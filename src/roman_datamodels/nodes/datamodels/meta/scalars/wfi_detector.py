from roman_datamodels.stnode import rad

__all__ = ["WfiDetector"]


class WfiDetectorMixin(str, rad.SchemaScalarNode, rad.EnumNodeMixin):
    """
    WFI Detector
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/wfi_detector-1.0.0",)


class WfiDetector(WfiDetectorMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    WFI Detector
    """

    WFI01 = "WFI01"
    WFI02 = "WFI02"
    WFI03 = "WFI03"
    WFI04 = "WFI04"
    WFI05 = "WFI05"
    WFI06 = "WFI06"
    WFI07 = "WFI07"
    WFI08 = "WFI08"
    WFI09 = "WFI09"
    WFI10 = "WFI10"
    WFI11 = "WFI11"
    WFI12 = "WFI12"
    WFI13 = "WFI13"
    WFI14 = "WFI14"
    WFI15 = "WFI15"
    WFI16 = "WFI16"
    WFI17 = "WFI17"
    WFI18 = "WFI18"
