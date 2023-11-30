from typing import Annotated, Optional

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseRomanDataModel
from ._common import CalLogs, Common, Photometry, Resample

__all__ = ["MosaicModel"]


class MosaicMeta(Common):
    photometry: Annotated[
        Photometry,
        Field(
            json_schema_extra={
                "title": "Photometry data",
            },
        ),
    ]
    resample: Annotated[
        Optional[Resample],
        Field(
            json_schema_extra={
                "title": "Resample data",
            },
        ),
    ]


class MosaicModel(BaseRomanDataModel):
    meta: Annotated[
        MosaicMeta,
        Field(
            json_schema_extra={
                "title": "WFI Mosaic metadata",
            },
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, u.electron / u.s, 2],
        Field(
            json_schema_extra={
                "title": "Science data, excluding border reference pixels.",
            },
        ),
    ]
    err: Annotated[
        AstropyQuantity[np.float32, u.electron / u.s, 2],
        Field(),
    ]
    context: Annotated[
        NdArray[np.uint32, 3],
        Field(),
    ]
    weight: Annotated[
        NdArray[np.float32, 3],
        Field(),
    ]
    var_poisson: Annotated[
        AstropyQuantity[np.float32, (u.electron / u.s) ** 2, 2],
        Field(),
    ]
    var_rnoise: Annotated[
        AstropyQuantity[np.float32, (u.electron / u.s) ** 2, 2],
        Field(),
    ]
    var_flat: Annotated[
        AstropyQuantity[np.float32, (u.electron / u.s) ** 2, 2],
        Field(),
    ]
    cal_logs: Annotated[
        CalLogs,
        Field(),
    ]
