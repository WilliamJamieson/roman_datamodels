from roman_datamodels.stnode import _base, _core, _default

from .basic import TvacBasic
from .tagged_objects import (
    TvacCalStep,
    TvacExposure,
    TvacGuidestar,
    TvacRefFile,
    TvacStatistics,
    TvacWfiMode,
)

__all__ = ["TvacCommon"]


class TvacCommonMixin(_base.AdditionalNodeMixin):
    """Mixin things present in the constructors not present in the schema"""

    @_core.rad_field
    def statistics(self) -> TvacStatistics:
        return self._get_node("statistics", TvacStatistics)

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("statistics",)


class TvacCommon(TvacCommonMixin, TvacBasic):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/common-1.0.0"

    @_core.rad_field
    def cal_step(self) -> TvacCalStep:
        return self._get_node("cal_step", TvacCalStep)

    @_core.rad_field
    def exposure(self) -> TvacExposure:
        return self._get_node("exposure", TvacExposure)

    @_core.rad_field
    def guidestar(self) -> TvacGuidestar:
        return self._get_node("guidestar", TvacGuidestar)

    @_core.rad_field
    def instrument(self) -> TvacWfiMode:
        return self._get_node("instrument", TvacWfiMode)

    @_core.rad_field
    def ref_file(self) -> TvacRefFile:
        return self._get_node("ref_file", TvacRefFile)

    @_core.rad_field
    def hdf5_meta(self) -> _base.DNode:
        return self._get_node("hdf5_meta", lambda: _base.DNode({"test": _default.NOSTR}))

    @_core.rad_field
    def hdf5_telemetry(self) -> str:
        return self._get_node("hdf5_telemetry", lambda: _default.NOSTR)

    @_core.rad_field
    def gw_meta(self) -> _base.DNode:
        return self._get_node("gw_meta", lambda: _base.DNode({"test": _default.NOSTR}))
