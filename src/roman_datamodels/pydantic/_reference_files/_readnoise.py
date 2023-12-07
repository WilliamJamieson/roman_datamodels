from typing import Annotated, ClassVar, Literal

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity
from .._config import create_shape_config
from .._core import BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_quantity_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefExposureType, reftype

__all__ = ["ReadnoiseRefModel"]


_SHAPE, readnoise_ref_shape_context = create_shape_config((4096, 4096))


class ReadnoiseRefMeta(RefExposureType, RefCommon):
    reftype: Annotated[
        Literal[reftype.READNOISE],
        Field(
            default_factory=default_constant_factory(reftype.READNOISE.value),
            title="Reference file type",
        ),
    ]


class ReadnoiseRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.READNOISE.value
    _tag_uri: ClassVar = asdf_tag_uri.READNOISE.value

    model_config = ConfigDict(
        title="Read noise reference schema",
    )

    meta: Annotated[
        ReadnoiseRefMeta,
        Field(
            default_factory=default_model_factory(ReadnoiseRefMeta),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, 2, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN),
            title="Dark Read noise data array",
        ),
    ]
