from astropy.time import Time

from roman_datamodels.stnode import _base, _core, _default

__all__ = ["Visit"]


class Visit_Dither(_core.ImpliedNodeMixin, _core.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Visit

    @_core.rad_field
    def primary_name(self) -> str | None:
        return self._get_node("primary_name", lambda: "None")

    @_core.rad_field
    def subpixel_name(self) -> str | None:
        return self._get_node("subpixel_name", lambda: "None")

    @_core.rad_field
    def executed_pattern(self) -> _base.LNode[float] | None:
        return self._get_node("executed_pattern", lambda: _base.LNode([float(v) for v in range(1, 10)]))


class Visit(_core.TaggedObjectNode):
    """
    Visit information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/visit-1.0.0"

    @_core.rad_field
    def dither(self) -> Visit_Dither:
        return self._get_node("dither", Visit_Dither)

    @_core.rad_field
    def engineering_quality(self) -> str:
        return self._get_node("engineering_quality", lambda: "OK")

    @_core.rad_field
    def pointing_engineering_source(self) -> str:
        return self._get_node("pointing_engineering_source", lambda: "CALCULATED")

    @_core.rad_field
    def type(self) -> str:
        return self._get_node("type", lambda: "PRIME_TARGETED_FIXED")

    @_core.rad_field
    def start_time(self) -> Time:
        return self._get_node("start_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @_core.rad_field
    def end_time(self) -> Time:
        return self._get_node("end_time", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @_core.rad_field
    def status(self) -> str:
        return self._get_node("status", lambda: "UNSUCCESSFUL")

    @_core.rad_field
    def nexposures(self) -> int:
        return self._get_node("nexposures", lambda: _default.NOINT)

    @_core.rad_field
    def internal_target(self) -> bool:
        return self._get_node("internal_target", lambda: False)
