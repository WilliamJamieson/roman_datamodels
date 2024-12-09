from astropy.time import Time

from roman_datamodels.stnode import _default, core, rad

from ...enums import (
    VisitEngineeringQualityEntry,
    VisitPointingEngineeringSourceEntry,
    VisitStatusEntry,
    VisitTypeEntry,
)

__all__ = ["Visit"]


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
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/visit-1.0.0"

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
        return self._get_node("nexposures", lambda: _default.NOINT)

    @rad.field
    def internal_target(self) -> bool:
        return self._get_node("internal_target", lambda: False)
