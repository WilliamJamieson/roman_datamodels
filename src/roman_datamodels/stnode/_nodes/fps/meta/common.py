from roman_datamodels.stnode import _default

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


class FpsCommon(FpsBasic):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/common-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            *super().asdf_required(),
            "cal_step",
            "exposure",
            "guidestar",
            "instrument",
            "ref_file",
            "hdf5_meta",
            "hdf5_telemetry",
            "gw_meta",
        )

    @property
    def cal_step(self) -> FpsCalStep:
        return self._get_node("cal_step", FpsCalStep)

    @property
    def exposure(self) -> FpsExposure:
        return self._get_node("exposure", FpsExposure)

    @property
    def guidestar(self) -> FpsGuidestar:
        return self._get_node("guidestar", FpsGuidestar)

    @property
    def instrument(self) -> FpsWfiMode:
        return self._get_node("instrument", FpsWfiMode)

    @property
    def ref_file(self) -> FpsRefFile:
        return self._get_node("ref_file", FpsRefFile)

    @property
    def hdf5_meta(self) -> dict:
        return self._get_node("hdf5_meta", lambda: {"test": _default.NOSTR})

    @property
    def hdf5_telemetry(self) -> str:
        return self._get_node("hdf5_telemetry", lambda: _default.NOSTR)

    @property
    def gw_meta(self) -> dict:
        return self._get_node("gw_meta", lambda: {"test": _default.NOSTR})

    @property
    def statistics(self) -> FpsStatistics:
        return self._get_node("statistics", FpsStatistics)
