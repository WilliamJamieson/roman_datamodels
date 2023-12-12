from __future__ import annotations

from typing import Annotated, Any, ClassVar

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseRomanStepModel
from .._defaults import (
    check_shape,
    default_model_factory,
    default_ndarray_factory,
    default_quantity_factory,
    fill_shape,
    ndarray_factory,
    quantity_factory,
)
from .._uri import asdf_tag_uri, asdf_uri
from ._common import Common

__all__ = ["RampFitOutputModel"]


_SHAPE = (8, 4096, 4096)


class RampFitOutputModel(BaseRomanStepModel):
    _uri: ClassVar = asdf_uri.RAMP_FIT_OUTPUT.value
    _tag_uri: ClassVar = asdf_tag_uri.RAMP_FIT_OUTPUT.value

    _testing_default: ClassVar = {"shape": (2, 8, 8)}

    model_config = ConfigDict(
        title="Ramp fit output schema",
    )

    meta: Annotated[
        Common,
        Field(
            default_factory=default_model_factory(Common),
        ),
    ]
    slope: Annotated[
        AstropyQuantity[np.float32, 3, u.electron / u.s],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.electron / u.s),
            title="Segment-specific slope",
        ),
    ]
    sigslope: Annotated[
        AstropyQuantity[np.float32, 3, u.electron / u.s],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.electron / u.s),
            title="Sigma for segment-specific slope",
        ),
    ]
    yint: Annotated[
        AstropyQuantity[np.float32, 3, u.electron],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.electron),
            title="Segment-specific y-intercept",
        ),
    ]
    sigyint: Annotated[
        AstropyQuantity[np.float32, 3, u.electron],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.electron),
            title="Sigma for segment-specific y-intercept",
        ),
    ]
    pedestal: Annotated[
        AstropyQuantity[np.float32, 2, u.electron],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE[1:], u.electron),
            title="Pedestal array",
        ),
    ]
    weights: Annotated[
        NdArray[np.float32, 3],
        Field(
            default_factory=default_ndarray_factory(np.float32, _SHAPE),
            title="Weights for segment-specific fits",
        ),
    ]
    crmag: Annotated[
        AstropyQuantity[np.float32, 3, u.electron],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.electron),
            title="Approximate CR magnitudes",
        ),
    ]
    var_poisson: Annotated[
        AstropyQuantity[np.float32, 3, (u.electron / u.s) ** 2],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, (u.electron / u.s) ** 2),
            title="Variance due to poisson noise for segment-specific slope",
        ),
    ]
    var_rnoise: Annotated[
        AstropyQuantity[np.float32, 3, (u.electron / u.s) ** 2],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, (u.electron / u.s) ** 2),
            title="Variance due to read noise for segment-specific slope",
        ),
    ]

    def _check_shapes(self, shape: tuple[int] | None):
        check_shape("slope", shape, value=self.slope)
        check_shape("sigslope", shape, value=self.sigslope)
        check_shape("yint", shape, value=self.yint)
        check_shape("sigyint", shape, value=self.sigyint)
        check_shape("pedestal", shape[1:], value=self.pedestal)
        check_shape("weights", shape, value=self.weights)
        check_shape("crmag", shape, value=self.crmag)
        check_shape("var_poisson", shape, value=self.var_poisson)
        check_shape("var_rnoise", shape, value=self.var_rnoise)

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
                fill_shape(data, "slope", shape, factory=quantity_factory(u.electron / u.s, np.float32))
                fill_shape(data, "sigslope", shape, factory=quantity_factory(u.electron / u.s, np.float32))
                fill_shape(data, "yint", shape, factory=quantity_factory(u.electron, np.float32))
                fill_shape(data, "sigyint", shape, factory=quantity_factory(u.electron, np.float32))
                fill_shape(data, "pedestal", shape[1:], factory=quantity_factory(u.electron, np.float32))
                fill_shape(data, "weights", shape, factory=ndarray_factory(np.float32))
                fill_shape(data, "crmag", shape, factory=quantity_factory(u.electron, np.float32))
                fill_shape(data, "var_poisson", shape, factory=quantity_factory((u.electron / u.s) ** 2, np.float32))
                fill_shape(data, "var_rnoise", shape, factory=quantity_factory((u.electron / u.s) ** 2, np.float32))

        return data
