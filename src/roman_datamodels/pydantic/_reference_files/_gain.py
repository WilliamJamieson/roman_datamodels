from typing import Annotated, Literal

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity
from .._core import BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon

__all__ = ["GainRefModel"]


class GainRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.GAIN],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]


class GainRefModel(BaseRomanRefModel):
    meta: Annotated[
        GainRefMeta,
        Field(
            json_schema_extra={
                "title": "Gain reference metadata",
            },
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, u.electron / u.DN, 2],
        Field(
            json_schema_extra={
                "title": "The detector gain map",
            },
        ),
    ]
