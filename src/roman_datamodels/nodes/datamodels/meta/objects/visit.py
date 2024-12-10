from enum import Enum
from types import MappingProxyType

from astropy.time import Time

from roman_datamodels.stnode import core, rad

__all__ = [
    "Visit",
    "VisitEngineeringQualityEntry",
    "VisitPointingEngineeringSourceEntry",
    "VisitStatusEntry",
    "VisitTypeEntry",
]


class VisitEngineeringQualityEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "engineering_quality"


class VisitEngineeringQualityEntry(VisitEngineeringQualityEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for quality in visit engineering
    """

    OK = "OK"
    SUSPECT = "SUSPECT"


class VisitPointingEngineeringSourceEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "pointing_engineering_source"


class VisitPointingEngineeringSourceEntry(VisitPointingEngineeringSourceEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for source in visit pointing engineering
    """

    CALCULATED = "CALCULATED"
    PLANNED = "PLANNED"


class VisitTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "type"


class VisitTypeEntry(VisitTypeEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for type in visit
    """

    GENERAL_ENGINEERING = "GENERAL_ENGINEERING"
    GENERIC = "GENERIC"
    PARALLEL = "PARALLEL"
    PRIME_TARGETED_FIXED = "PRIME_TARGETED_FIXED"
    PRIME_UNTARGETED = "PRIME_UNTARGETED"


class VisitStatusEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "status"


class VisitStatusEntry(VisitStatusEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for status in visit
    """

    DATALOSS = "DATALOSS"
    SUCCESSFUL = "SUCCESSFUL"
    UNSUCCESSFUL = "UNSUCCESSFUL"


class Visit_Dither(rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Visit

    @rad.field
    def primary_name(self) -> str | None:
        return self._get_node("primary_name", lambda: "None")

    @rad.field
    def subpixel_name(self) -> str | None:
        return self._get_node("subpixel_name", lambda: "None")

    @rad.field
    def executed_pattern(self) -> core.LNode[float] | None:
        return self._get_node("executed_pattern", lambda: core.LNode([float(v) for v in range(1, 10)]))


class Visit(rad.TaggedObjectNode):
    """
    Visit information
    """

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

    @rad.field
    def dither(self) -> Visit_Dither:
        return self._get_node("dither", Visit_Dither)

    @rad.field
    def engineering_quality(self) -> VisitEngineeringQualityEntry:
        return self._get_node("engineering_quality", lambda: VisitEngineeringQualityEntry.OK)

    @rad.field
    def pointing_engineering_source(self) -> VisitPointingEngineeringSourceEntry:
        return self._get_node("pointing_engineering_source", lambda: VisitPointingEngineeringSourceEntry.CALCULATED)

    @rad.field
    def type(self) -> VisitTypeEntry:
        return self._get_node("type", lambda: VisitTypeEntry.PRIME_TARGETED_FIXED)

    @rad.field
    def start_time(self) -> Time:
        return self._get_node("start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def end_time(self) -> Time:
        return self._get_node("end_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def status(self) -> VisitStatusEntry:
        return self._get_node("status", lambda: VisitStatusEntry.UNSUCCESSFUL)

    @rad.field
    def nexposures(self) -> int:
        return self._get_node("nexposures", lambda: rad.NOINT)

    @rad.field
    def internal_target(self) -> bool:
        return self._get_node("internal_target", lambda: False)
