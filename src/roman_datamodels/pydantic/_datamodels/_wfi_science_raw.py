from typing import Annotated

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseRomanDataModel
from ._common import Common

__all__ = ["ScienceRawModel"]


class ScienceRawModel(BaseRomanDataModel):
    meta: Annotated[
        Common,
        Field(
            json_schema_extra={
                "title": "WFI Science Raw metadata",
            },
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.uint16, u.DN, 2],
        Field(
            json_schema_extra={
                "title": "Science data, excluding border reference pixels.",
            },
        ),
    ]
    amp33: Annotated[
        AstropyQuantity[np.float32, u.DN, 3],
        Field(
            json_schema_extra={
                "title": "Amp 33 reference pixel data",
            },
        ),
    ]
    resultantdq: Annotated[
        NdArray[np.uint8, 3],
        Field(
            json_schema_extra={
                "title": "Optional 3-D data quality array (plane dq for each resultant",
            },
        ),
    ]
