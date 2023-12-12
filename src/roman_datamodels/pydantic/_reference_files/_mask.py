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

__all__ = ["MaskRefModel"]

_SHAPE = (4096, 4096)


class MaskRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[ref_type.MASK],
        Field(
            default_factory=default_constant_factory(ref_type.MASK.value),
            title="Reference file type",
        ),
    ]


class MaskRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.MASK.value
    _tag_uri: ClassVar = asdf_tag_uri.MASK.value

    _testing_default: ClassVar = {"shape": (8, 8)}

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
            default_factory=default_ndarray_factory(np.uint32, _SHAPE),
            title="Data quality mask array",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        check_shape("dq", shape, value=self.dq)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> MaskRefModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.dq.shape) != 2:
            raise ValueError(f"Expected 2-D dq, got {self.dq.shape}")

        self._check_shape(self.dq.shape)

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

            if isinstance(data, MaskRefModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "dq", shape, factory=ndarray_factory(np.uint32))

        return data
