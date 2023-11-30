from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel, Number

__all__ = ["Pointing"]


class Pointing(BaseDataModel):
    ra_v1: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] RA of telescope V1 axis",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.ra_v1",
                        "GuideWindow.ra_v1",
                    ],
                },
            },
        ),
    ]
    dec_v1: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] Dec of telescope V1 axis",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.dec_v1",
                        "GuideWindow.dec_v1",
                    ],
                },
            },
        ),
    ]
    pa_v3: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] Position angle of telescope V3 axis",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.pa_v3",
                        "GuideWindow.pa_v3",
                    ],
                },
            },
        ),
    ]
