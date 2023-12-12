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
    default_num_value,
    fill_shape,
    ndarray_factory,
)
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefOpticalElement, ref_type

__all__ = ["PixelareaRefModel"]


_SHAPE = (4096, 4096)


class Photometry(BaseRomanModel):
    pixelarea_steradians: Annotated[
        AstropyQuantity[np.float64, 0, u.steradian] | None,
        Field(
            default_factory=default_constant_factory(float(default_num_value.NONUM.value) * u.steradian),
            title="Nominal pixel area in steradians",
        ),
    ]
    pixelarea_arcsecsq: Annotated[
        AstropyQuantity[np.float64, 0, u.arcsec**2] | None,
        Field(
            default_factory=default_constant_factory(float(default_num_value.NONUM.value) * (u.arcsec**2)),
            title="Nominal pixel area in arcsec^2",
        ),
    ]


class PixelareaRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[ref_type.PIXELAREA],
        Field(
            default_factory=default_constant_factory(ref_type.PIXELAREA.value),
            title="Reference file type",
        ),
    ]
    photometry: Annotated[
        Photometry,
        Field(
            default_factory=default_model_factory(Photometry),
        ),
    ]


class PixelareaRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.PIXELAREA.value
    _tag_uri: ClassVar = asdf_tag_uri.PIXELAREA.value

    _testing_default: ClassVar = {"shape": (8, 8)}

    model_config = ConfigDict(
        title="Pixel area reference schema",
    )

    meta: Annotated[
        PixelareaRefMeta,
        Field(
            default_factory=default_model_factory(PixelareaRefMeta),
        ),
    ]
    data: Annotated[
        NdArray[np.float32, 2],
        Field(
            default_factory=default_ndarray_factory(np.float32, _SHAPE),
            title="Pixel area array",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        check_shape("data", shape, value=self.data)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> PixelareaRefModel:
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

            if isinstance(data, PixelareaRefModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "data", shape, factory=ndarray_factory(np.float32))

        return data
