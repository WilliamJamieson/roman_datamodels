from typing import Annotated, Literal

import numpy as np
from pydantic import Field

from .._adaptors import NdArray
from .._core import BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon, RefOpticalElement

__all__ = ["FlatRefModel"]


class FlatRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[reftype.FLAT],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]


class FlatRefModel(BaseRomanRefModel):
    meta: Annotated[
        FlatRefMeta,
        Field(
            json_schema_extra={
                "title": "Flat reference metadata",
            },
        ),
    ]
    data: Annotated[
        NdArray[np.float32, 2],
        Field(
            json_schema_extra={
                "title": "Flat data array",
            },
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            json_schema_extra={
                "title": "Data quality array",
            },
        ),
    ]
    err: Annotated[
        NdArray[np.float32, 2],
        Field(
            json_schema_extra={
                "title": "Error array",
            },
        ),
    ]
