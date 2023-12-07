from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._core import BaseRomanTaggedModel, Number
from ..._defaults import default_constant_factory, default_num_value
from ..._enums import StrEnum
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Resample"]


class weight_type(StrEnum):
    exptime = "exptime"
    ivm = "ivm"


class Resample(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.RESAMPLE.value
    _tag_uri: ClassVar = asdf_tag_uri.RESAMPLE.value

    model_config = ConfigDict(
        title="Resample information",
    )

    pixel_scale_ratio: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Pixel Scale Ratio of resample to input scale",
        ),
    ]
    pixfrac: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Fraction of pixel to use for pixel convolution",
        ),
    ]
    pointings: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value * -1),
            title="Number of pointings in the resample",
        ),
    ]
    product_exposure_time: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value * -1),
            title="Total exposure time for resample product",
        ),
    ]
    weight_type: Annotated[
        weight_type,
        Field(
            default_factory=default_constant_factory(weight_type.exptime.value),
            title="Drizzle weight type for resample",
        ),
    ]
