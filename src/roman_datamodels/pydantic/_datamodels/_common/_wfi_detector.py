from typing import Annotated

from pydantic import Field

from ..._enums import detector

__all__ = ["WfiDetector"]


WfiDetector = Annotated[
    detector,
    Field(
        json_schema_extra={
            "title": "Name of detector used to acquire the data",
        },
    ),
]
