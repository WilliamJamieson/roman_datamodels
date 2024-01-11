# Generated by RAD using generator based on datamodel-code-generator
#    source schema: ref_file-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._base import BaseDataModel
from roman_datamodels.core._model import DataModel


class Crds(BaseDataModel):
    """
    CRDS parameters
    """

    schema_uri: ClassVar[None] = None
    sw_version: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceCommon.crds_software_version", "GuideWindow.crds_software_version"],
                },
            },
            title="Version of CRDS file selection software used",
        ),
    ]
    context_used: Annotated[
        str,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceCommon.crds_context_used", "GuideWindow.crds_context_used"],
                },
            },
            title="CRDS context (.pmap) used to select ref files",
        ),
    ]


class RefFile(DataModel):
    """
    Reference file information
    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/ref_file-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/ref_file-1.0.0"

    crds: Annotated[Crds, Field(title="CRDS parameters")]
    dark: Annotated[
        str | None,
        Field(
            None,
            json_schema_extra={
                "archive_catalog": {"datatype": "nvarchar(120)", "destination": ["ScienceRefData.r_dark", "GuideWindow.r_dark"]}
            },
            title="Dark reference file information",
        ),
    ]
    distortion: Annotated[
        str | None,
        Field(
            None,
            json_schema_extra={
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceRefData.r_distortion", "GuideWindow.r_distortion"],
                }
            },
            title="Distortion reference file information",
        ),
    ]
    mask: Annotated[
        str | None,
        Field(
            None,
            json_schema_extra={
                "archive_catalog": {"datatype": "nvarchar(120)", "destination": ["ScienceRefData.r_mask", "GuideWindow.r_mask"]}
            },
            title="Mask reference file information",
        ),
    ]
    flat: Annotated[
        str | None,
        Field(
            None,
            json_schema_extra={
                "archive_catalog": {"datatype": "nvarchar(120)", "destination": ["ScienceRefData.r_flat", "GuideWindow.r_flat"]}
            },
            title="Flat reference file information",
        ),
    ]
    gain: Annotated[
        str | None,
        Field(
            None,
            json_schema_extra={
                "archive_catalog": {"datatype": "nvarchar(120)", "destination": ["ScienceRefData.r_gain", "GuideWindow.r_gain"]}
            },
            title="Gain reference file information",
        ),
    ]
    readnoise: Annotated[
        str | None,
        Field(
            None,
            json_schema_extra={
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceRefData.r_readnoise", "GuideWindow.r_readnoise"],
                }
            },
            title="Read noise reference file information",
        ),
    ]
    linearity: Annotated[
        str | None,
        Field(
            None,
            json_schema_extra={
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceRefData.r_linearity", "GuideWindow.r_linearity"],
                }
            },
            title="Linearity reference file information",
        ),
    ]
    photom: Annotated[
        str | None,
        Field(
            None,
            json_schema_extra={
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceRefData.r_photom", "GuideWindow.r_photom"],
                }
            },
            title="Photometry reference file information",
        ),
    ]
    area: Annotated[
        str | None,
        Field(
            None,
            json_schema_extra={
                "archive_catalog": {"datatype": "nvarchar(120)", "destination": ["ScienceRefData.r_area", "GuideWindow.r_area"]}
            },
            title="Area reference file information",
        ),
    ]
    saturation: Annotated[
        str | None,
        Field(
            None,
            json_schema_extra={
                "archive_catalog": {
                    "datatype": "nvarchar(120)",
                    "destination": ["ScienceRefData.r_saturation", "GuideWindow.r_saturation"],
                }
            },
            title="Saturation reference file information",
        ),
    ]
