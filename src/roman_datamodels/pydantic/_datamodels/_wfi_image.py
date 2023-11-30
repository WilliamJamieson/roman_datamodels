from typing import Annotated, Optional

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseRomanDataModel
from ._common import Common, Photometry, SourceDetection

__all__ = ["ImageModel"]


class ImageMeta(Common):
    photometry: Annotated[
        Photometry,
        Field(
            json_schema_extra={
                "title": "Photometry data",
            },
        ),
    ]
    source_detection: Annotated[
        Optional[SourceDetection],
        Field(
            json_schema_extra={
                "title": "Source Detection data",
            },
        ),
    ]


class ImageModel(BaseRomanDataModel):
    meta: Annotated[
        ImageMeta,
        Field(
            json_schema_extra={
                "title": "WFI image metadata",
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
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(),
    ]
    err: Annotated[
        AstropyQuantity[np.float32, u.electron / u.s, 2],
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
    amp33: Annotated[
        AstropyQuantity[np.float32, u.DN, 3],
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
