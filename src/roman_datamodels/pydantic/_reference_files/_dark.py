from __future__ import annotations

from typing import Annotated, Any, ClassVar, Literal

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from .._adaptors import AstropyQuantity, NdArray
from .._core import BaseRomanModel, BaseRomanRefModel
from .._defaults import (
    check_shape,
    default_constant_factory,
    default_model_factory,
    default_ndarray_factory,
    default_num_factory,
    default_quantity_factory,
    default_str_factory,
    fill_shape,
    ndarray_factory,
    quantity_factory,
)
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefExposureType, RefOpticalElement, ref_type

__all__ = ["DarkRefModel"]


_SHAPE = (2, 4096, 4096)


class Exposure(BaseRomanModel):
    ngroups: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(6),
            title="Number of groups in integration",
        ),
    ]
    nframes: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(8),
            title="Number of frames in group",
        ),
    ]
    groupgap: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(0),
            title="Number of frames dropped between groups",
        ),
    ]
    ma_table_name: Annotated[
        str,
        Field(
            default_factory=default_str_factory,
            title="Name of the multi-accumulation table used",
        ),
    ]
    ma_table_number: Annotated[
        int,
        Field(
            default_factory=default_num_factory,
            title="Number of the multi-accumulation table used",
        ),
    ]


class DarkRefMeta(RefOpticalElement, RefExposureType, RefCommon):
    reftype: Annotated[
        Literal[ref_type.DARK],
        Field(
            default_factory=default_constant_factory(ref_type.DARK.value),
            title="Reference file type",
        ),
    ]
    exposure: Annotated[
        Exposure,
        Field(
            default_factory=default_model_factory(Exposure),
        ),
    ]


class DarkRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.DARK.value
    _tag_uri: ClassVar = asdf_tag_uri.DARK.value

    _testing_default: ClassVar = {"shape": (2, 8, 8)}

    model_config = ConfigDict(
        title="Dark reference schema",
    )

    meta: Annotated[
        DarkRefMeta,
        Field(
            default_factory=default_model_factory(DarkRefMeta),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.DN),
            title="Dark current array",
            description=(
                "The dark current array represents the integrated number of counts "
                "due to the accumulation of dark current electrons in the pixels."
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
    dark_slope: Annotated[
        AstropyQuantity[np.float32, 2, u.DN / u.s],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE[1:], u.DN / u.s),
            title="Dark current slope array",
            description=(
                "The dark current slope array represents the slope of the "
                "integrated number of counts due to the accumulation of dark "
                "current electrons in the pixels for slope fitting purposes."
            ),
        ),
    ]
    dark_slope_error: Annotated[
        AstropyQuantity[np.float32, 2, u.DN / u.s],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE[1:], u.DN / u.s),
            title="Uncertainty in dark current slope array",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        _n_shape = shape[0]
        _shape = shape[1:]

        check_shape("data", _shape, n_shape=_n_shape, value=self.data)
        check_shape("dq", _shape, value=self.dq)
        check_shape("dark_slope", _shape, value=self.dark_slope)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> DarkRefModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.data.shape) != 3:
            raise ValueError(f"Expected 3-D data, got {self.data.shape}")

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
            if shape and len(shape) != 3:
                raise ValueError(f"Expected 3-D shape, got {shape}")

            _shape = shape[1:] if shape else None
            _n_shape = shape[0] if shape else None

            if isinstance(data, DarkRefModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "data", _shape, n_shape=_n_shape, factory=quantity_factory(u.DN, np.float32))
                fill_shape(data, "dq", _shape, factory=ndarray_factory(np.uint32))
                fill_shape(data, "dark_slope", _shape, factory=quantity_factory(u.DN / u.s, np.float32))

        return data
