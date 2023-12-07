from typing import Annotated

from pydantic import Field

from ..._enums import StrEnum

__all__ = ["GuidewindowModes", "guidewindow_modes"]


class guidewindow_modes(StrEnum):
    WIM_ACQ = "WIM-ACQ"
    WIM_TRACK = "WIM-TRACK"
    WSM_ACQ_1 = "WSM-ACQ-1"
    WSM_ACQ_2 = "WSM-ACQ-2"
    WSM_TRACK = "WSM-TRACK"
    DEFOCUSED_MODERATE = "DEFOCUSED-MODERATE"
    DEFOCUSED_LARGE = "DEFOCUSED-LARGE"


GuidewindowModes = Annotated[
    guidewindow_modes,
    Field(
        title="Guide window mode",
    ),
]
