from typing import Annotated, Literal

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyUnit, NdArray
from .._core import BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon

__all__ = ["LinearityRefModel"]


class LinearityRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.LINEARITY],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]
    input_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            json_schema_extra={
                "title": "Units of the input to the linearity polynomial",
            },
        ),
    ]
    output_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            json_schema_extra={
                "title": "Units of the output of the linearity polynomial.",
            },
        ),
    ]


class LinearityRefModel(BaseRomanRefModel):
    meta: Annotated[
        LinearityRefMeta,
        Field(
            json_schema_extra={
                "title": "Linearity reference metadata",
            },
        ),
    ]
    coeffs: Annotated[
        NdArray[np.float32, 3],
        Field(
            json_schema_extra={
                "title": "Linearly coefficients",
                "description": (
                    "Contains the coefficients of a polynomial to correct pixel "
                    "values for classic non-linearity. Both the input to and "
                    "output from the polynomial are in units of DN. The coefficients "
                    "have units that contain various powers of DN."
                ),
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
