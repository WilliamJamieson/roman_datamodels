from typing import Annotated

import numpy as np
from pydantic import Field

from .._adaptors import NdArray
from .._core import BaseRomanDataModel
from ._common import Common

__all__ = ["MsosStackModel"]


class MsosStackMeta(Common):
    image_list: Annotated[str, Field()]


class MsosStackModel(BaseRomanDataModel):
    meta: Annotated[
        MsosStackMeta,
        Field(
            json_schema_extra={
                "title": "MSOS Stack metadata",
            },
        ),
    ]
    data: Annotated[
        NdArray[np.float64, 2],
        Field(
            json_schema_extra={
                "title": "Flux data",
            },
        ),
    ]
    uncertainty: Annotated[
        NdArray[np.float64, 2],
        Field(
            json_schema_extra={
                "title": "Uncertainty data",
            },
        ),
    ]
    mask: Annotated[
        NdArray[np.uint8, 2],
        Field(
            json_schema_extra={
                "title": "Mask data",
            },
        ),
    ]
    coverage: Annotated[
        NdArray[np.uint8, 2],
        Field(
            json_schema_extra={
                "title": "Coverage data",
            },
        ),
    ]
