from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["FpsGuidewindowModes"]


class FpsGuidewindowModes(str, _core.SchemaScalarNode):
    """
    Guidewindow modes
    """

    @classmethod
    def WIM_ACQ(cls) -> FpsGuidewindowModes:
        return cls("WIM-ACQ")

    @classmethod
    def WIM_TRACK(cls) -> FpsGuidewindowModes:
        return cls("WIM-TRACK")

    @classmethod
    def WSM_ACQ_1(cls) -> FpsGuidewindowModes:
        return cls("WSM-ACQ-1")

    @classmethod
    def WSM_ACQ_2(cls) -> FpsGuidewindowModes:
        return cls("WSM-ACQ-2")

    @classmethod
    def WSM_TRACK(cls) -> FpsGuidewindowModes:
        return cls("WSM-TRACK")

    @classmethod
    def DEFOCUSED_MODERATE(cls) -> FpsGuidewindowModes:
        return cls("DEFOCUSED-MODERATE")

    @classmethod
    def DEFOCUSED_LARGE(cls) -> FpsGuidewindowModes:
        return cls("DEFOCUSED-LARGE")

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/guidewindow_modes-1.0.0"
