from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel
from ..._enums import optical_element

__all__ = ["WfiOpticalElement"]


class WfiOpticalElement(BaseDataModel):
    optical_element: Annotated[
        optical_element,
        Field(
            json_schema_extra={
                "title": "name of the filter element used",
            },
        ),
    ]
