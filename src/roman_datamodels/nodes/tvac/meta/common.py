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


class TvacCommonMixin(core.AdditionalNodeMixin):
    """Mixin things present in the constructors not present in the schema"""

    @property
    @rad.field
    def statistics(self: rad.Node) -> TvacStatistics:  # type: ignore[misc]
        return TvacStatistics()

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("statistics",)


_TvacCommon: TypeAlias = _TvacBasic | TvacCalStep | TvacExposure | TvacGuidestar | TvacRefFile | TvacWfiMode | TvacStatistics


class TvacCommon(TvacCommonMixin, TvacBasic[_TvacCommon | _T]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/common-1.0.0",)

    @property
    @rad.field
    def cal_step(self: rad.Node) -> TvacCalStep:
        return TvacCalStep()

    @property
    @rad.field
    def exposure(self: rad.Node) -> TvacExposure:
        return TvacExposure()

    @property
    @rad.field
    def guidestar(self: rad.Node) -> TvacGuidestar:
        return TvacGuidestar()

    @property
    @rad.field
    def instrument(self: rad.Node) -> TvacWfiMode:
        return TvacWfiMode()

    @property
    @rad.field
    def ref_file(self: rad.Node) -> TvacRefFile:
        return TvacRefFile()

    @property
    @rad.field
    def hdf5_meta(self: rad.Node) -> core.DNode[Any]:
        return core.DNode({"test": rad.NOSTR})

    @property
    @rad.field
    def hdf5_telemetry(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def gw_meta(self: rad.Node) -> core.DNode[Any]:
        return core.DNode({"test": rad.NOSTR})
