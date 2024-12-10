from enum import Enum

from roman_datamodels.stnode import rad

__all__ = [
    "Ephemeris",
    "EphemerisTypeEntry",
]


class EphemerisTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
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


class Ephemeris(rad.TaggedObjectNode):
    """
    Ephemeris information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/ephemeris-1.0.0"

    @rad.field
    def earth_angle(self) -> float:
        return self._get_node("earth_angle", lambda: rad.NONUM)

    @rad.field
    def moon_angle(self) -> float:
        return self._get_node("moon_angle", lambda: rad.NONUM)

    @rad.field
    def sun_angle(self) -> float:
        return self._get_node("sun_angle", lambda: rad.NONUM)

    @rad.field
    def ephemeris_reference_frame(self) -> str:
        return self._get_node("ephemeris_reference_frame", lambda: rad.NOSTR)

    @rad.field
    def type(self) -> EphemerisTypeEntry:
        return self._get_node("type", lambda: EphemerisTypeEntry.DEFINITIVE)

    @rad.field
    def time(self) -> float:
        return self._get_node("time", lambda: rad.NONUM)

    @rad.field
    def spatial_x(self) -> float:
        return self._get_node("spatial_x", lambda: rad.NONUM)

    @rad.field
    def spatial_y(self) -> float:
        return self._get_node("spatial_y", lambda: rad.NONUM)

    @rad.field
    def spatial_z(self) -> float:
        return self._get_node("spatial_z", lambda: rad.NONUM)

    @rad.field
    def velocity_x(self) -> float:
        return self._get_node("velocity_x", lambda: rad.NONUM)

    @rad.field
    def velocity_y(self) -> float:
        return self._get_node("velocity_y", lambda: rad.NONUM)

    @rad.field
    def velocity_z(self) -> float:
        return self._get_node("velocity_z", lambda: rad.NONUM)
