from __future__ import annotations

from typing import Annotated, Any, ClassVar

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from roman_datamodels.pydantic import _adaptors, _check, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

from . import _common

__all__ = ["RampModel"]


_SHAPE = (8, 4096, 4096)


class RampModel(_core.BaseRomanStepModel):
    _uri: ClassVar = uri.asdf_uri.RAMP.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.RAMP.value

    _testing_default: ClassVar = {"shape": (2, 8, 8)}

    model_config = ConfigDict(
        title="Ramp schema",
    )

    meta: Annotated[
        _common.Common,
        Field(
            default_factory=_defaults.default_model_factory(_common.Common),
        ),
    ]
    data: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, (u.DN, u.electron)],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.DN),
            title="Science data, including the border reference pixels.",
        ),
    ]
    pixeldq: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, _SHAPE[1:]),
            title="2-D data quality array for all planes",
        ),
    ]
    groupdq: Annotated[
        _adaptors.NdArray[np.uint32, 3],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, _SHAPE),
            title="3-D data quality array (plane dq for each group)",
        ),
    ]
    err: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, (u.DN, u.electron)],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.DN),
            title="Error array containing the square root of the exposure-level combined variance",
        ),
    ]
    amp33: Annotated[
        _adaptors.AstropyQuantity[np.uint16, 3, u.DN],
        Field(
            default_factory=_defaults.default_quantity_factory(np.uint16, (*_SHAPE[:2], 128), u.DN),
            title="Amp 33 reference pixel data",
        ),
    ]
    border_ref_pix_left: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, (*_SHAPE[:2], 4), u.DN),
            title="Original border reference pixels, on left (from viewers perspective).",
        ),
    ]
    border_ref_pix_right: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, (*_SHAPE[:2], 4), u.DN),
            title="Original border reference pixels, on right (from viewers perspective).",
        ),
    ]
    border_ref_pix_top: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, (_SHAPE[0], 4, _SHAPE[2]), u.DN),
            title="Original border reference pixels, on top.",
        ),
    ]
    border_ref_pix_bottom: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, (_SHAPE[0], 4, _SHAPE[2]), u.DN),
            title="Original border reference pixels, on bottom.",
        ),
    ]
    dq_border_ref_pix_left: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, (_SHAPE[1], 4)),
            title="DQ for border reference pixels, on left (from viewers perspective).",
        ),
    ]
    dq_border_ref_pix_right: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, (_SHAPE[1], 4)),
            title="DQ for border reference pixels, on right (from viewers perspective).",
        ),
    ]
    dq_border_ref_pix_top: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, (4, _SHAPE[2])),
            title="DQ for border reference pixels, on top.",
        ),
    ]
    dq_border_ref_pix_bottom: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, (4, _SHAPE[2])),
            title="DQ for border reference pixels, on bottom.",
        ),
    ]

    def _check_shapes(self, shape: tuple[int] | None):
        """Check all the shapes are consistent"""

        _shape = shape[1:]
        _n_groups = shape[0]

        _check.check_shape("data", _shape, n_shape=_n_groups, value=self.data)
        _check.check_shape("pixeldq", _shape, value=self.pixeldq)
        _check.check_shape("groupdq", _shape, n_shape=_n_groups, value=self.groupdq)
        _check.check_shape("err", _shape, n_shape=_n_groups, value=self.err)

        _check.check_shape("amp33", _shape, n_shape=_n_groups, border="amp33", fill_border=False, value=self.amp33)
        _check.check_shape(
            "border_ref_pix_left", _shape, n_shape=_n_groups, border="lr", fill_border=False, value=self.border_ref_pix_left
        )
        _check.check_shape(
            "border_ref_pix_right", _shape, n_shape=_n_groups, border="lr", fill_border=False, value=self.border_ref_pix_right
        )
        _check.check_shape(
            "border_ref_pix_top", _shape, n_shape=_n_groups, border="tb", fill_border=False, value=self.border_ref_pix_top
        )
        _check.check_shape(
            "border_ref_pix_bottom", _shape, n_shape=_n_groups, border="tb", fill_border=False, value=self.border_ref_pix_bottom
        )
        _check.check_shape("dq_border_ref_pix_left", _shape, border="lr", fill_border=False, value=self.dq_border_ref_pix_left)
        _check.check_shape("dq_border_ref_pix_right", _shape, border="lr", fill_border=False, value=self.dq_border_ref_pix_right)
        _check.check_shape("dq_border_ref_pix_top", _shape, border="tb", fill_border=False, value=self.dq_border_ref_pix_top)
        _check.check_shape(
            "dq_border_ref_pix_bottom", _shape, border="tb", fill_border=False, value=self.dq_border_ref_pix_bottom
        )

    @model_validator(mode="after")
    def _handle_data_shape(self) -> RampModel:
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

            _n_groups = shape[0] if shape is not None else None
            _shape = shape[1:] if shape is not None else None

            if isinstance(data, RampModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                _check.fill_shape(data, "data", _shape, n_shape=_n_groups, maker=_check.quantity_maker(u.DN, np.float32))
                _check.fill_shape(data, "pixeldq", _shape, maker=_check.ndarray_maker(np.uint32))
                _check.fill_shape(data, "groupdq", _shape, n_shape=_n_groups, maker=_check.ndarray_maker(np.uint32))
                _check.fill_shape(data, "err", _shape, n_shape=_n_groups, maker=_check.quantity_maker(u.DN, np.float32))
                _check.fill_shape(
                    data,
                    "amp33",
                    _shape,
                    n_shape=_n_groups,
                    fill_border=False,
                    border="amp33",
                    maker=_check.quantity_maker(u.DN, np.uint16),
                )
                _check.fill_shape(
                    data,
                    "border_ref_pix_left",
                    _shape,
                    n_shape=_n_groups,
                    border="lr",
                    fill_border=False,
                    maker=_check.quantity_maker(u.DN, np.float32),
                )
                _check.fill_shape(
                    data,
                    "border_ref_pix_right",
                    _shape,
                    n_shape=_n_groups,
                    border="lr",
                    fill_border=False,
                    maker=_check.quantity_maker(u.DN, np.float32),
                )
                _check.fill_shape(
                    data,
                    "border_ref_pix_top",
                    _shape,
                    n_shape=_n_groups,
                    border="tb",
                    fill_border=False,
                    maker=_check.quantity_maker(u.DN, np.float32),
                )
                _check.fill_shape(
                    data,
                    "border_ref_pix_bottom",
                    _shape,
                    n_shape=_n_groups,
                    border="tb",
                    fill_border=False,
                    maker=_check.quantity_maker(u.DN, np.float32),
                )
                _check.fill_shape(
                    data, "dq_border_ref_pix_left", _shape, border="lr", fill_border=False, maker=_check.ndarray_maker(np.uint32)
                )
                _check.fill_shape(
                    data, "dq_border_ref_pix_right", _shape, border="lr", fill_border=False, maker=_check.ndarray_maker(np.uint32)
                )
                _check.fill_shape(
                    data, "dq_border_ref_pix_top", _shape, border="tb", fill_border=False, maker=_check.ndarray_maker(np.uint32)
                )
                _check.fill_shape(
                    data,
                    "dq_border_ref_pix_bottom",
                    _shape,
                    border="tb",
                    fill_border=False,
                    maker=_check.ndarray_maker(np.uint32),
                )

        return data
