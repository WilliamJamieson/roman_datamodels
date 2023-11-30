from typing import Annotated, Literal

import numpy as np
from pydantic import Field

from .._adaptors import NdArray
from .._core import BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon

__all__ = ["SuperbiasRefModel"]


class SuperbiasRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.BIAS],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]


class SuperbiasRefModel(BaseRomanRefModel):
    meta: Annotated[
        SuperbiasRefMeta,
        Field(
            json_schema_extra={
                "title": "Super bias reference metadata",
            },
        ),
    ]
    data: Annotated[
        NdArray[np.float32, 2],
        Field(
            json_schema_extra={
                "title": "2-D super-bias array",
            },
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            json_schema_extra={
                "title": "2-D data quality array for all planes",
            },
        ),
    ]
    err: Annotated[
        NdArray[np.float32, 2],
        Field(
            json_schema_extra={
                "title": "2-D Error array",
            },
        ),
    ]
