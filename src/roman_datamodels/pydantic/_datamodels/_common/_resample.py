from typing import Annotated

from pydantic import Field

from ..._core import BaseDataModel, Number
from ..._enums import weight_type

__all__ = ["Resample"]


class Resample(BaseDataModel):
    pixel_scale_ratio: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Pixel Scale Ratio of resample to input scale",
            },
        ),
    ]
    pixfrac: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Fraction of pixel to use for pixel convolution",
            },
        ),
    ]
    pointings: Annotated[
        int,
        Field(
            json_schema_extra={
                "title": "Number of pointings in the resample",
            },
        ),
    ]
    product_exposure_time: Annotated[
        Number,
        Field(
            json_schema_extra={
                "title": "Total exposure time for resample product",
            },
        ),
    ]
    weight_type: Annotated[
        weight_type,
        Field(
            json_schema_extra={
                "title": "Drizzle weight type for resample",
            },
        ),
    ]
