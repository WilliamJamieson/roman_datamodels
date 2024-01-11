# Generated by RAD using generator based on datamodel-code-generator
#    source schema: coordinates-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from enum import Enum
from typing import Annotated, ClassVar

from pydantic import Field

from roman_datamodels.core._model import DataModel


class ReferenceFrame(Enum):
    ICRS = "ICRS"


class Coordinates(DataModel):
    """
    Information about the coordinates in the file
    """

    schema_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/schemas/coordinates-1.0.0"

    tag_uri: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/coordinates-1.0.0"

    reference_frame: Annotated[
        ReferenceFrame,
        Field(
            json_schema_extra={
                "archive_catalog": {
                    "datatype": "nvarchar(10)",
                    "destination": ["ScienceCommon.reference_frame", "GuideWindow.reference_frame"],
                }
            },
            title="Name of the coordinate reference frame",
        ),
    ]