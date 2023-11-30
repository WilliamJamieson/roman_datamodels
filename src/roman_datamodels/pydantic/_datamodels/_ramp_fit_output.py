from typing import Annotated

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseRomanDataModel
from ._common import Common

__all__ = ["RampFitOutputModel"]


class RampFitOutputModel(BaseRomanDataModel):
    meta: Annotated[
        Common,
        Field(
            json_schema_extra={
                "title": "Ramp Fit Output metadata",
            },
        ),
    ]
    slope: Annotated[
        AstropyQuantity[np.float32, u.electron / u.s, 3],
        Field(
            json_schema_extra={
                "title": "Segment-specific slope",
            },
        ),
    ]
    sigslope: Annotated[
        AstropyQuantity[np.float32, u.electron / u.s, 3],
        Field(
            json_schema_extra={
                "title": "Sigma for segment-specific slope",
            },
        ),
    ]
    yint: Annotated[
        AstropyQuantity[np.float32, u.electron, 3],
        Field(
            json_schema_extra={
                "title": "Segment-specific y-intercept",
            },
        ),
    ]
    sigyint: Annotated[
        AstropyQuantity[np.float32, u.electron, 3],
        Field(
            json_schema_extra={
                "title": "Sigma for segment-specific y-intercept",
            },
        ),
    ]
    pedestal: Annotated[
        AstropyQuantity[np.float32, u.electron, 2],
        Field(
            json_schema_extra={
                "title": "Pedestal array",
            },
        ),
    ]
    weights: Annotated[
        NdArray[np.float32, 3],
        Field(
            json_schema_extra={
                "title": "Weights for segment-specific fits",
            },
        ),
    ]
    crmag: Annotated[
        AstropyQuantity[np.float32, u.electron, 3],
        Field(
            json_schema_extra={
                "title": "Approximate CR magnitudes",
            },
        ),
    ]
    var_poisson: Annotated[
        AstropyQuantity[np.float32, (u.electron / u.s) ** 2, 3],
        Field(
            json_schema_extra={
                "title": "Variance due to poisson noise for segment-specific slope",
            },
        ),
    ]
    var_rnoise: Annotated[
        AstropyQuantity[np.float32, (u.electron / u.s) ** 2, 3],
        Field(
            json_schema_extra={
                "title": "Variance due to read noise for segment-specific slope",
            },
        ),
    ]
