from typing import Annotated

from pydantic import Field

from ..._enums import guidewindow_modes

__all__ = ["GuidewindowModes"]


GuidewindowModes = Annotated[
    guidewindow_modes,
    Field(
        json_schema_extra={
            "title": "Guide window mode",
        },
    ),
]
