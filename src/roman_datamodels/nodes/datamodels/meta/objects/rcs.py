from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

__all__ = [
    "Rcs",
    "RcsBankEntry",
    "RcsBankEntryMixin",
    "RcsElectronicsEntry",
    "RcsElectronicsEntryMixin",
    "RcsLedEntry",
    "RcsLedEntryMixin",
]


class RcsElectronicsEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Rcs

    @classmethod
    def asdf_property_name(cls) -> str:
        return "electronics"


class RcsElectronicsEntry(RcsElectronicsEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
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


class RcsBankEntry(RcsBankEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
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


class RcsLedEntry(RcsLedEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
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


_Rcs: TypeAlias = RcsElectronicsEntry | RcsBankEntry | RcsLedEntry | int | bool | None


class Rcs(rad.TaggedObjectNode[_Rcs]):
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
        return False

    @rad.field
    def electronics(self) -> RcsElectronicsEntry | None:
        return RcsElectronicsEntry.A

    @rad.field
    def bank(self) -> RcsBankEntry | None:
        return RcsBankEntry.ONE

    @rad.field
    def led(self) -> RcsLedEntry | None:
        return RcsLedEntry.ONE

    @rad.field
    def counts(self) -> int:
        return rad.NOINT
