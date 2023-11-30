from typing import Annotated

from pydantic import Field

from ..._adaptors import AstropyTime
from ..._core import BaseDataModel
from ..._enums import origin, telescope

__all__ = ["Basic"]


CalibrationSoftwareVersion = Annotated[
    str,
    Field(
        json_schema_extra={
            "title": "Calibration software version number",
            "sdf": {
                "special_processing": "VALUE_REQUIRED",
                "source": {
                    "origin": "TBD",
                },
            },
            "archive_catalog": {
                "datatype": "nvarchar(120)",
                "destination": [
                    "ScienceCommon.calibration_software_version",
                    "GuideWindow.calibration_software_version",
                ],
            },
            "flowStyle": "block",
        },
    ),
]
FileDate = Annotated[
    AstropyTime,
    Field(
        json_schema_extra={
            "title": "Date this file was created (UTC)",
            "sdf": {
                "special_processing": "VALUE_REQUIRED",
                "source": {
                    "origin": "TBD",
                },
            },
            "archive_catalog": {
                "datatype": "datetime2",
                "destination": [
                    "ScienceCommon.filedate",
                    "GuideWindow.filedate",
                ],
            },
            "flowStyle": "block",
        },
    ),
]
Filename = Annotated[
    str,
    Field(
        json_schema_extra={
            "title": "Name of the file",
            "sdf": {
                "special_processing": "VALUE_REQUIRED",
                "source": {
                    "origin": "TBD",
                },
            },
            "archive_catalog": {
                "datatype": "nvarchar(120)",
                "destination": [
                    "ScienceCommon.filename",
                    "GuideWindow.filename",
                ],
            },
            "flowStyle": "block",
        },
    ),
]
ModelType = Annotated[
    str,
    Field(
        json_schema_extra={
            "title": "Type of data model",
            "sdf": {
                "special_processing": "VALUE_REQUIRED",
                "source": {
                    "origin": "TBD",
                },
            },
            "archive_catalog": {
                "datatype": "nvarchar(50)",
                "destination": [
                    "ScienceCommon.model_type",
                    "GuideWindow.model_type",
                ],
            },
            "flowStyle": "block",
        },
    ),
]
Origin = Annotated[
    origin,
    Field(
        json_schema_extra={
            "title": "Organization responsible for creating file",
            "sdf": {
                "special_processing": "VALUE_REQUIRED",
                "source": {
                    "origin": "TBD",
                },
            },
            "archive_catalog": {
                "datatype": "nvarchar(15)",
                "destination": [
                    "ScienceCommon.origin",
                    "GuideWindow.origin",
                ],
            },
            "flowStyle": "block",
        },
    ),
]
PrdSoftwareVersion = Annotated[
    str,
    Field(
        json_schema_extra={
            "title": "S&OC PRD version number used in data processing",
            "sdf": {
                "special_processing": "VALUE_REQUIRED",
                "source": {
                    "origin": "TBD",
                },
            },
            "archive_catalog": {
                "datatype": "nvarchar(120)",
                "destination": [
                    "ScienceCommon.prd_software_version",
                    "GuideWindow.prd_software_version",
                ],
            },
            "flowStyle": "block",
        },
    ),
]
SdfSoftwareVersion = Annotated[
    str,
    Field(
        json_schema_extra={
            "title": "SDF software version number",
            "sdf": {
                "special_processing": "VALUE_REQUIRED",
                "source": {
                    "origin": "TBD",
                },
            },
            "archive_catalog": {
                "datatype": "nvarchar(120)",
                "destination": [
                    "ScienceCommon.sdf_software_version",
                    "GuideWindow.sdf_software_version",
                ],
            },
            "flowStyle": "block",
        },
    ),
]
Telescope = Annotated[
    telescope,
    Field(
        json_schema_extra={
            "title": "Telescope used to acquire the data",
            "sdf": {
                "special_processing": "VALUE_REQUIRED",
                "source": {
                    "origin": "TBD",
                },
            },
            "archive_catalog": {
                "datatype": "nvarchar(5)",
                "destination": [
                    "ScienceCommon.telescope",
                    "GuideWindow.telescope",
                ],
            },
            "flowStyle": "block",
        },
    ),
]


class Basic(BaseDataModel):
    calibration_software_version: CalibrationSoftwareVersion
    filename: Filename
    file_date: FileDate
    mdl_type: ModelType  # TODO: resolve the name issue
    origin: Origin
    prd_software_version: PrdSoftwareVersion
    sdf_software_version: SdfSoftwareVersion
    telescope: Telescope

    # This might resolve the name issue, but it could create problems
    # model_config = ConfigDict(
    #     protected_namespaces = ()
    # )
