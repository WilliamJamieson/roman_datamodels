from typing import Annotated

from pydantic import Field

from ..._adaptors import AstropyTime
from ..._core import BaseDataModel
from ..._enums import engineering_quality, pointing_engdb_quality

__all__ = ["Visit"]


class Visit(BaseDataModel):
    engineering_quality: Annotated[
        engineering_quality,
        Field(
            json_schema_extra={
                "title": "Engineering data quality indicator from EngDB",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(10)",
                    "destination": [
                        "ScienceCommon.engineering_quality",
                        "GuideWindow.engineering_quality",
                    ],
                },
            },
        ),
    ]
    pointing_engdb_quality: Annotated[
        pointing_engdb_quality,
        Field(
            json_schema_extra={
                "title": "Quality of pointing information from EngDB",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(10)",
                    "destination": [
                        "ScienceCommon.pointing_engdb_quality",
                        "GuideWindow.pointing_engdb_quality",
                    ],
                },
            },
        ),
    ]
    type: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Visit type",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(30)",
                    "destination": [
                        "ScienceCommon.visit_type",
                        "GuideWindow.visit_type",
                    ],
                },
            },
        ),
    ]
    start_time: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "title": "UTC visit start time",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "datetime2",
                    "destination": [
                        "ScienceCommon.visit_start_time",
                        "GuideWindow.visit_start_time",
                    ],
                },
            },
        ),
    ]
    end_time: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "title": "UTC visit mid time",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "datetime2",
                    "destination": [
                        "ScienceCommon.visit_end_time",
                        "GuideWindow.visit_end_time",
                    ],
                },
            },
        ),
    ]
    status: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Status of a visit",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceCommon.visit_status",
                        "GuideWindow.visit_status",
                    ],
                },
            },
        ),
    ]
    total_exposures: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Total number of planned exposures in visit",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "ScienceCommon.visit_total_exposures",
                        "GuideWindow.visit_total_exposures",
                    ],
                },
            },
        ),
    ]
    internal_target: Annotated[
        bool,
        Field(
            json_schema_extra={
                "title": "At least one exposure in visit is internal",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nchar(1)",
                    "destination": [
                        "ScienceCommon.visit_internal_target",
                        "GuideWindow.visit_internal_target",
                    ],
                },
            },
        ),
    ]
    target_of_opportunity: Annotated[
        bool,
        Field(
            json_schema_extra={
                "title": "Visit scheduled as target of opportunity",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nchar(1)",
                    "destination": [
                        "ScienceCommon.target_of_opportunity",
                        "GuideWindow.target_of_opportunity",
                    ],
                },
            },
        ),
    ]
