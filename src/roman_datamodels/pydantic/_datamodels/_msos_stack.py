from typing import Annotated, ClassVar

import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import NdArray
from .._config import create_shape_config
from .._core import BaseRomanDataModel
from .._defaults import default_constant_factory, default_model_factory, default_ndarray_factory, default_str_value
from .._uri import asdf_tag_uri, asdf_uri
from ._common import Common

__all__ = ["MsosStackModel"]


class MsosStackMeta(Common):
    image_list: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
        ),
    ]


_SHAPE, msos_stack_shape_context = create_shape_config((4096, 4096))


class MsosStackModel(BaseRomanDataModel):
    _uri: ClassVar = asdf_uri.MSOS_STACK.value
    _tag_uri: ClassVar = asdf_tag_uri.MSOS_STACK.value

    model_config = ConfigDict(
        title="MSOS Stack Level 3 schema",
    )

    meta: Annotated[
        MsosStackMeta,
        Field(
            default_factory=default_model_factory(MsosStackMeta),
        ),
    ]
    data: Annotated[
        NdArray[np.float64, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float64),
            title="Flux data",
        ),
    ]
    uncertainty: Annotated[
        NdArray[np.float64, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float64),
            title="Uncertainty data",
        ),
    ]
    mask: Annotated[
        NdArray[np.uint8, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint8),
            title="Mask data",
        ),
    ]
    coverage: Annotated[
        NdArray[np.uint8, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint8),
            title="Coverage data",
        ),
    ]
