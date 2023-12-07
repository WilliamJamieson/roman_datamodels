from typing import Annotated, ClassVar, Literal

import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import NdArray
from .._config import create_shape_config
from .._core import BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_ndarray_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefOpticalElement, reftype

__all__ = ["MaskRefModel"]

_SHAPE, mask_ref_shape_context = create_shape_config((4096, 4096))


class MaskRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[reftype.MASK],
        Field(
            default_factory=default_constant_factory(reftype.MASK.value),
            title="Reference file type",
        ),
    ]


class MaskRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.MASK.value
    _tag_uri: ClassVar = asdf_tag_uri.MASK.value

    model_config = ConfigDict(title="DQ Mask reference schema")

    meta: Annotated[
        MaskRefMeta,
        Field(
            default_factory=default_model_factory(MaskRefMeta),
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32),
            title="Data quality mask array",
        ),
    ]
