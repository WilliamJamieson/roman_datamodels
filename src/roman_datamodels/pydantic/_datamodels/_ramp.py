from typing import Annotated

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseRomanDataModel
from ._common import Common

__all__ = ["RampModel"]


class RampModel(BaseRomanDataModel):
    meta: Annotated[
        Common,
        Field(
            json_schema_extra={
                "title": "Ramp metadata",
            },
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, (u.DN, u.electron), 3],
        Field(
            json_schema_extra={
                "title": "Science data, including the border reference pixels.",
            },
        ),
    ]
    pixeldq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            json_schema_extra={
                "title": "2-D data quality array for all planes",
            },
        ),
    ]
    groupdq: Annotated[
        NdArray[np.uint32, 3],
        Field(
            json_schema_extra={
                "title": "3-D data quality array (plane dq for each group)",
            },
        ),
    ]
    err: Annotated[
        AstropyQuantity[np.float32, (u.DN, u.electron), 3],
        Field(
            json_schema_extra={
                "title": "Error array containing the square root of the exposure-level combined variance",
            },
        ),
    ]
    amp33: Annotated[
        AstropyQuantity[np.uint16, u.DN, 3],
        Field(
            json_schema_extra={
                "title": "Amp 33 reference pixel data",
            },
        ),
    ]
    border_ref_pix_left: Annotated[
        AstropyQuantity[np.float32, u.DN, 3],
        Field(
            json_schema_extra={
                "title": "Original border reference pixels, on left (from viewers perspective).",
            },
        ),
    ]
    border_ref_pix_right: Annotated[
        AstropyQuantity[np.float32, u.DN, 3],
        Field(
            json_schema_extra={
                "title": "Original border reference pixels, on right (from viewers perspective).",
            },
        ),
    ]
    border_ref_pix_top: Annotated[
        AstropyQuantity[np.float32, u.DN, 3],
        Field(
            json_schema_extra={
                "title": "Original border reference pixels, on top.",
            },
        ),
    ]
    border_ref_pix_bottom: Annotated[
        AstropyQuantity[np.float32, u.DN, 3],
        Field(
            json_schema_extra={
                "title": "Original border reference pixels, on bottom.",
            },
        ),
    ]
    dq_border_ref_pix_left: Annotated[
        NdArray[np.uint32, 2],
        Field(
            json_schema_extra={
                "title": "DQ for border reference pixels, on left (from viewers perspective).",
            },
        ),
    ]
    dq_border_ref_pix_right: Annotated[
        NdArray[np.uint32, 2],
        Field(
            json_schema_extra={
                "title": "DQ for border reference pixels, on right (from viewers perspective).",
            },
        ),
    ]
    dq_border_ref_pix_top: Annotated[
        NdArray[np.uint32, 2],
        Field(
            json_schema_extra={
                "title": "DQ for border reference pixels, on top.",
            },
        ),
    ]
    dq_border_ref_pix_bottom: Annotated[
        NdArray[np.uint32, 2],
        Field(
            json_schema_extra={
                "title": "DQ for border reference pixels, on bottom.",
            },
        ),
    ]
