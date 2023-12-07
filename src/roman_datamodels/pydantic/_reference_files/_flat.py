from typing import Annotated, ClassVar, Literal

import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import NdArray
from .._config import create_shape_config
from .._core import BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_ndarray_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefOpticalElement, reftype

__all__ = ["FlatRefModel"]


_SHAPE, flat_ref_shape_context = create_shape_config((4096, 4096))


class FlatRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[reftype.FLAT],
        Field(
            default_factory=default_constant_factory(reftype.FLAT.value),
            title="Reference file type",
        ),
    ]


class FlatRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.FLAT.value
    _tag_uri: ClassVar = asdf_tag_uri.FLAT.value

    model_config = ConfigDict(
        title="Flat reference schema",
    )

    meta: Annotated[
        FlatRefMeta,
        Field(
            default_factory=default_model_factory(FlatRefMeta),
        ),
    ]
    data: Annotated[
        NdArray[np.float32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float32),
            title="Flat data array",
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32),
            title="Data quality array",
        ),
    ]
    err: Annotated[
        NdArray[np.float32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float32),
            title="Error array",
        ),
    ]
