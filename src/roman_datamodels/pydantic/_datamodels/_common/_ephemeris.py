from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel, Number
from ..._enums import ephemeris_type

__all__ = ["Ephemeris"]


class Ephemeris(BaseDataModel):
    earth_angle: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[radians] Earth Angle",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.earth_angle",
                        "GuideWindow.earth_angle",
                    ],
                },
            },
        ),
    ]
    moon_angle: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[radians] Moon Angle",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.moon_angle",
                        "GuideWindow.moon_angle",
                    ],
                },
            },
        ),
    ]
    ephemeris_reference_frame: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Ephemeris reference frame",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(10)",
                    "destination": [
                        "ScienceCommon.ephemeris_reference_frame",
                        "GuideWindow.ephermeris_reference_frame",
                    ],
                },
            },
        ),
    ]
    sun_angle: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[radians] Sun Angle",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.sun_angle",
                        "GuideWindow.sun_angle",
                    ],
                },
            },
        ),
    ]
    type: Annotated[
        ephemeris_type,
        Field(
            json_schema_extra={
                "title": "Type of ephemeris",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.ephermeris_type",
                        "GuideWindow.ephemeris_type",
                    ],
                },
            },
        ),
    ]
    time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "UTC time of position and velocity vectors in ephemeris (MJD)",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Roman Science Data Processing (RSDP)",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.ephemeris_time",
                        "GuideWindow.ephermeris_time",
                    ],
                },
            },
        ),
    ]
    spatial_x: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[km] X spatial coordinate of Roman",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Roman Science Data Processing (RSDP)",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.spatial_x",
                        "GuideWindow.spatial_x",
                    ],
                },
            },
        ),
    ]
    spatial_y: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[km] Y spatial coordinate of Roman",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Roman Science Data Processing (RSDP)",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.spatial_y",
                        "GuideWindow.spatial_y",
                    ],
                },
            },
        ),
    ]
    spatial_z: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[km] Z spatial coordinate of Roman",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Roman Science Data Processing (RSDP)",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.spatial_z",
                        "GuideWindow.spatial_z",
                    ],
                },
            },
        ),
    ]
    velocity_x: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[km/s] X component of Roman velocity",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Roman Science Data Processing (RSDP)",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.velocity_x",
                        "GuideWindow.velocity_x",
                    ],
                },
            },
        ),
    ]
    velocity_y: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[km/s] Y component of Roman velocity",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Roman Science Data Processing (RSDP)",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.velocity_y",
                        "GuideWindow.velocity_y",
                    ],
                },
            },
        ),
    ]
    velocity_z: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "[km/s] Z component of Roman velocity",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "Roman Science Data Processing (RSDP)",
                    },
                },
                "archive_catalog": {
                    "datatype": "float",
                    "destination": [
                        "ScienceCommon.velocity_z",
                        "GuideWindow.velocity_z",
                    ],
                },
            },
        ),
    ]
