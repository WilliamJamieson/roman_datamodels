from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel, Number

__all__ = ["Wcsinfo"]


class Wcsinfo(BaseDataModel):
    v2_ref: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[arcsec] Telescope v2 coordinate of the reference point",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.v2_ref",
                        "GuideWindow.v2_ref",
                    ],
                },
            },
        ),
    ]
    v3_ref: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[arcsec] Telescope v3 coordinate of the reference point",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.v3_ref",
                        "GuideWindow.v3_ref",
                    ],
                },
            },
        ),
    ]
    vparity: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Relative sense of rotation between Ideal xy and V2V3",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "ScienceCommon.vparity",
                        "GuideWindow.vparity",
                    ],
                },
            },
        ),
    ]
    v3yangle: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] Angle from V3 axis to Ideal y axis",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.v3yangle",
                        "GuideWindow.v3yangle",
                    ],
                },
            },
        ),
    ]
    ra_ref: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] Right ascension of the reference point",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.ra_ref",
                        "GuideWindow.ra_ref",
                    ],
                },
            },
        ),
    ]
    dec_ref: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] Declination of the reference point",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.dec_ref",
                        "GuideWindow.dec_ref",
                    ],
                },
            },
        ),
    ]
    roll_ref: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[deg] V3 roll angle at the ref point (N over E)",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.roll_ref",
                        "GuideWindow.roll_ref",
                    ],
                },
            },
        ),
    ]
    s_region: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "spatial extent of the observation",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(max)",
                    "destination": [
                        "ScienceCommon.s_region",
                        "GuideWindow.s_region",
                    ],
                },
            },
        ),
    ]
