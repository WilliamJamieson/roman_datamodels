from enum import Enum

from roman_datamodels.stnode import _core

__all__ = [
    "WcsinfoApertureNameEntry",
    "WcsinfoMosaicProjectionEntry",
    "WcsinfoVparityEntry",
]


class WcsinfoApertureNameEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Wcsinfo

        return Wcsinfo

    @classmethod
    def asdf_property_name(cls) -> str:
        return "aperture_name"


class WcsinfoApertureNameEntry(WcsinfoApertureNameEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
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


class WcsinfoVparityEntryMixin(int, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Wcsinfo

        return Wcsinfo

    @classmethod
    def asdf_property_name(cls) -> str:
        return "vparity"


class WcsinfoVparityEntry(WcsinfoVparityEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible entries for vparity in wcsinfo
    """

    REVERSED = -1
    NORMAL = 1


class WcsinfoMosaicProjectionEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import MosaicWcsinfo

        return MosaicWcsinfo

    @classmethod
    def asdf_property_name(cls) -> str:
        return "projection"


class WcsinfoMosaicProjectionEntry(WcsinfoMosaicProjectionEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible entries for projection in wcsinfo
    """

    TAN = "TAN"
