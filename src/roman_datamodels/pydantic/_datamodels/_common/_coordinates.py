from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel
from ..._enums import coordinates

__all__ = ["Coordinates"]


class Coordinates(BaseDataModel):
    reference_frame: Annotated[
        coordinates,
        Field(
            json_schema_extra={
                "title": "Reference frame",
                "archive_catalog": {
                    "datatype": "nvarchar(10)",
                    "destination": [
                        "ScienceCommon.reference_frame",
                        "GuideWindow.reference_frame",
                    ],
                },
            },
        ),
    ]
