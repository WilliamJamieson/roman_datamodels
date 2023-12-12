from __future__ import annotations

from typing import Annotated, Any, ClassVar, Literal

import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from .._adaptors import NdArray
from .._core import BaseRomanRefModel
from .._defaults import (
    check_shape,
    default_constant_factory,
    default_model_factory,
    default_ndarray_factory,
    fill_shape,
    ndarray_factory,
)
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefOpticalElement, ref_type

__all__ = ["FlatRefModel"]


_SHAPE = (4096, 4096)


class FlatRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[ref_type.FLAT],
        Field(
            default_factory=default_constant_factory(ref_type.FLAT.value),
            title="Reference file type",
        ),
    ]


class FlatRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.FLAT.value
    _tag_uri: ClassVar = asdf_tag_uri.FLAT.value

    _testing_default: ClassVar = {"shape": (8, 8)}

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
            default_factory=default_ndarray_factory(np.float32, _SHAPE),
            title="Flat data array",
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(np.uint32, _SHAPE),
            title="Data quality array",
        ),
    ]
    err: Annotated[
        NdArray[np.float32, 2],
        Field(
            default_factory=default_ndarray_factory(np.float32, _SHAPE),
            title="Error array",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        check_shape("data", shape, value=self.data)
        check_shape("dq", shape, value=self.dq)
        check_shape("err", shape, value=self.err)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> FlatRefModel:
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

            if isinstance(data, FlatRefModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "data", shape, factory=ndarray_factory(np.float32))
                fill_shape(data, "dq", shape, factory=ndarray_factory(np.uint32))
                fill_shape(data, "err", shape, factory=ndarray_factory(np.float32))

        return data
