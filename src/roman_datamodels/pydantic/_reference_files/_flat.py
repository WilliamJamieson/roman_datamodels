from __future__ import annotations

from typing import Annotated, Any, ClassVar, Literal

import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from roman_datamodels.pydantic import _adaptors, _check, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

from . import _ref_common

__all__ = ["FlatRefModel"]


_SHAPE = (4096, 4096)


class FlatRefMeta(_ref_common.RefOpticalElement, _ref_common.RefCommon):
    reftype: Annotated[
        Literal[_ref_common.ref_type.FLAT],
        Field(
            default_factory=_defaults.default_constant_factory(_ref_common.ref_type.FLAT.value),
            title="Reference file type",
        ),
    ]


class FlatRefModel(_core.BaseRomanRefModel):
    _uri: ClassVar = uri.asdf_uri.FLAT.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.FLAT.value

    _testing_default: ClassVar = {"shape": (8, 8)}

    model_config = ConfigDict(
        title="Flat reference schema",
    )

    meta: Annotated[
        FlatRefMeta,
        Field(
            default_factory=_defaults.default_model_factory(FlatRefMeta),
        ),
    ]
    data: Annotated[
        _adaptors.NdArray[np.float32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.float32, _SHAPE),
            title="Flat data array",
        ),
    ]
    dq: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, _SHAPE),
            title="Data quality array",
        ),
    ]
    err: Annotated[
        _adaptors.NdArray[np.float32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.float32, _SHAPE),
            title="Error array",
        ),
    ]

    def _check_shape(self, shape: tuple[int] | None) -> None:
        _check.check_shape("data", shape, value=self.data)
        _check.check_shape("dq", shape, value=self.dq)
        _check.check_shape("err", shape, value=self.err)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> FlatRefModel:
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

            if isinstance(data, FlatRefModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                _check.fill_shape(data, "data", shape, maker=_check.ndarray_maker(np.float32))
                _check.fill_shape(data, "dq", shape, maker=_check.ndarray_maker(np.uint32))
                _check.fill_shape(data, "err", shape, maker=_check.ndarray_maker(np.float32))

        return data
