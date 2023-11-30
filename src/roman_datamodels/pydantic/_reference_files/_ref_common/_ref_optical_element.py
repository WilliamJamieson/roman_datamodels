from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel
from ..._datamodels import common

__all__ = ["RefOpticalElement"]


class RefOpticalElement(BaseDataModel):
    instrument: Annotated[
        common.WfiOpticalElement,
        Field(
            json_schema_extra={
                "title": "Name of the filter element used",
            },
        ),
    ]
