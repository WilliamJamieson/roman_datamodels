from roman_datamodels.stnode import _base, _core, _default

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


class FpsCommonMixin(_base.AdditionalNodeMixin):
    """Mixin things present in the constructors not present in the schema"""

    @_core.rad_field
    def statistics(self) -> FpsStatistics:
        return self._get_node("statistics", FpsStatistics)

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("statistics",)


class FpsCommon(FpsCommonMixin, FpsBasic):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/common-1.0.0"

    @_core.rad_field
    def cal_step(self) -> FpsCalStep:
        return self._get_node("cal_step", FpsCalStep)

    @_core.rad_field
    def exposure(self) -> FpsExposure:
        return self._get_node("exposure", FpsExposure)

    @_core.rad_field
    def guidestar(self) -> FpsGuidestar:
        return self._get_node("guidestar", FpsGuidestar)

    @_core.rad_field
    def instrument(self) -> FpsWfiMode:
        return self._get_node("instrument", FpsWfiMode)

    @_core.rad_field
    def ref_file(self) -> FpsRefFile:
        return self._get_node("ref_file", FpsRefFile)

    @_core.rad_field
    def hdf5_meta(self) -> _base.DNode:
        return self._get_node("hdf5_meta", lambda: _base.DNode({"test": _default.NOSTR}))

    @_core.rad_field
    def hdf5_telemetry(self) -> str:
        return self._get_node("hdf5_telemetry", lambda: _default.NOSTR)

    @_core.rad_field
    def gw_meta(self) -> _base.DNode:
        return self._get_node("gw_meta", lambda: _base.DNode({"test": _default.NOSTR}))
