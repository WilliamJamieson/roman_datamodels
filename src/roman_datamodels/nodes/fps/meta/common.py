from typing import Any, TypeAlias, TypeVar

from roman_datamodels.stnode import core, rad

from .basic import FpsBasic, _FpsBasic
from .objects import (
    FpsCalStep,
    FpsExposure,
    FpsGuidestar,
    FpsRefFile,
    FpsStatistics,
    FpsWfiMode,
)

__all__ = ["FpsCommon"]

_T = TypeVar("_T")


class FpsCommonMixin(rad.ExtraFieldsMixin[FpsStatistics | _T]):
    """Mixin things present in the constructors not present in the schema"""

    @rad.field
    def statistics(self) -> FpsStatistics:
        return FpsStatistics()

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("statistics",)


_FpsCommon: TypeAlias = _FpsBasic | FpsCalStep | FpsExposure | FpsGuidestar | FpsRefFile | FpsWfiMode | FpsStatistics


class FpsCommon(FpsCommonMixin[_FpsCommon | _T], FpsBasic[_FpsCommon | _T]):
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
    def hdf5_meta(self) -> core.DNode[Any]:
        return core.DNode({"test": rad.NOSTR})

    @rad.field
    def hdf5_telemetry(self) -> str:
        return rad.NOSTR

    @rad.field
    def gw_meta(self) -> core.DNode[Any]:
        return core.DNode({"test": rad.NOSTR})
