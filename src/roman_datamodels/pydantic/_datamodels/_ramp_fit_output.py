from __future__ import annotations

from typing import Annotated, Any, ClassVar

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from roman_datamodels.pydantic import _adaptors, _check, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

from . import _common

__all__ = ["RampFitOutputModel"]


_SHAPE = (8, 4096, 4096)


class RampFitOutputModel(_core.BaseRomanStepModel):
    _uri: ClassVar = uri.asdf_uri.RAMP_FIT_OUTPUT.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.RAMP_FIT_OUTPUT.value

    _testing_default: ClassVar = {"shape": (2, 8, 8)}

    model_config = ConfigDict(
        title="Ramp fit output schema",
    )

    meta: Annotated[
        _common.Common,
        Field(
            default_factory=_defaults.default_model_factory(_common.Common),
        ),
    ]
    slope: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.electron / u.s],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.electron / u.s),
            title="Segment-specific slope",
        ),
    ]
    sigslope: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.electron / u.s],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.electron / u.s),
            title="Sigma for segment-specific slope",
        ),
    ]
    yint: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.electron],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.electron),
            title="Segment-specific y-intercept",
        ),
    ]
    sigyint: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.electron],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.electron),
            title="Sigma for segment-specific y-intercept",
        ),
    ]
    pedestal: Annotated[
        _adaptors.AstropyQuantity[np.float32, 2, u.electron],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE[1:], u.electron),
            title="Pedestal array",
        ),
    ]
    weights: Annotated[
        _adaptors.NdArray[np.float32, 3],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.float32, _SHAPE),
            title="Weights for segment-specific fits",
        ),
    ]
    crmag: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.electron],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.electron),
            title="Approximate CR magnitudes",
        ),
    ]
    var_poisson: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, (u.electron / u.s) ** 2],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, (u.electron / u.s) ** 2),
            title="Variance due to poisson noise for segment-specific slope",
        ),
    ]
    var_rnoise: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, (u.electron / u.s) ** 2],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, (u.electron / u.s) ** 2),
            title="Variance due to read noise for segment-specific slope",
        ),
    ]

    def _check_shapes(self, shape: tuple[int] | None):
        _check.check_shape("slope", shape, value=self.slope)
        _check.check_shape("sigslope", shape, value=self.sigslope)
        _check.check_shape("yint", shape, value=self.yint)
        _check.check_shape("sigyint", shape, value=self.sigyint)
        _check.check_shape("pedestal", shape[1:], value=self.pedestal)
        _check.check_shape("weights", shape, value=self.weights)
        _check.check_shape("crmag", shape, value=self.crmag)
        _check.check_shape("var_poisson", shape, value=self.var_poisson)
        _check.check_shape("var_rnoise", shape, value=self.var_rnoise)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> RampFitOutputModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.slope.shape) != 3:
            raise ValueError(f"Expected 3-D data, got {self.slope.shape}")

        self._check_shapes(self.slope.shape)

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

            if isinstance(data, RampFitOutputModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                _check.fill_shape(data, "slope", shape, maker=_check.quantity_maker(u.electron / u.s, np.float32))
                _check.fill_shape(data, "sigslope", shape, maker=_check.quantity_maker(u.electron / u.s, np.float32))
                _check.fill_shape(data, "yint", shape, maker=_check.quantity_maker(u.electron, np.float32))
                _check.fill_shape(data, "sigyint", shape, maker=_check.quantity_maker(u.electron, np.float32))
                _check.fill_shape(data, "pedestal", shape[1:], maker=_check.quantity_maker(u.electron, np.float32))
                _check.fill_shape(data, "weights", shape, maker=_check.ndarray_maker(np.float32))
                _check.fill_shape(data, "crmag", shape, maker=_check.quantity_maker(u.electron, np.float32))
                _check.fill_shape(data, "var_poisson", shape, maker=_check.quantity_maker((u.electron / u.s) ** 2, np.float32))
                _check.fill_shape(data, "var_rnoise", shape, maker=_check.quantity_maker((u.electron / u.s) ** 2, np.float32))

        return data
