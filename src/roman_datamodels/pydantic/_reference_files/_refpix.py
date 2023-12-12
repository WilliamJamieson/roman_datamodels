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
    ndarray_factory,
)
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, ref_type

__all__ = ["RefpixRefModel"]


_SHAPE = (32, 286721)


class RefpixRefMeta(RefCommon):
    reftype: Annotated[
        Literal[ref_type.REFPIX],
        Field(
            default_factory=default_constant_factory(ref_type.REFPIX.value),
            title="Reference file type",
        ),
    ]
    input_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            default_factory=default_constant_factory(u.DN),
            title="Units of the input to the input to the reference pixel correction.",
        ),
    ]
    output_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            default_factory=default_constant_factory(u.DN),
            title="Units of the output of the reference pixel correction.",
        ),
    ]


class RefpixRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.REFPIX.value
    _tag_uri: ClassVar = asdf_tag_uri.REFPIX.value

    _testing_default: ClassVar = {"shape": (12, 781)}  # Usable reduced shape due to fft shape requirements

    model_config = ConfigDict(
        title="Reference pixel correction reference schema",
    )

    meta: Annotated[
        RefpixRefMeta,
        Field(
            default_factory=default_model_factory(RefpixRefMeta),
        ),
    ]
    gamma: Annotated[
        NdArray[np.complex128, 2],
        Field(
            default_factory=default_ndarray_factory(np.complex128, _SHAPE),
            title="Left column correction coefficients",
        ),
    ]
    zeta: Annotated[
        NdArray[np.complex128, 2],
        Field(
            default_factory=default_ndarray_factory(np.complex128, _SHAPE),
            title="Right column correction coefficients",
        ),
    ]
    alpha: Annotated[
        NdArray[np.complex128, 2],
        Field(
            default_factory=default_ndarray_factory(np.complex128, _SHAPE),
            title="Reference amplifier (amp33) correction coefficients",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        check_shape("gamma", shape, value=self.gamma)
        check_shape("zeta", shape, value=self.zeta)
        check_shape("alpha", shape, value=self.alpha)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> RefpixRefModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.gamma.shape) != 2:
            raise ValueError(f"Expected 2-D data, got {self.gamma.shape}")

        self._check_shape(self.gamma.shape)

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

            if isinstance(data, RefpixRefModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "gamma", shape, factory=ndarray_factory(np.complex128))
                fill_shape(data, "zeta", shape, factory=ndarray_factory(np.complex128))
                fill_shape(data, "alpha", shape, factory=ndarray_factory(np.complex128))

        return data
