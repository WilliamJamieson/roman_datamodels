from typing import Any, TypeAlias, TypeVar

from roman_datamodels.stnode import core, rad

from .basic import TvacBasic, _TvacBasic
from .objects import (
    TvacCalStep,
    TvacExposure,
    TvacGuidestar,
    TvacRefFile,
    TvacStatistics,
    TvacWfiMode,
)

__all__ = ["TvacCommon"]

_T = TypeVar("_T")


class TvacCommonMixin(rad.ExtraFieldsMixin[TvacStatistics | _T]):
    """Mixin things present in the constructors not present in the schema"""

    @rad.field
    def statistics(self) -> TvacStatistics:
        return TvacStatistics()

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("statistics",)


_TvacCommon: TypeAlias = _TvacBasic | TvacCalStep | TvacExposure | TvacGuidestar | TvacRefFile | TvacWfiMode | TvacStatistics


class TvacCommon(TvacCommonMixin[_TvacCommon | _T], TvacBasic[_TvacCommon | _T]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/common-1.0.0",)

    @rad.field
    def cal_step(self) -> TvacCalStep:
        return TvacCalStep()

    @rad.field
    def exposure(self) -> TvacExposure:
        return TvacExposure()

    @rad.field
    def guidestar(self) -> TvacGuidestar:
        return TvacGuidestar()

    @rad.field
    def instrument(self) -> TvacWfiMode:
        return TvacWfiMode()

    @rad.field
    def ref_file(self) -> TvacRefFile:
        return TvacRefFile()

    @rad.field
    def hdf5_meta(self) -> core.DNode[Any]:
        return core.DNode({"test": rad.NOSTR})

    @rad.field
    def hdf5_telemetry(self) -> str:
        return rad.NOSTR

    @rad.field
    def gw_meta(self) -> core.DNode[Any]:
        return core.DNode({"test": rad.NOSTR})
