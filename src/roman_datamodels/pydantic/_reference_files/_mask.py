from typing import Annotated, Literal

import numpy as np
from pydantic import Field

from .._adaptors import NdArray
from .._core import BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon, RefOpticalElement

__all__ = ["MaskRefModel"]


class MaskRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[reftype.MASK],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]


class MaskRefModel(BaseRomanRefModel):
    meta: Annotated[
        MaskRefMeta,
        Field(
            json_schema_extra={
                "title": "Flat reference metadata",
            },
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            json_schema_extra={
                "title": "Data quality mask array",
            },
        ),
    ]
