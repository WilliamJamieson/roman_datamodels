from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["GuidewindowModes"]


class GuidewindowModes(str, _core.SchemaScalarNode):
    """
    Guidewindow modes
    """

    @classmethod
    def WIM_ACQ(cls) -> GuidewindowModes:
        return cls("WIM-ACQ")

    @classmethod
    def WIM_TRACK(cls) -> GuidewindowModes:
        return cls("WIM-TRACK")

    @classmethod
    def WSM_ACQ_1(cls) -> GuidewindowModes:
        return cls("WSM-ACQ-1")

    @classmethod
    def WSM_ACQ_2(cls) -> GuidewindowModes:
        return cls("WSM-ACQ-2")

    @classmethod
    def WSM_TRACK(cls) -> GuidewindowModes:
        return cls("WSM-TRACK")

    @classmethod
    def DEFOCUSED_MODERATE(cls) -> GuidewindowModes:
        return cls("DEFOCUSED-MODERATE")

    @classmethod
    def DEFOCUSED_LARGE(cls) -> GuidewindowModes:
        return cls("DEFOCUSED-LARGE")

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/guidewindow_modes-1.0.0"
