from enum import Enum
from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = [
    "Rcs",
    "RcsBankEntry",
    "RcsElectronicsEntry",
    "RcsLedEntry",
]


class RcsElectronicsEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Rcs

    @classmethod
    def asdf_property_name(cls) -> str:
        return "electronics"


class RcsElectronicsEntry(RcsElectronicsEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible electronics in rcs
    """

    A = "A"
    B = "B"
    NONE = "None"


class RcsBankEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Rcs

    @classmethod
    def asdf_property_name(cls) -> str:
        return "bank"


class RcsBankEntry(RcsBankEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible banks in rcs
    """

    ONE = "1"
    TWO = "2"
    NONE = "None"


class RcsLedEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Rcs

    @classmethod
    def asdf_property_name(cls) -> str:
        return "led"


class RcsLedEntry(RcsLedEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible leds in rcs
    """

    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    NONE = "None"


class Rcs(rad.TaggedObjectNode):
    """
    Relative Calibration System Information
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/rcs-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {"asdf://stsci.edu/datamodels/roman/tags/rcs-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/rcs-1.0.0"}
        )

    @rad.field
    def active(self) -> bool:
        return self._get_node("active", lambda: False)

    @rad.field
    def electronics(self) -> RcsElectronicsEntry | None:
        return self._get_node("electronics", lambda: RcsElectronicsEntry.A)

    @rad.field
    def bank(self) -> RcsBankEntry | None:
        return self._get_node("bank", lambda: RcsBankEntry.ONE)

    @rad.field
    def led(self) -> RcsLedEntry | None:
        return self._get_node("led", lambda: RcsLedEntry.ONE)

    @rad.field
    def counts(self) -> int:
        return self._get_node("counts", lambda: rad.NOINT)
