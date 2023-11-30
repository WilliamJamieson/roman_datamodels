from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel
from ..._enums import instrument
from ._wfi_detector import WfiDetector
from ._wfi_optical_element import WfiOpticalElement

__all__ = ["WfiMode"]


class WfiMode(BaseDataModel):
    name: Annotated[
        instrument,
        Field(
            json_schema_extra={
                "title": "Instrument used to acquire the data",
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(5)",
                    "destination": [
                        "ScienceCommon.instrument_name",
                        "GuideWindow.instrument_name",
                    ],
                },
            },
        ),
    ]
    detector: Annotated[
        WfiDetector,
        Field(
            json_schema_extra={
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(10)",
                    "destination": [
                        "ScienceCommon.detector",
                        "GuideWindow.detector",
                    ],
                },
            },
        ),
    ]
    optical_element: Annotated[
        WfiOpticalElement,
        Field(
            json_schema_extra={
                "sdf": {
                    "special_processing": "VALUE_REQUIRED",
                    "source": {
                        "origin": "TBD",
                    },
                },
                "archive_catalog": {
                    "datatype": "nvarchar(10)",
                    "destination": [
                        "ScienceCommon.optical_element",
                        "GuideWindow.optical_element",
                    ],
                },
            },
        ),
    ]
