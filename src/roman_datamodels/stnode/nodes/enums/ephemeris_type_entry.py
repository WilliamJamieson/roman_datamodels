from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["EphemerisTypeEntry"]


class EphemerisTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Ephemeris

        return Ephemeris

    @classmethod
    def asdf_property_name(cls) -> str:
        return "type"


class EphemerisTypeEntry(EphemerisTypeEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for type in ephemeris
    """

    DEFINITIVE = "DEFINITIVE"
    PREDICTED = "PREDICTED"
