from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel

__all__ = ["RefFile"]


class Crds(BaseDataModel):
    sw_version: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Version of CRDS file selection software used",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.crds_software_version",
                        "GuideWindow.crds_software_version",
                    ],
                },
            },
        ),
    ]
    context_used: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "CRDS context (.pmap) used to select ref files",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.crds_context_used",
                        "GuideWindow.crds_context_used",
                    ],
                },
            },
        ),
    ]


class RefFile(BaseDataModel):
    crds: Annotated[
        Crds,
        Field(
            json_schema_extra={
                "title": "CRDS Parameters",
            },
        ),
    ]
    dark: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Dark reference file location",
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.r_dark",
                        "GuideWindow.r_dark",
                    ],
                },
            },
        ),
    ]
    distortion: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Distortion reference file location",
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.r_distortion",
                        "GuideWindow.r_distortion",
                    ],
                },
            },
        ),
    ]
    mask: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Mask reference file location",
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.r_mask",
                        "GuideWindow.r_mask",
                    ],
                },
            },
        ),
    ]
    flat: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Flat reference file location",
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.r_flat",
                        "GuideWindow.r_flat",
                    ],
                },
            },
        ),
    ]
    gain: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Gain reference file location",
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.r_gain",
                        "GuideWindow.r_gain",
                    ],
                },
            },
        ),
    ]
    readnoise: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Readnoise reference file location",
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.r_readnoise",
                        "GuideWindow.r_readnoise",
                    ],
                },
            },
        ),
    ]
    linearity: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "linearity reference file location",
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.r_linearity",
                        "GuideWindow.r_linearity",
                    ],
                },
            },
        ),
    ]
    photom: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Photometry reference file location",
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.r_photom",
                        "GuideWindow.r_photom",
                    ],
                },
            },
        ),
    ]
    area: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Area reference file location",
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.r_area",
                        "GuideWindow.r_area",
                    ],
                },
            },
        ),
    ]
    saturation: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Saturation reference file location",
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": [
                        "ScienceCommon.r_saturation",
                        "GuideWindow.r_saturation",
                    ],
                },
            },
        ),
    ]
