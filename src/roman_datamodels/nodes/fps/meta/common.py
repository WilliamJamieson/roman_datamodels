from roman_datamodels.stnode import core, rad

from .basic import FpsBasic
from .objects import (
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
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/common-1.0.0",)

    @rad.field
    def cal_step(self) -> FpsCalStep:
        return FpsCalStep()

    @rad.field
    def exposure(self) -> FpsExposure:
        return FpsExposure()

    @rad.field
    def guidestar(self) -> FpsGuidestar:
        return FpsGuidestar()

    @rad.field
    def instrument(self) -> FpsWfiMode:
        return FpsWfiMode()

    @rad.field
    def ref_file(self) -> FpsRefFile:
        return FpsRefFile()

    @rad.field
    def hdf5_meta(self) -> core.DNode:
        return core.DNode({"test": rad.NOSTR})

    @rad.field
    def hdf5_telemetry(self) -> str:
        return rad.NOSTR

    @rad.field
    def gw_meta(self) -> core.DNode:
        return core.DNode({"test": rad.NOSTR})