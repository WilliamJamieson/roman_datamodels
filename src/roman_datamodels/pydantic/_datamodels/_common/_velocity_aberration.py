from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel, Number

__all__ = ["VelocityAberration"]


class VelocityAberration(BaseDataModel):
    ra_offset: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Velocity aberration right ascension offset",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.ra_offset",
                        "GuideWindow.ra_offset",
                    ],
                },
            },
        ),
    ]
    dec_offset: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Velocity aberration declination offset",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.dec_offset",
                        "GuideWindow.dec_offset",
                    ],
                },
            },
        ),
    ]
    scale_factor: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Velocity aberration scale factor",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.scale_factor",
                        "GuideWindow.scale_factor",
                    ],
                },
            },
        ),
    ]
