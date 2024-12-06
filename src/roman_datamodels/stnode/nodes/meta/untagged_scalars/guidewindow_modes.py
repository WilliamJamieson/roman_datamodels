from __future__ import annotations

from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["GuidewindowModes"]


class GuidewindowModesMixin(str, _core.SchemaScalarNode, _core.EnumNodeMixin):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/guidewindow_modes-1.0.0"


class GuidewindowModes(GuidewindowModesMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Guidewindow modes
    """

    WIM_ACQ = "WIM-ACQ"
    WIM_TRACK = "WIM-TRACK"
    WSM_ACQ_1 = "WSM-ACQ-1"
    WSM_ACQ_2 = "WSM-ACQ-2"
    WSM_TRACK = "WSM-TRACK"
    DEFOCUSED_MODERATE = "DEFOCUSED-MODERATE"
    DEFOCUSED_LARGE = "DEFOCUSED-LARGE"
