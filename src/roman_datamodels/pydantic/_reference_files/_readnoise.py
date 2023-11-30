from typing import Annotated, Literal

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity
from .._core import BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon, RefExposureType

__all__ = ["ReadnoiseRefModel"]


class ReadnoiseRefMeta(RefExposureType, RefCommon):
    reftype: Annotated[
        Literal[reftype.READNOISE],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]


class ReadnoiseRefModel(BaseRomanRefModel):
    meta: Annotated[
        ReadnoiseRefMeta,
        Field(
            json_schema_extra={
                "title": "Readnoise reference metadata",
            },
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, u.DN, 3],
        Field(
            json_schema_extra={
                "title": "Dark Read noise data array",
            },
        ),
    ]
