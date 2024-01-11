# Generated by RAD using generator based on datamodel-code-generator
#    source schema: aperture-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from enum import Enum
from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._model import DataModel


class Name(Enum):
    WFI_01_FULL = "WFI_01_FULL"
    WFI_02_FULL = "WFI_02_FULL"
    WFI_03_FULL = "WFI_03_FULL"
    WFI_04_FULL = "WFI_04_FULL"
    WFI_05_FULL = "WFI_05_FULL"
    WFI_06_FULL = "WFI_06_FULL"
    WFI_07_FULL = "WFI_07_FULL"
    WFI_08_FULL = "WFI_08_FULL"
    WFI_09_FULL = "WFI_09_FULL"
    WFI_10_FULL = "WFI_10_FULL"
    WFI_11_FULL = "WFI_11_FULL"
    WFI_12_FULL = "WFI_12_FULL"
    WFI_13_FULL = "WFI_13_FULL"
    WFI_14_FULL = "WFI_14_FULL"
    WFI_15_FULL = "WFI_15_FULL"
    WFI_16_FULL = "WFI_16_FULL"
    WFI_17_FULL = "WFI_17_FULL"
    WFI_18_FULL = "WFI_18_FULL"
    BORESIGHT = "BORESIGHT"
    CGI_CEN = "CGI_CEN"
    WFI_CEN = "WFI_CEN"


class Aperture(DataModel):
    """
    Aperture information
    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/aperture-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/aperture-1.0.0"

    name: Annotated[
        Name,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "PSS:aperture.AperName"}},
                "archive_catalog": {
                    "datatype": "nvarchar(40)",
                    "destination": ["ScienceCommon.aperture_name", "GuideWindow.aperture_name"],
                },
            },
            title="PRD science aperture used",
        ),
    ]
    position_angle: Annotated[
        float,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "float",
                    "destination": ["ScienceCommon.position_angle", "GuideWindow.position_angle"],
                },
            },
            title="[deg] Position angle of aperture used",
        ),
    ]