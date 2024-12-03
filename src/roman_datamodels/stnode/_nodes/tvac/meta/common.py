from roman_datamodels.stnode import _default

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


class TvacCommon(TvacBasic):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/common-1.0.0"

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
    def cal_step(self) -> TvacCalStep:
        return self._get_node("cal_step", TvacCalStep)

    @property
    def exposure(self) -> TvacExposure:
        return self._get_node("exposure", TvacExposure)

    @property
    def guidestar(self) -> TvacGuidestar:
        return self._get_node("guidestar", TvacGuidestar)

    @property
    def instrument(self) -> TvacWfiMode:
        return self._get_node("instrument", TvacWfiMode)

    @property
    def ref_file(self) -> TvacRefFile:
        return self._get_node("ref_file", TvacRefFile)

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
    def statistics(self) -> TvacStatistics:
        return self._get_node("statistics", TvacStatistics)
