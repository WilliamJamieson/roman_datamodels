from roman_datamodels.stnode import core, rad

from .basic import FpsBasic
from .tagged_objects import (
    FpsCalStep,
    FpsExposure,
    FpsGuidestar,
    FpsRefFile,
    FpsStatistics,
    FpsWfiMode,
)

__all__ = ["FpsCommon"]


class FpsCommonMixin(core.AdditionalNodeMixin):
    """Mixin things present in the constructors not present in the schema"""

    @rad.field
    def statistics(self) -> FpsStatistics:
        return self._get_node("statistics", FpsStatistics)

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("statistics",)


class FpsCommon(FpsCommonMixin, FpsBasic):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/common-1.0.0"

    @rad.field
    def cal_step(self) -> FpsCalStep:
        return self._get_node("cal_step", FpsCalStep)

    @rad.field
    def exposure(self) -> FpsExposure:
        return self._get_node("exposure", FpsExposure)

    @rad.field
    def guidestar(self) -> FpsGuidestar:
        return self._get_node("guidestar", FpsGuidestar)

    @rad.field
    def instrument(self) -> FpsWfiMode:
        return self._get_node("instrument", FpsWfiMode)

    @rad.field
    def ref_file(self) -> FpsRefFile:
        return self._get_node("ref_file", FpsRefFile)

    @rad.field
    def hdf5_meta(self) -> core.DNode:
        return self._get_node("hdf5_meta", lambda: core.DNode({"test": rad.NOSTR}))

    @rad.field
    def hdf5_telemetry(self) -> str:
        return self._get_node("hdf5_telemetry", lambda: rad.NOSTR)

    @rad.field
    def gw_meta(self) -> core.DNode:
        return self._get_node("gw_meta", lambda: core.DNode({"test": rad.NOSTR}))
