from typing import Annotated, Callable, ClassVar, Literal

import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import NdArray
from .._config import create_shape_config
from .._core import BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_ndarray_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefOpticalElement, reftype

__all__ = ["IpcRefModel"]


_SHAPE, ipc_ref_shape_context = create_shape_config((4096, 4096))


def _default_data_factory() -> Callable[[], np.ndarray]:
    ndarray_factory = default_ndarray_factory(_SHAPE, np.float32)

    def _data_factory() -> np.ndarray:
        ndarray = ndarray_factory()
        n_rows, n_cols = ndarray.shape
        ndarray[int(np.floor(n_rows / 2)), int(np.floor(n_cols / 2))] = 1.0
        return ndarray

    return _data_factory


class IpcRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[reftype.IPC],
        Field(
            default_factory=default_constant_factory(reftype.IPC.value),
            title="Reference file type",
        ),
    ]


class IpcRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.IPC.value
    _tag_uri: ClassVar = asdf_tag_uri.IPC.value

    model_config = ConfigDict(
        title="IPC reference schema",
    )

    meta: Annotated[
        IpcRefMeta,
        Field(
            default_factory=default_model_factory(IpcRefMeta),
        ),
    ]
    data: Annotated[
        NdArray[np.float32, 2],
        Field(
            default_factory=_default_data_factory(),
            title="Interpixel capacitance correction kernel array",
            description="Reference kernel used for convolving with data in order to correct " "for interpixel capacitance",
        ),
    ]
