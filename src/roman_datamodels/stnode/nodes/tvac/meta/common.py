from roman_datamodels.stnode import core, rad

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


class TvacCommonMixin(core.AdditionalNodeMixin):
    """Mixin things present in the constructors not present in the schema"""

    @rad.field
    def statistics(self) -> TvacStatistics:
        return self._get_node("statistics", TvacStatistics)

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("statistics",)


class TvacCommon(TvacCommonMixin, TvacBasic):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/common-1.0.0"

    @rad.field
    def cal_step(self) -> TvacCalStep:
        return self._get_node("cal_step", TvacCalStep)

    @rad.field
    def exposure(self) -> TvacExposure:
        return self._get_node("exposure", TvacExposure)

    @rad.field
    def guidestar(self) -> TvacGuidestar:
        return self._get_node("guidestar", TvacGuidestar)

    @rad.field
    def instrument(self) -> TvacWfiMode:
        return self._get_node("instrument", TvacWfiMode)

    @rad.field
    def ref_file(self) -> TvacRefFile:
        return self._get_node("ref_file", TvacRefFile)

    @rad.field
    def hdf5_meta(self) -> core.DNode:
        return self._get_node("hdf5_meta", lambda: core.DNode({"test": rad.NOSTR}))

    @rad.field
    def hdf5_telemetry(self) -> str:
        return self._get_node("hdf5_telemetry", lambda: rad.NOSTR)

    @rad.field
    def gw_meta(self) -> core.DNode:
        return self._get_node("gw_meta", lambda: core.DNode({"test": rad.NOSTR}))
