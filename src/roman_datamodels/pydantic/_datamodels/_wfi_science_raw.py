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

__all__ = ["ScienceRawModel"]


_SHAPE = (8, 4096, 4096)


class ScienceRawModel(BaseRomanStepModel):
    _uri: ClassVar = asdf_uri.WFI_SCIENCE_RAW.value
    _tag_uri: ClassVar = asdf_tag_uri.WFI_SCIENCE_RAW.value

    _optional_fields: ClassVar = ("resultantdq",)

    _testing_default = {"shape": (2, 8, 8)}

    model_config = ConfigDict(title="The schema for Level 1 WFI science data (both imaging and spectrographic).")

    meta: Annotated[
        Common,
        Field(
            default_factory=default_model_factory(Common),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.uint16, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(np.uint16, _SHAPE, u.DN),
            title="Science data, excluding border reference pixels.",
        ),
    ]
    amp33: Annotated[
        AstropyQuantity[np.uint16, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(np.uint16, _SHAPE, u.DN),
            title="Amp 33 reference pixel data",
        ),
    ]
    resultantdq: Annotated[
        NdArray[np.uint8, 3],
        Field(
            default_factory=default_ndarray_factory(np.uint8, _SHAPE),
            title="Optional 3-D data quality array (plane dq for each resultant",
        ),
    ]

    def _check_shapes(self, shape: tuple[int] | None) -> None:
        """Check all the shapes are consistent"""

        check_shape("data", shape, value=self.data)
        check_shape("amp33", shape, value=self.amp33)
        check_shape("resultantdq", shape, value=self.resultantdq)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> ScienceRawModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.data.shape) != 3:
            raise ValueError(f"Expected 3-D data, got {self.data.shape}")

        self._check_shapes(self.data.shape)

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

            if isinstance(data, ScienceRawModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "data", shape, factory=quantity_factory(u.DN, np.uint16))
                fill_shape(data, "amp33", shape, factory=quantity_factory(u.DN, np.uint16))
                fill_shape(data, "resultantdq", shape, factory=ndarray_factory(np.uint8))

            else:
                raise ValueError(f"Expected dict or ScienceRawModel, got {type(data)}")

        return data
