from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["RcsBankEntry", "RcsElectronicsEntry", "RcsLedEntry"]


class RcsElectronicsEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Rcs

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
        from ..meta import Rcs

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
        from ..meta import Rcs

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
