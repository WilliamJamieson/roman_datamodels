# Generated by RAD using generator based on datamodel-code-generator
#    source schema: program-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._model import DataModel


class Program(DataModel):
    """
    Program information
    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/program-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/program-1.0.0"

    title: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "PSS:dms_program.title"}},
                "archive_catalog": {
                    "datatype": "nvarchar(200)",
                    "destination": ["ScienceCommon.program_title", "GuideWindow.program_title"],
                },
            },
            title="Proposal title",
        ),
    ]
    pi_name: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {"datatype": "nvarchar(100)", "destination": ["ScienceCommon.pi_name", "GuideWindow.pi_name"]},
            },
            title="Principle Investigator name",
        ),
    ]
    category: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "PSS:dms_program.category"}},
                "archive_catalog": {
                    "datatype": "nvarchar(6)",
                    "destination": ["ScienceCommon.program_category", "GuideWindow.program_category"],
                },
            },
            title="Program category",
        ),
    ]
    subcategory: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "PSS:dms_program.subcategory"}},
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": ["ScienceCommon.program_subcategory", "GuideWindow.program_subcategory"],
                },
            },
            title="Program subcategory",
        ),
    ]
    science_category: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "PSS:dms_program.science_category"}},
                "archive_catalog": {
                    "datatype": "nvarchar(50)",
                    "destination": ["ScienceCommon.science_category", "GuideWindow.science_category"],
                },
            },
            title="Science category assigned during TAC process",
        ),
    ]
    continuation_id: Annotated[
        int,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "PSS:dms_program.continuation_id"}},
                "archive_catalog": {
                    "datatype": "int",
                    "destination": ["ScienceCommon.continuation_id", "GuideWindow.continuation_id"],
                },
            },
            title="Continuation of previous Program",
        ),
    ]
