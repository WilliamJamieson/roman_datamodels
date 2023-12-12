from __future__ import annotations

from typing import Annotated, Any, ClassVar, Literal

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseRomanRefModel
from .._defaults import (
    check_shape,
    default_constant_factory,
    default_model_factory,
    default_ndarray_factory,
    default_quantity_factory,
    fill_shape,
    ndarray_factory,
    quantity_factory,
)
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, ref_type

__all__ = ["SaturationRefModel"]


_SHAPE = (4096, 4096)


class SaturationRefMeta(RefCommon):
    reftype: Annotated[
        Literal[ref_type.SATURATION],
        Field(
            default_factory=default_constant_factory(ref_type.SATURATION.value),
            title="Reference file type",
        ),
    ]


class SaturationRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.SATURATION.value
    _tag_uri: ClassVar = asdf_tag_uri.SATURATION.value

    _testing_default: ClassVar = {"shape": (8, 8)}

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
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.DN),
            title="Saturation threshold",
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(np.uint32, _SHAPE),
            title="2-D data quality array for all planes",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        check_shape("data", shape, value=self.data)
        check_shape("dq", shape, value=self.dq)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> SaturationRefModel:
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

            if isinstance(data, SaturationRefModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "data", shape, factory=quantity_factory(u.DN, np.float32))
                fill_shape(data, "dq", shape, factory=ndarray_factory(np.uint32))

        return data
