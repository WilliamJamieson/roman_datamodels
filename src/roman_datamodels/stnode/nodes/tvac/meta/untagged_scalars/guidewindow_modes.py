from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["TvacGuidewindowModes"]


class TvacGuidewindowModes(str, _core.SchemaScalarNode):
    """
    Guidewindow modes
    """

    @classmethod
    def WIM_ACQ(cls) -> TvacGuidewindowModes:
        return cls("WIM-ACQ")

    @classmethod
    def WIM_TRACK(cls) -> TvacGuidewindowModes:
        return cls("WIM-TRACK")

    @classmethod
    def WSM_ACQ_1(cls) -> TvacGuidewindowModes:
        return cls("WSM-ACQ-1")

    @classmethod
    def WSM_ACQ_2(cls) -> TvacGuidewindowModes:
        return cls("WSM-ACQ-2")

    @classmethod
    def WSM_TRACK(cls) -> TvacGuidewindowModes:
        return cls("WSM-TRACK")

    @classmethod
    def DEFOCUSED_MODERATE(cls) -> TvacGuidewindowModes:
        return cls("DEFOCUSED-MODERATE")

    @classmethod
    def DEFOCUSED_LARGE(cls) -> TvacGuidewindowModes:
        return cls("DEFOCUSED-LARGE")

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/guidewindow_modes-1.0.0"
