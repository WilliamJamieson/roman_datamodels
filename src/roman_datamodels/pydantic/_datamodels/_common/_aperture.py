from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel, Number
from ..._enums import aperture

__all__ = ["Aperture"]


class Aperture(BaseDataModel):
    name: Annotated[
        aperture,
        Field(
            json_schema_extra={
                "title": "PRD science aperture used",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:aperture.AperName",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(40)",
                    "destination": [
                        "ScienceCommon.aperture_name",
                        "GuideWindow.aperture_name",
                    ],
                },
            },
        ),
    ]
    position_angle: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] Position angle of aperture used",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",  # v3_position_angle in baseline_prime_visits or spacecraft_parameters
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.position_angle",
                        "GuideWindow.position_angle",
                    ],
                },
            },
        ),
    ]
