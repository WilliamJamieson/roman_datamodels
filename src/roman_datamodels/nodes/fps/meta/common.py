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


class FpsCommonMixin(core.AdditionalNodeMixin):
    """Mixin things present in the constructors not present in the schema"""

    @property
    @rad.field
    def statistics(self: rad.Node) -> FpsStatistics:  # type: ignore[misc]
        return FpsStatistics()

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("statistics",)


_FpsCommon: TypeAlias = _FpsBasic | FpsCalStep | FpsExposure | FpsGuidestar | FpsRefFile | FpsWfiMode | FpsStatistics


class FpsCommon(FpsCommonMixin, FpsBasic[_FpsCommon | _T]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/common-1.0.0",)

    @property
    @rad.field
    def cal_step(self: rad.Node) -> FpsCalStep:
        return FpsCalStep()

    @property
    @rad.field
    def exposure(self: rad.Node) -> FpsExposure:
        return FpsExposure()

    @property
    @rad.field
    def guidestar(self: rad.Node) -> FpsGuidestar:
        return FpsGuidestar()

    @property
    @rad.field
    def instrument(self: rad.Node) -> FpsWfiMode:
        return FpsWfiMode()

    @property
    @rad.field
    def ref_file(self: rad.Node) -> FpsRefFile:
        return FpsRefFile()

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
