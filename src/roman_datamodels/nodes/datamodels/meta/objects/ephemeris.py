from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = [
    "Ephemeris",
    "EphemerisTypeEntry",
    "EphemerisTypeEntryMixin",
]


class EphemerisTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
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


class Ephemeris(rad.TaggedObjectNode):
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

    @rad.field
    def earth_angle(self) -> float:
        return rad.NONUM

    @rad.field
    def moon_angle(self) -> float:
        return rad.NONUM

    @rad.field
    def sun_angle(self) -> float:
        return rad.NONUM

    @rad.field
    def ephemeris_reference_frame(self) -> str:
        return rad.NOSTR

    @rad.field
    def type(self) -> EphemerisTypeEntry:
        return EphemerisTypeEntry.DEFINITIVE

    @rad.field
    def time(self) -> float:
        return rad.NONUM

    @rad.field
    def spatial_x(self) -> float:
        return rad.NONUM

    @rad.field
    def spatial_y(self) -> float:
        return rad.NONUM

    @rad.field
    def spatial_z(self) -> float:
        return rad.NONUM

    @rad.field
    def velocity_x(self) -> float:
        return rad.NONUM

    @rad.field
    def velocity_y(self) -> float:
        return rad.NONUM

    @rad.field
    def velocity_z(self) -> float:
        return rad.NONUM
