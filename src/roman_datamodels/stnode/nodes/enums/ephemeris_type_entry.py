from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["EphemerisTypeEntry"]


class EphemerisTypeEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Ephemeris

        return Ephemeris

    @classmethod
    def asdf_property_name(cls) -> str:
        return "type"


class EphemerisTypeEntry(EphemerisTypeEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible entries for type in ephemeris
    """

    DEFINITIVE = "DEFINITIVE"
    PREDICTED = "PREDICTED"
