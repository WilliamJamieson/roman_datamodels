from typing import Annotated, ClassVar, Literal

import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import NdArray
from .._config import create_shape_config
from .._core import BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_ndarray_factory
from .._enums import reftype
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon

__all__ = ["SuperbiasRefModel"]


_SHAPE, superbias_ref_shape_context = create_shape_config((4096, 4096))


class SuperbiasRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.BIAS],
        Field(
            default_factory=default_constant_factory(reftype.BIAS.value),
            title="Reference file type",
        ),
    ]


class SuperbiasRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.SUPERBIAS.value
    _tag_uri: ClassVar = asdf_tag_uri.SUPERBIAS.value

    model_config = ConfigDict(
        title="Superbias reference schema",
    )
    meta: Annotated[
        SuperbiasRefMeta,
        Field(
            default_factory=default_model_factory(SuperbiasRefMeta),
        ),
    ]
    data: Annotated[
        NdArray[np.float32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float32),
            title="2-D super-bias array",
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32),
            title="2-D data quality array for all planes",
        ),
    ]
    err: Annotated[
        NdArray[np.float32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float32),
            title="2-D Error array",
        ),
    ]
