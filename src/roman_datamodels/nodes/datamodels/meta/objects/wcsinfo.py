from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = [
    "Wcsinfo",
    "WcsinfoApertureNameEntry",
    "WcsinfoVparityEntry",
]


class WcsinfoApertureNameEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Wcsinfo

    @classmethod
    def asdf_property_name(cls) -> str:
        return "aperture_name"


class WcsinfoApertureNameEntry(WcsinfoApertureNameEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for aperture_name in wcsinfo
    """

    WFI01_FULL = "WFI01_FULL"
    WFI02_FULL = "WFI02_FULL"
    WFI03_FULL = "WFI03_FULL"
    WFI04_FULL = "WFI04_FULL"
    WFI05_FULL = "WFI05_FULL"
    WFI06_FULL = "WFI06_FULL"
    WFI07_FULL = "WFI07_FULL"
    WFI08_FULL = "WFI08_FULL"
    WFI09_FULL = "WFI09_FULL"
    WFI10_FULL = "WFI10_FULL"
    WFI11_FULL = "WFI11_FULL"
    WFI12_FULL = "WFI12_FULL"
    WFI13_FULL = "WFI13_FULL"
    WFI14_FULL = "WFI14_FULL"
    WFI15_FULL = "WFI15_FULL"
    WFI16_FULL = "WFI16_FULL"
    WFI17_FULL = "WFI17_FULL"
    WFI18_FULL = "WFI18_FULL"
    WFI_01_FULL = "WFI_01_FULL"
    WFI_02_FULL = "WFI_02_FULL"
    WFI_03_FULL = "WFI_03_FULL"
    WFI_04_FULL = "WFI_04_FULL"
    WFI_05_FULL = "WFI_05_FULL"
    WFI_06_FULL = "WFI_06_FULL"
    WFI_07_FULL = "WFI_07_FULL"
    WFI_08_FULL = "WFI_08_FULL"
    WFI_09_FULL = "WFI_09_FULL"
    WFI_10_FULL = "WFI_10_FULL"
    WFI_11_FULL = "WFI_11_FULL"
    WFI_12_FULL = "WFI_12_FULL"
    WFI_13_FULL = "WFI_13_FULL"
    WFI_14_FULL = "WFI_14_FULL"
    WFI_15_FULL = "WFI_15_FULL"
    WFI_16_FULL = "WFI_16_FULL"
    WFI_17_FULL = "WFI_17_FULL"
    WFI_18_FULL = "WFI_18_FULL"
    WFI_CEN = "WFI_CEN"
    BORESIGHT = "BORESIGHT"
    CGI_CEN = "CGI_CEN"


class WcsinfoVparityEntryMixin(int, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Wcsinfo

    @classmethod
    def asdf_property_name(cls) -> str:
        return "vparity"


class WcsinfoVparityEntry(WcsinfoVparityEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for vparity in wcsinfo
    """

    REVERSED = -1
    NORMAL = 1


class Wcsinfo(rad.TaggedObjectNode):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/wcsinfo-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/wcsinfo-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/wcsinfo-1.0.0",
            }
        )

    @rad.field
    def aperture_name(self) -> WcsinfoApertureNameEntry:
        return WcsinfoApertureNameEntry.WFI01_FULL

    @rad.field
    def pa_aperture(self) -> float:
        return rad.NONUM

    @rad.field
    def v2_ref(self) -> float:
        return rad.NONUM

    @rad.field
    def v3_ref(self) -> float:
        return rad.NONUM

    @rad.field
    def vparity(self) -> WcsinfoVparityEntry:
        return WcsinfoVparityEntry.REVERSED

    @rad.field
    def v3yangle(self) -> float:
        return rad.NONUM

    @rad.field
    def ra_ref(self) -> float:
        return rad.NONUM

    @rad.field
    def dec_ref(self) -> float:
        return rad.NONUM

    @rad.field
    def roll_ref(self) -> float:
        return rad.NONUM

    @rad.field
    def s_region(self) -> str:
        return rad.NOSTR
