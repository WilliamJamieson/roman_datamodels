# Generated by RAD using generator based on datamodel-code-generator
#    source schema: wfi_mode-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from enum import Enum
from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._extended import _WfiMode

from . import wfi_detector, wfi_optical_element


class name(Enum):
    WFI = "WFI"


class WfiMode(_WfiMode):
    """
    WFI observing configuration

    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/wfi_mode-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/wfi_mode-1.0.0"

    name: Annotated[
        name,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "nvarchar(5)",
                    "destination": ["ScienceCommon.instrument_name", "GuideWindow.instrument_name"],
                },
            },
            title="Instrument used to acquire the data",
        ),
    ]
    detector: Annotated[
        wfi_detector.WfiDetector,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "nvarchar(10)",
                    "destination": ["ScienceCommon.detector", "GuideWindow.detector"],
                },
            }
        ),
    ]
    optical_element: Annotated[
        wfi_optical_element.WfiOpticalElement,
        Field(
            json_schema_extra={
                "sdf": {"special_processing": "VALUE_REQUIRED", "source": {"origin": "TBD"}},
                "archive_catalog": {
                    "datatype": "nvarchar(20)",
                    "destination": ["ScienceCommon.optical_element", "GuideWindow.optical_element"],
                },
            }
        ),
    ]