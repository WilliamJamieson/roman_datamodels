from __future__ import annotations

from typing import Annotated, Any, ClassVar, Literal

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from roman_datamodels.pydantic import _adaptors, _check, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

from . import _ref_common

__all__ = ["InverselinearityRefModel"]


_SHAPE = (2, 4096, 4096)


class InverselinearityRefMeta(_ref_common.RefCommon):
    reftype: Annotated[
        Literal[_ref_common.ref_type.INVERSELINEARITY],
        Field(
            default_factory=_defaults.default_constant_factory(_ref_common.ref_type.INVERSELINEARITY.value),
            title="Reference file type",
        ),
    ]
    input_units: Annotated[
        _adaptors.AstropyUnit[u.DN],
        Field(
            default_factory=_defaults.default_constant_factory(u.DN),
            title="Units of the input to the inverse linearity polynomial.",
        ),
    ]
    output_units: Annotated[
        _adaptors.AstropyUnit[u.DN],
        Field(
            default_factory=_defaults.default_constant_factory(u.DN),
            title="Units of the output of the inverse linearity polynomial.",
        ),
    ]


class InverselinearityRefModel(_core.BaseRomanRefModel):
    _uri: ClassVar = uri.asdf_uri.INVERSELINEARITY.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.INVERSELINEARITY.value

    _testing_default: ClassVar = {"shape": (2, 8, 8)}

    model_config = ConfigDict(
        title="Inverse linearity correction reference schema",
    )

    meta: Annotated[
        InverselinearityRefMeta,
        Field(
            default_factory=_defaults.default_model_factory(InverselinearityRefMeta),
        ),
    ]
    coeffs: Annotated[
        _adaptors.NdArray[np.float32, 3],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.float32, _SHAPE),
            title="Inverse linearly coefficients",
            description=(
                "Contains the coefficients of a polynomial to add classic non-linearity "
                "to pixels. Both the input to and output from the polynomial are in units "
                "of DN. The coefficients have units that contain various powers of DN."
            ),
        ),
    ]
    dq: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, _SHAPE[1:]),
            title="2-D data quality array for all planes",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        _n_shape = shape[0]
        _shape = shape[1:]

        _check.check_shape("coeffs", _shape, n_shape=_n_shape, value=self.coeffs)
        _check.check_shape("dq", _shape, value=self.dq)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> InverselinearityRefModel:
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

            if isinstance(data, InverselinearityRefModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                _check.fill_shape(data, "coeffs", _shape, n_shape=_n_shape, maker=_check.ndarray_maker(np.float32))
                _check.fill_shape(data, "dq", _shape, maker=_check.ndarray_maker(np.uint32))

        return data
