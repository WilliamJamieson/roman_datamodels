from typing import Annotated, Literal

import astropy.units as u
import numpy as np
from pydantic import Field

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseDataModel, BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon, RefExposureType, RefOpticalElement

__all__ = ["DarkRefModel"]


class Exposure(BaseDataModel):
    ngroups: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Number of groups in integration",
            },
        ),
    ]
    nframes: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Number of frames in group",
            },
        ),
    ]
    groupgap: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Number of frames dropped between groups",
            },
        ),
    ]
    ma_table_name: Annotated[
        str,
        Field(
            json_schema_extra={
                "title": "Name of the multi-accumulation table used",
            },
        ),
    ]
    ma_table_number: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Number of the multi-accumulation table used",
            },
        ),
    ]


class DarkRefMeta(RefOpticalElement, RefExposureType, RefCommon):
    reftype: Annotated[
        Literal[reftype.DARK],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]
    exposure: Annotated[
        Exposure,
        Field(
            json_schema_extra={
                "title": "Exposure parameters",
            },
        ),
    ]


class DarkRefModel(BaseRomanRefModel):
    meta: Annotated[
        DarkRefMeta,
        Field(
            json_schema_extra={
                "title": "Dark reference metadata",
            },
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, u.DN, 3],
        Field(
            json_schema_extra={
                "title": "Dark current array",
                "description": (
                    "The dark current array represents the integrated number of counts "
                    "due to the accumulation of dark current electrons in the pixels."
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
    dark_slope: Annotated[
        AstropyQuantity[np.float32, u.DN / u.s, 2],
        Field(
            json_schema_extra={
                "title": "Dark current slope array",
                "description": (
                    "The dark current slope array represents the slope of the "
                    "integrated number of counts due to the accumulation of dark "
                    "current electrons in the pixels for slope fitting purposes."
                ),
            },
        ),
    ]
    dark_slope_error: Annotated[
        AstropyQuantity[np.float32, u.DN / u.s, 2],
        Field(
            json_schema_extra={
                "title": "Uncertainty in dark current slope array",
            },
        ),
    ]
