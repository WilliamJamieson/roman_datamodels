from types import MappingProxyType
from typing import TypeAlias

from astropy.time import Time

from roman_datamodels.stnode import core, rad

__all__ = [
    "Visit",
    "VisitEngineeringQualityEntry",
    "VisitPointingEngineeringSourceEntry",
    "VisitStatusEntry",
    "VisitTypeEntry",
]


class VisitEngineeringQualityEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "engineering_quality"


class VisitEngineeringQualityEntry(VisitEngineeringQualityEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for quality in visit engineering
    """

    OK = "OK"
    SUSPECT = "SUSPECT"


class VisitPointingEngineeringSourceEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "pointing_engineering_source"


class VisitPointingEngineeringSourceEntry(VisitPointingEngineeringSourceEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for source in visit pointing engineering
    """

    CALCULATED = "CALCULATED"
    PLANNED = "PLANNED"


class VisitTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "type"


class VisitTypeEntry(VisitTypeEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for type in visit
    """

    GENERAL_ENGINEERING = "GENERAL_ENGINEERING"
    GENERIC = "GENERIC"
    PARALLEL = "PARALLEL"
    PRIME_TARGETED_FIXED = "PRIME_TARGETED_FIXED"
    PRIME_UNTARGETED = "PRIME_UNTARGETED"


class VisitStatusEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "status"


class VisitStatusEntry(VisitStatusEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for status in visit
    """

    DATALOSS = "DATALOSS"
    SUCCESSFUL = "SUCCESSFUL"
    UNSUCCESSFUL = "UNSUCCESSFUL"


_Visit_Dither = core.LNode[float] | str | None


class Visit_Dither(rad.ImpliedNodeMixin[_Visit_Dither], rad.ObjectNode[_Visit_Dither]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Visit

    @property
    @rad.field
    def primary_name(self: rad.Node) -> str | None:
        return "None"

    @property
    @rad.field
    def subpixel_name(self: rad.Node) -> str | None:
        return "None"

    @property
    @rad.field
    def executed_pattern(self: rad.Node) -> core.LNode[float] | None:
        return core.LNode([float(v) for v in range(1, 10)])


_Visit: TypeAlias = (
    Visit_Dither
    | VisitEngineeringQualityEntry
    | VisitPointingEngineeringSourceEntry
    | VisitStatusEntry
    | VisitTypeEntry
    | Time
    | int
    | bool
)


class Visit(rad.TaggedObjectNode[_Visit]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/visit-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/visit-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/visit-1.0.0",
            }
        )

    @property
    @rad.field
    def dither(self: rad.Node) -> Visit_Dither:
        return Visit_Dither()

    @property
    @rad.field
    def engineering_quality(self: rad.Node) -> VisitEngineeringQualityEntry:
        return VisitEngineeringQualityEntry.OK

    @property
    @rad.field
    def pointing_engineering_source(self: rad.Node) -> VisitPointingEngineeringSourceEntry:
        return VisitPointingEngineeringSourceEntry.CALCULATED

    @property
    @rad.field
    def type(self: rad.Node) -> VisitTypeEntry:
        return VisitTypeEntry.PRIME_TARGETED_FIXED

    @property
    @rad.field
    def start_time(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def end_time(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def status(self: rad.Node) -> VisitStatusEntry:
        return VisitStatusEntry.UNSUCCESSFUL

    @property
    @rad.field
    def nexposures(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def internal_target(self: rad.Node) -> bool:
        return False
