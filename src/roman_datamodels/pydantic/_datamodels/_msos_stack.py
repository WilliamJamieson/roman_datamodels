from __future__ import annotations

from typing import Annotated, Any, ClassVar

import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from roman_datamodels.pydantic import _adaptors, _check, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

from . import _common

__all__ = ["MsosStackModel"]


class MsosStackMeta(_common.Common):
    image_list: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
        ),
    ]


_SHAPE = (4088, 4088)


class MsosStackModel(_core.BaseRomanStepModel):
    _uri: ClassVar = uri.asdf_uri.MSOS_STACK.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.MSOS_STACK.value

    _testing_default: ClassVar = {"shape": (8, 8)}

    model_config = ConfigDict(
        title="MSOS Stack Level 3 schema",
    )

    meta: Annotated[
        MsosStackMeta,
        Field(
            default_factory=_defaults.default_model_factory(MsosStackMeta),
        ),
    ]
    data: Annotated[
        _adaptors.NdArray[np.float64, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.float64, _SHAPE),
            title="Flux data",
        ),
    ]
    uncertainty: Annotated[
        _adaptors.NdArray[np.float64, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.float64, _SHAPE),
            title="Uncertainty data",
        ),
    ]
    mask: Annotated[
        _adaptors.NdArray[np.uint8, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint8, _SHAPE),
            title="Mask data",
        ),
    ]
    coverage: Annotated[
        _adaptors.NdArray[np.uint8, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint8, _SHAPE),
            title="Coverage data",
        ),
    ]

    def _check_shapes(self, shape: tuple[int] | None):
        _check.check_shape("data", shape, value=self.data)
        _check.check_shape("uncertainty", shape, value=self.uncertainty)
        _check.check_shape("mask", shape, value=self.mask)
        _check.check_shape("coverage", shape, value=self.coverage)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> MsosStackModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.data.shape) != 2:
            raise ValueError(f"Expected 2-D data, got {self.data.shape}")

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
            if shape and len(shape) != 2:
                raise ValueError(f"Expected 2-D shape, got {shape}")

            if isinstance(data, MsosStackModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                _check.fill_shape(data, "data", shape, maker=_check.ndarray_maker(np.float64))
                _check.fill_shape(data, "uncertainty", shape, maker=_check.ndarray_maker(np.float64))
                _check.fill_shape(data, "mask", shape, maker=_check.ndarray_maker(np.uint8))
                _check.fill_shape(data, "coverage", shape, maker=_check.ndarray_maker(np.uint8))

        return data
