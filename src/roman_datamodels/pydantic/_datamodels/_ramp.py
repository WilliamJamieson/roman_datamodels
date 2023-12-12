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

__all__ = ["RampModel"]


_SHAPE = (8, 4096, 4096)


class RampModel(BaseRomanStepModel):
    _uri: ClassVar = asdf_uri.RAMP.value
    _tag_uri: ClassVar = asdf_tag_uri.RAMP.value

    _testing_default: ClassVar = {"shape": (2, 8, 8)}

    model_config = ConfigDict(
        title="Ramp schema",
    )

    meta: Annotated[
        Common,
        Field(
            default_factory=default_model_factory(Common),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, 3, (u.DN, u.electron)],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.DN),
            title="Science data, including the border reference pixels.",
        ),
    ]
    pixeldq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(np.uint32, _SHAPE[1:]),
            title="2-D data quality array for all planes",
        ),
    ]
    groupdq: Annotated[
        NdArray[np.uint32, 3],
        Field(
            default_factory=default_ndarray_factory(np.uint32, _SHAPE),
            title="3-D data quality array (plane dq for each group)",
        ),
    ]
    err: Annotated[
        AstropyQuantity[np.float32, 3, (u.DN, u.electron)],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.DN),
            title="Error array containing the square root of the exposure-level combined variance",
        ),
    ]
    amp33: Annotated[
        AstropyQuantity[np.uint16, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(np.uint16, (*_SHAPE[:2], 128), u.DN),
            title="Amp 33 reference pixel data",
        ),
    ]
    border_ref_pix_left: Annotated[
        AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(np.float32, (*_SHAPE[:2], 4), u.DN),
            title="Original border reference pixels, on left (from viewers perspective).",
        ),
    ]
    border_ref_pix_right: Annotated[
        AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(np.float32, (*_SHAPE[:2], 4), u.DN),
            title="Original border reference pixels, on right (from viewers perspective).",
        ),
    ]
    border_ref_pix_top: Annotated[
        AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(np.float32, (_SHAPE[0], 4, _SHAPE[2]), u.DN),
            title="Original border reference pixels, on top.",
        ),
    ]
    border_ref_pix_bottom: Annotated[
        AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(np.float32, (_SHAPE[0], 4, _SHAPE[2]), u.DN),
            title="Original border reference pixels, on bottom.",
        ),
    ]
    dq_border_ref_pix_left: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(np.uint32, (_SHAPE[1], 4)),
            title="DQ for border reference pixels, on left (from viewers perspective).",
        ),
    ]
    dq_border_ref_pix_right: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(np.uint32, (_SHAPE[1], 4)),
            title="DQ for border reference pixels, on right (from viewers perspective).",
        ),
    ]
    dq_border_ref_pix_top: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(np.uint32, (4, _SHAPE[2])),
            title="DQ for border reference pixels, on top.",
        ),
    ]
    dq_border_ref_pix_bottom: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(np.uint32, (4, _SHAPE[2])),
            title="DQ for border reference pixels, on bottom.",
        ),
    ]

    def _check_shapes(self, shape: tuple[int] | None):
        """Check all the shapes are consistent"""

        _shape = shape[1:]
        _n_groups = shape[0]

        check_shape("data", _shape, n_shape=_n_groups, value=self.data)
        check_shape("pixeldq", _shape, value=self.pixeldq)
        check_shape("groupdq", _shape, n_shape=_n_groups, value=self.groupdq)
        check_shape("err", _shape, n_shape=_n_groups, value=self.err)

        check_shape("amp33", _shape, n_shape=_n_groups, border="amp33", fill_border=False, value=self.amp33)
        check_shape(
            "border_ref_pix_left", _shape, n_shape=_n_groups, border="lr", fill_border=False, value=self.border_ref_pix_left
        )
        check_shape(
            "border_ref_pix_right", _shape, n_shape=_n_groups, border="lr", fill_border=False, value=self.border_ref_pix_right
        )
        check_shape(
            "border_ref_pix_top", _shape, n_shape=_n_groups, border="tb", fill_border=False, value=self.border_ref_pix_top
        )
        check_shape(
            "border_ref_pix_bottom", _shape, n_shape=_n_groups, border="tb", fill_border=False, value=self.border_ref_pix_bottom
        )
        check_shape("dq_border_ref_pix_left", _shape, border="lr", fill_border=False, value=self.dq_border_ref_pix_left)
        check_shape("dq_border_ref_pix_right", _shape, border="lr", fill_border=False, value=self.dq_border_ref_pix_right)
        check_shape("dq_border_ref_pix_top", _shape, border="tb", fill_border=False, value=self.dq_border_ref_pix_top)
        check_shape("dq_border_ref_pix_bottom", _shape, border="tb", fill_border=False, value=self.dq_border_ref_pix_bottom)

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
                fill_shape(data, "data", _shape, n_shape=_n_groups, factory=quantity_factory(u.DN, np.float32))
                fill_shape(data, "pixeldq", _shape, factory=ndarray_factory(np.uint32))
                fill_shape(data, "groupdq", _shape, n_shape=_n_groups, factory=ndarray_factory(np.uint32))
                fill_shape(data, "err", _shape, n_shape=_n_groups, factory=quantity_factory(u.DN, np.float32))
                fill_shape(
                    data,
                    "amp33",
                    _shape,
                    n_shape=_n_groups,
                    fill_border=False,
                    border="amp33",
                    factory=quantity_factory(u.DN, np.uint16),
                )
                fill_shape(
                    data,
                    "border_ref_pix_left",
                    _shape,
                    n_shape=_n_groups,
                    border="lr",
                    fill_border=False,
                    factory=quantity_factory(u.DN, np.float32),
                )
                fill_shape(
                    data,
                    "border_ref_pix_right",
                    _shape,
                    n_shape=_n_groups,
                    border="lr",
                    fill_border=False,
                    factory=quantity_factory(u.DN, np.float32),
                )
                fill_shape(
                    data,
                    "border_ref_pix_top",
                    _shape,
                    n_shape=_n_groups,
                    border="tb",
                    fill_border=False,
                    factory=quantity_factory(u.DN, np.float32),
                )
                fill_shape(
                    data,
                    "border_ref_pix_bottom",
                    _shape,
                    n_shape=_n_groups,
                    border="tb",
                    fill_border=False,
                    factory=quantity_factory(u.DN, np.float32),
                )
                fill_shape(
                    data, "dq_border_ref_pix_left", _shape, border="lr", fill_border=False, factory=ndarray_factory(np.uint32)
                )
                fill_shape(
                    data, "dq_border_ref_pix_right", _shape, border="lr", fill_border=False, factory=ndarray_factory(np.uint32)
                )
                fill_shape(
                    data, "dq_border_ref_pix_top", _shape, border="tb", fill_border=False, factory=ndarray_factory(np.uint32)
                )
                fill_shape(
                    data, "dq_border_ref_pix_bottom", _shape, border="tb", fill_border=False, factory=ndarray_factory(np.uint32)
                )

        return data
