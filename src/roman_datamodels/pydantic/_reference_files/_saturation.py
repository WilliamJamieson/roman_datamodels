from typing import Annotated, ClassVar, Literal

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity, NdArray
from .._config import create_shape_config
from .._core import BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_ndarray_factory, default_quantity_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, reftype

__all__ = ["SaturationRefModel"]


_SHAPE, saturation_ref_shape_context = create_shape_config((4096, 4096))


class SaturationRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.SATURATION],
        Field(
            default_factory=default_constant_factory(reftype.SATURATION.value),
            title="Reference file type",
        ),
    ]


class SaturationRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.SATURATION.value
    _tag_uri: ClassVar = asdf_tag_uri.SATURATION.value

    model_config = ConfigDict(
        title="Saturation reference schema",
    )

    meta: Annotated[
        SaturationRefMeta,
        Field(
            default_factory=default_model_factory(SaturationRefMeta),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, 2, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN),
            title="Saturation threshold",
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32),
            title="2-D data quality array for all planes",
        ),
    ]
