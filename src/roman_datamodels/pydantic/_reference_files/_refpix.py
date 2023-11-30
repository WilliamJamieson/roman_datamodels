from typing import Annotated, Literal

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyUnit, NdArray
from .._core import BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon

__all__ = ["RefpixRefModel"]


class RefpixRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.REFPIX],
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
                "title": "Units of the input to the input to the reference pixel correction.",
            },
        ),
    ]
    output_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            json_schema_extra={
                "title": "Units of the output of the reference pixel correction.",
            },
        ),
    ]


class RefpixRefModel(BaseRomanRefModel):
    meta: Annotated[
        RefpixRefMeta,
        Field(
            json_schema_extra={
                "title": "Reference pixel correction reference metadata",
            },
        ),
    ]
    gamma: Annotated[
        NdArray[np.complex128, 2],
        Field(
            json_schema_extra={
                "title": "Left column correction coefficients",
            },
        ),
    ]
    zeta: Annotated[
        NdArray[np.complex128, 2],
        Field(
            json_schema_extra={
                "title": "Right column correction coefficients",
            },
        ),
    ]
    alpha: Annotated[
        NdArray[np.complex128, 2],
        Field(
            json_schema_extra={
                "title": "Reference amplifier (amp33) correction coefficients",
            },
        ),
    ]
