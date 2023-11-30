from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel

__all__ = ["Program"]


class Program(BaseDataModel):
    title: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Proposal title",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_program.title",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(200)",
                    "destination": [
                        "ScienceCommon.program_title",
                        "GuideWindow.program_title",
                    ],
                },
            },
        ),
    ]
    pi_name: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Principle Investigator name",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(100)",
                    "destination": [
                        "ScienceCommon.pi_name",
                        "GuideWindow.pi_name",
                    ],
                },
            },
        ),
    ]
    category: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Program category",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_program.category",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(6)",
                    "destination": [
                        "ScienceCommon.program_category",
                        "GuideWindow.program_category",
                    ],
                },
            },
        ),
    ]
    subcategory: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Program subcategory",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_program.subcategory",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(6)",
                    "destination": [
                        "ScienceCommon.program_subcategory",
                        "GuideWindow.program_subcategory",
                    ],
                },
            },
        ),
    ]
    science_category: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Science category assigned during TAC process",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_program.science_category",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(50)",
                    "destination": [
                        "ScienceCommon.science_category",
                        "GuideWindow.science_category",
                    ],
                },
            },
        ),
    ]
    continuation_id: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Continuation of previous Program",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "PSS:dms_program.continuation_id",
                    },
                },
                "archive_catalog": {
                    "datatype": "int",
                    "destination": [
                        "ScienceCommon.continuation_id",
                        "GuideWindow.continuation_id",
                    ],
                },
            },
        ),
    ]
