from typing import Annotated, Literal, Optional

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseDataModel, BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon, RefOpticalElement

__all__ = ["PixelareaRefModel"]


class Photometry(BaseDataModel):
    pixelarea_steradians: Annotated[
        Optional[AstropyQuantity[np.float64, u.steradian]],
        Field(
            json_schema_extra={
                "title": "Nominal pixel area in steradians",
            },
        ),
    ]
    pixelarea_steradians: Annotated[
        Optional[AstropyQuantity[np.float64, u.arcsec**2]],
        Field(
            json_schema_extra={
                "title": "Nominal pixel area in arcsec^2",
            },
        ),
    ]


class PixelareaRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[reftype.PIXELAREA],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]
    photometry: Annotated[
        Photometry,
        Field(
            json_schema_extra={
                "title": "Photometry information",
            },
        ),
    ]


class PixelareaRefModel(BaseRomanRefModel):
    meta: Annotated[
        PixelareaRefMeta,
        Field(
            json_schema_extra={
                "title": "Pixelarea reference metadata",
            },
        ),
    ]
    data: Annotated[
        NdArray[np.float32, 2],
        Field(
            json_schema_extra={
                "title": "Pixel area array",
            },
        ),
    ]
