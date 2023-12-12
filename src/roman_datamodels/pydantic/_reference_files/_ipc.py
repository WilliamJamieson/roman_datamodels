from __future__ import annotations

from typing import Annotated, Any, Callable, ClassVar, Literal

import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from .._adaptors import NdArray
from .._core import BaseRomanRefModel
from .._defaults import check_shape, default_constant_factory, default_model_factory, fill_shape, ndarray_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefOpticalElement, ref_type

__all__ = ["IpcRefModel"]


_SHAPE = (4096, 4096)


def _data_factory(shape: tuple[int]) -> np.ndarray:
    ndarray = ndarray_factory(np.float32)(shape)
    n_rows, n_cols = ndarray.shape
    ndarray[int(np.floor(n_rows / 2)), int(np.floor(n_cols / 2))] = 1.0
    return ndarray


def _default_data_factory(shape: tuple[int]) -> Callable[[], np.ndarray]:
    _ndarray_factory = _data_factory(shape)

    def _factory() -> np.ndarray:
        return _ndarray_factory

    return _factory


class IpcRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[ref_type.IPC],
        Field(
            default_factory=default_constant_factory(ref_type.IPC.value),
            title="Reference file type",
        ),
    ]


class IpcRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.IPC.value
    _tag_uri: ClassVar = asdf_tag_uri.IPC.value

    _testing_default: ClassVar = {"shape": (8, 8)}

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
            default_factory=_default_data_factory(_SHAPE),
            title="Interpixel capacitance correction kernel array",
            description="Reference kernel used for convolving with data in order to correct " "for interpixel capacitance",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        check_shape("data", shape, value=self.data)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> IpcRefModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.data.shape) != 2:
            raise ValueError(f"Expected 2-D data, got {self.data.shape}")

        self._check_shape(self.data.shape)

        return self

    @model_validator(mode="before")
    @classmethod
    def _handle_input_shape(cls, data: Any, info: ValidationInfo) -> Any:
        """Handle shaping the default input data"""
        context = info.context

        if context:
            if not set(context.keys()).issubset({"shape"}):
                raise ValueError(f"Only 'shape' is allowed in context, got {list(context.keys())}")

            shape = context.get("shape", None)
            if shape and len(shape) != 2:
                raise ValueError(f"Expected 2-D shape, got {shape}")

            if isinstance(data, IpcRefMeta):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "data", shape, factory=_data_factory)

        return data
