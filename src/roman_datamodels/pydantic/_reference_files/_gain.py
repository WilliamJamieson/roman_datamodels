from typing import Annotated, ClassVar, Literal

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity
from .._config import create_shape_config
from .._core import BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_quantity_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, reftype

__all__ = ["GainRefModel"]


_SHAPE, gain_ref_shape_context = create_shape_config((4096, 4096))


class GainRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.GAIN],
        Field(
            default_factory=default_constant_factory(reftype.GAIN.value),
            title="Reference file type",
        ),
    ]


class GainRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.GAIN.value
    _tag_uri: ClassVar = asdf_tag_uri.GAIN.value

    model_config = ConfigDict(
        title="Gain reference schema",
    )

    meta: Annotated[
        GainRefMeta,
        Field(
            default_factory=default_model_factory(GainRefMeta),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, 2, u.electron / u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron / u.DN),
            title="The detector gain map",
        ),
    ]
