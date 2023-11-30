from typing import Annotated, Literal

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon

__all__ = ["SaturationRefModel"]


class SaturationRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.SATURATION],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]


class SaturationRefModel(BaseRomanRefModel):
    meta: Annotated[
        SaturationRefMeta,
        Field(
            json_schema_extra={
                "title": "Saturation reference metadata",
            },
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, u.DN, 2],
        Field(
            json_schema_extra={
                "title": "Saturation threshold",
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
