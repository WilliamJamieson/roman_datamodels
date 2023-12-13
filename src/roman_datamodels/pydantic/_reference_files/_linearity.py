from __future__ import annotations

from typing import Annotated, Any, ClassVar, Literal

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from .._adaptors import AstropyUnit, NdArray
from .._core import BaseRomanRefModel
from .._defaults import (
    check_shape,
    default_constant_factory,
    default_model_factory,
    default_ndarray_factory,
    fill_shape,
    ndarray_maker,
)
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, ref_type

__all__ = ["LinearityRefModel"]


_SHAPE = (2, 4096, 4096)


class LinearityRefMeta(RefCommon):
    reftype: Annotated[
        Literal[ref_type.LINEARITY],
        Field(
            default_factory=default_constant_factory(ref_type.LINEARITY.value),
            title="Reference file type",
        ),
    ]
    input_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            default_factory=default_constant_factory(u.DN),
            title="Units of the input to the linearity polynomial",
        ),
    ]
    output_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            default_factory=default_constant_factory(u.DN),
            title="Units of the output of the linearity polynomial.",
        ),
    ]


class LinearityRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.LINEARITY.value
    _tag_uri: ClassVar = asdf_tag_uri.LINEARITY.value

    _testing_default: ClassVar = {"shape": (2, 8, 8)}

    model_config = ConfigDict(
        title="Linearity correction reference schema",
    )

    meta: Annotated[
        LinearityRefMeta,
        Field(
            default_factory=default_model_factory(LinearityRefMeta),
        ),
    ]
    coeffs: Annotated[
        NdArray[np.float32, 3],
        Field(
            default_factory=default_ndarray_factory(np.float32, _SHAPE),
            title="Linearly coefficients",
            description=(
                "Contains the coefficients of a polynomial to correct pixel "
                "values for classic non-linearity. Both the input to and "
                "output from the polynomial are in units of DN. The coefficients "
                "have units that contain various powers of DN."
            ),
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(np.uint32, _SHAPE[1:]),
            title="2-D data quality array for all planes",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        _n_shape = shape[0]
        _shape = shape[1:]

        check_shape("coeffs", _shape, n_shape=_n_shape, value=self.coeffs)
        check_shape("dq", _shape, value=self.dq)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> LinearityRefModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.coeffs.shape) != 3:
            raise ValueError(f"Expected 3-D data, got {self.coeffs.shape}")

        self._check_shape(self.coeffs.shape)

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
            if shape and len(shape) != 3:
                raise ValueError(f"Expected 3-D shape, got {shape}")

            _shape = shape[1:] if shape else None
            _n_shape = shape[0] if shape else None

            if isinstance(data, LinearityRefModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "coeffs", _shape, n_shape=_n_shape, maker=ndarray_maker(np.float32))
                fill_shape(data, "dq", _shape, maker=ndarray_maker(np.uint32))

        return data
