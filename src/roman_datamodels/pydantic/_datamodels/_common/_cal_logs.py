from typing import Annotated

from pydantic import Field

__all__ = ["CalLogs"]


CalLogs = Annotated[
    list[str],
    Field(
        json_schema_extra={
            "title": "Calibration log messages",
        },
    ),
]
