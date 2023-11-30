from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel
from ..._enums import calibration_status

__all__ = ["CalStep"]


class CalStep(BaseDataModel):
    assign_wcs: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Assign World Coordinate System",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_assign_wcs",
                        "GuideWindow.s_assign_wcs",
                    ],
                },
            },
        ),
    ]
    flat_field: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Flat Field Step",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_flat_field",
                        "GuideWindow.s_flat_field",
                    ],
                },
            },
        ),
    ]
    dark: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Dark Subtraction",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_dark",
                        "GuideWindow.s_dark",
                    ],
                },
            },
        ),
    ]
    dq_init: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Data Quality Mask Step",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_dq_init",
                        "GuideWindow.s_dq_init",
                    ],
                },
            },
        ),
    ]
    jump: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Jump Detection Step",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_jump",
                        "GuideWindow.s_jump",
                    ],
                },
            },
        ),
    ]
    linearity: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Linearity Correction",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_linearity",
                        "GuideWindow.s_linearity",
                    ],
                },
            },
        ),
    ]
    photom: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Photometry Step",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_photom",
                        "GuideWindow.s_photom",
                    ],
                },
            },
        ),
    ]
    source_detection: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Source Detection Step",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_source_detection",
                        "GuideWindow.s_source_detection",
                    ],
                },
            },
        ),
    ]
    ramp_fit: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Ramp Fitting",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_ramp_fit",
                        "GuideWindow.s_ramp_fit",
                    ],
                },
            },
        ),
    ]
    refpix: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Reference Pixel Correction",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_refpix",
                        "GuideWindow.s_refpix",
                    ],
                },
            },
        ),
    ]
    saturation: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Saturation Checking",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_saturation",
                        "GuideWindow.s_saturation",
                    ],
                },
            },
        ),
    ]
    outlier_detection: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Outlier Detection",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_outlier_detection",
                        "GuideWindow.s_outlier_detection",
                    ],
                },
            },
        ),
    ]
    tweakreg: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Tweakreg Step",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_tweakreg",
                        "GuideWindow.s_tweakreg",
                    ],
                },
            },
        ),
    ]
    skymatch: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Sky Match Step",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_skymatch",
                        "GuideWindow.s_skymatch",
                    ],
                },
            },
        ),
    ]
    resample: Annotated[
        calibration_status,
        Field(
            json_schema_extra={
                "title": "Resample Step",
                "archive_catalog": {
                    "datatype": "nvarchar(15)",
                    "destination": [
                        "ScienceRefData.s_resample",
                        "GuideWindow.s_resample",
                    ],
                },
            },
        ),
    ]
