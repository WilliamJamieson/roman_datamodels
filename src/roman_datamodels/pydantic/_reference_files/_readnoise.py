from __future__ import annotations

from typing import Annotated, Any, ClassVar, Literal

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from .._adaptors import AstropyQuantity
from .._core import BaseRomanRefModel
from .._defaults import (
    check_shape,
    default_constant_factory,
    default_model_factory,
    default_quantity_factory,
    fill_shape,
    quantity_factory,
)
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefExposureType, ref_type

__all__ = ["ReadnoiseRefModel"]


_SHAPE = (4096, 4096)


class ReadnoiseRefMeta(RefExposureType, RefCommon):
    reftype: Annotated[
        Literal[ref_type.READNOISE],
        Field(
            default_factory=default_constant_factory(ref_type.READNOISE.value),
            title="Reference file type",
        ),
    ]


class ReadnoiseRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.READNOISE.value
    _tag_uri: ClassVar = asdf_tag_uri.READNOISE.value

    _testing_default: ClassVar = {"shape": (8, 8)}

    model_config = ConfigDict(
        title="Read noise reference schema",
    )

    meta: Annotated[
        ReadnoiseRefMeta,
        Field(
            default_factory=default_model_factory(ReadnoiseRefMeta),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, 2, u.DN],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.DN),
            title="Dark Read noise data array",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        check_shape("data", shape, value=self.data)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> ReadnoiseRefModel:
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

            if isinstance(data, ReadnoiseRefMeta):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "data", shape, factory=quantity_factory(u.DN, np.float32))

        return data
