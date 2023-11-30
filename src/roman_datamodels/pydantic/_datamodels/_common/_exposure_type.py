from typing import Annotated

from pydantic import Field

from ..._enums import exposure_type

__all__ = ["ExposureType"]

ExposureType = Annotated[
    exposure_type,
    Field(
        json_schema_extra={
            "title": "Type of data in the exposure (viewing mode)",
        },
    ),
]
