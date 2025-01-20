from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

__all__ = [
    "Ephemeris",
    "EphemerisTypeEntry",
]


class EphemerisTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return Ephemeris

    @classmethod
    def asdf_property_name(cls) -> str:
        return "type"


class EphemerisTypeEntry(EphemerisTypeEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for type in ephemeris
    """

    DEFINITIVE = "DEFINITIVE"
    PREDICTED = "PREDICTED"


_Ephemeris: TypeAlias = EphemerisTypeEntry | float | str


class Ephemeris(rad.TaggedObjectNode[_Ephemeris]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/ephemeris-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/ephemeris-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/ephemeris-1.0.0"
            }
        )

    @property
    @rad.field
    def earth_angle(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def moon_angle(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def sun_angle(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def ephemeris_reference_frame(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def type(self: rad.Node) -> EphemerisTypeEntry:
        return EphemerisTypeEntry.DEFINITIVE

    @property
    @rad.field
    def time(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def spatial_x(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def spatial_y(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def spatial_z(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def velocity_x(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def velocity_y(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def velocity_z(self: rad.Node) -> float:
        return rad.NONUM
