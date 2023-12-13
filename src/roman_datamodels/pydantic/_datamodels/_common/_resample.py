from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _core, _defaults, _strenum
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Resample"]


class weight_type(_strenum.StrEnum):
    exptime = "exptime"
    ivm = "ivm"


class Resample(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.RESAMPLE.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.RESAMPLE.value

    model_config = ConfigDict(
        title="Resample information",
    )

    pixel_scale_ratio: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Pixel Scale Ratio of resample to input scale",
        ),
    ]
    pixfrac: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Fraction of pixel to use for pixel convolution",
        ),
    ]
    pointings: Annotated[
        int,
        Field(
            default_factory=_defaults.default_constant_factory(_defaults.default_num_value.NONUM.value * -1),
            title="Number of pointings in the resample",
        ),
    ]
    product_exposure_time: Annotated[
        float,
        Field(
            default_factory=_defaults.default_constant_factory(_defaults.default_num_value.NONUM.value * -1),
            title="Total exposure time for resample product",
        ),
    ]
    weight_type: Annotated[
        weight_type,
        Field(
            default_factory=_defaults.default_constant_factory(weight_type.exptime.value),
            title="Drizzle weight type for resample",
        ),
    ]
