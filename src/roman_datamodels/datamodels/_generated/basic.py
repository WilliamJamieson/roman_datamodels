# Generated by RAD using generator based on datamodel-code-generator
#    source schema: basic-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from enum import Enum
from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._base import BaseDataModel
from roman_datamodels.core.adaptors import AstropyTime


class Origin(Enum):
    STSCI = "STSCI"
    IPAC_SSC = "IPAC/SSC"


class Telescope(Enum):
    ROMAN = "ROMAN"


class Basic(BaseDataModel):
    """
    Common metadata keywords
    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/basic-1.0.0"

    calibration_software_version: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceCommon.calibration_software_version", "GuideWindow.calibration_software_version"],
                },
            },
            title="Calibration software version number",
        ),
    ]
    filename: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceCommon.filename", "GuideWindow.filename"],
                },
            },
            title="Name of the file",
        ),
    ]
    file_date: Annotated[
        AstropyTime,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {"datatype": "datetime2", "destination": ["ScienceCommon.filedate", "GuideWindow.filedate"]},
            },
            title="Date this file was created (UTC)",
        ),
    ]
    model_type: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "nvarchar(50)",
                    "destination": ["ScienceCommon.model_type", "GuideWindow.model_type"],
                },
            },
            title="Type of data model",
        ),
    ]
    origin: Annotated[
        Origin,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {"datatype": "nvarchar(15)", "destination": ["ScienceCommon.origin", "GuideWindow.origin"]},
            },
            title="Organization responsible for creating file",
        ),
    ]
    prd_software_version: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceCommon.prd_software_version", "GuideWindow.prd_software_version"],
                },
            },
            title="S&OC PRD version number used in data processing",
        ),
    ]
    sdf_software_version: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceCommon.sdf_software_version", "GuideWindow.sdf_software_version"],
                },
            },
            title="SDF software version number",
        ),
    ]
    telescope: Annotated[
        Telescope,
        Field(
            json_schema_extra={
                "archive_catalog": {
                    "datatype": "nvarchar(5)",
                    "destination": ["ScienceCommon.telescope", "GuideWindow.telescope"],
                }
            },
            title="Telescope used to acquire the data",
        ),
    ]