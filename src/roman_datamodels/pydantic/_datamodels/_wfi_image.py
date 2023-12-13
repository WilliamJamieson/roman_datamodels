from __future__ import annotations

from typing import Annotated, Any, ClassVar

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from roman_datamodels.pydantic import _adaptors, _check, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

from . import _common

__all__ = ["ImageModel"]


_SHAPE = (4088, 4088)
_N_GROUPS = 8


class ImageMeta(_common.Common):
    photometry: Annotated[
        _common.Photometry,
        Field(
            default_factory=_defaults.default_model_factory(_common.Photometry),
            title="Photometry data",
        ),
    ]
    source_detection: Annotated[
        _common.SourceDetection | None,
        Field(
            default_factory=_defaults.default_model_factory(_common.SourceDetection),
            title="Source Detection data",
        ),
    ]


class ImageModel(_core.BaseRomanStepModel):
    _uri: ClassVar = uri.asdf_uri.WFI_IMAGE.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.WFI_IMAGE.value

    _optional_fields: ClassVar = ("var_flat",)

    _testing_default: ClassVar = {"shape": (8, 8), "n_groups": 2}

    model_config = ConfigDict(
        title="The schema for WFI Level 2 images.",
    )

    meta: Annotated[
        ImageMeta,
        Field(
            default_factory=_defaults.default_model_factory(ImageMeta),
        ),
    ]
    data: Annotated[
        _adaptors.AstropyQuantity[np.float32, 2, u.electron / u.s],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.electron / u.s),
            title="Science data, excluding border reference pixels.",
        ),
    ]
    dq: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, _SHAPE),
        ),
    ]
    err: Annotated[
        _adaptors.AstropyQuantity[np.float32, 2, u.electron / u.s],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.electron / u.s),
        ),
    ]
    var_poisson: Annotated[
        _adaptors.AstropyQuantity[np.float32, 2, (u.electron / u.s) ** 2],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, (u.electron / u.s) ** 2),
        ),
    ]
    var_rnoise: Annotated[
        _adaptors.AstropyQuantity[np.float32, 2, (u.electron / u.s) ** 2],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, (u.electron / u.s) ** 2),
        ),
    ]
    var_flat: Annotated[
        _adaptors.AstropyQuantity[np.float32, 2, (u.electron / u.s) ** 2],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, (u.electron / u.s) ** 2),
        ),
    ]
    amp33: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, (_N_GROUPS, _SHAPE[0] + 8, 128), u.DN),
            title="Amp 33 reference pixel data",
        ),
    ]
    border_ref_pix_left: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, (_N_GROUPS, _SHAPE[0] + 8, 4), u.DN),
            title="Original border reference pixels, on left (from viewers perspective).",
        ),
    ]
    border_ref_pix_right: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, (_N_GROUPS, _SHAPE[0] + 8, 4), u.DN),
            title="Original border reference pixels, on right (from viewers perspective).",
        ),
    ]
    border_ref_pix_top: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, (_N_GROUPS, 4, _SHAPE[1] + 8), u.DN),
            title="Original border reference pixels, on top.",
        ),
    ]
    border_ref_pix_bottom: Annotated[
        _adaptors.AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, (_N_GROUPS, 4, _SHAPE[1] + 8), u.DN),
            title="Original border reference pixels, on bottom.",
        ),
    ]
    dq_border_ref_pix_left: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, (_SHAPE[0] + 8, 4)),
            title="DQ for border reference pixels, on left (from viewers perspective).",
        ),
    ]
    dq_border_ref_pix_right: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, (_SHAPE[0] + 8, 4)),
            title="DQ for border reference pixels, on right (from viewers perspective).",
        ),
    ]
    dq_border_ref_pix_top: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, (4, _SHAPE[1] + 8)),
            title="DQ for border reference pixels, on top.",
        ),
    ]
    dq_border_ref_pix_bottom: Annotated[
        _adaptors.NdArray[np.uint32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, (4, _SHAPE[1] + 8)),
            title="DQ for border reference pixels, on bottom.",
        ),
    ]
    cal_logs: _common.CalLogs

    def _check_shapes(self, shape: tuple[int] | None, n_groups: int | None) -> None:
        """Check all the shapes are consistent"""

        _check.check_shape("data", shape, value=self.data)
        _check.check_shape("dq", shape, value=self.dq)
        _check.check_shape("err", shape, value=self.err)
        _check.check_shape("var_poisson", shape, value=self.var_poisson)
        _check.check_shape("var_rnoise", shape, value=self.var_rnoise)
        _check.check_shape("var_flat", shape, value=self.var_flat)

        _check.check_shape("amp33", shape, n_shape=n_groups, border="amp33", value=self.amp33)
        _check.check_shape("border_ref_pix_left", shape, n_shape=n_groups, border="lr", value=self.border_ref_pix_left)
        _check.check_shape("border_ref_pix_right", shape, n_shape=n_groups, border="lr", value=self.border_ref_pix_right)
        _check.check_shape("border_ref_pix_top", shape, n_shape=n_groups, border="tb", value=self.border_ref_pix_top)
        _check.check_shape("border_ref_pix_bottom", shape, n_shape=n_groups, border="tb", value=self.border_ref_pix_bottom)

        _check.check_shape("dq_border_ref_pix_left", shape, border="lr", value=self.dq_border_ref_pix_left)
        _check.check_shape("dq_border_ref_pix_right", shape, border="lr", value=self.dq_border_ref_pix_right)
        _check.check_shape("dq_border_ref_pix_top", shape, border="tb", value=self.dq_border_ref_pix_top)
        _check.check_shape("dq_border_ref_pix_bottom", shape, border="tb", value=self.dq_border_ref_pix_bottom)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> ImageModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.data.shape) != 2:
            raise ValueError(f"Expected 2-D data, got {self.data.shape}")

        if len(self.amp33.shape) != 3:
            raise ValueError(f"Expected 3-D amp33, got {self.amp33.shape}")

        self._check_shapes(self.data.shape, self.amp33.shape[0])

        return self

    @model_validator(mode="before")
    @classmethod
    def _handle_input_shape(cls, data: Any, info: ValidationInfo) -> Any:
        """Handle shaping the default input data"""
        context = info.context

        if context:
            if not set(context.keys()).issubset({"shape", "n_groups"}):
                raise ValueError(f"Only 'shape' and 'n_groups' are allowed in context, got {list(context.keys())}")

            shape = context.get("shape", None)
            if shape and len(shape) != 2:
                raise ValueError(f"Expected 2-D shape, got {shape}")

            n_groups = context.get("n_groups", None)
            if shape is not None and n_groups is None:
                raise ValueError("If shape is provided, n_groups must also be provided")

            if isinstance(data, ImageModel):
                data._check_shapes(shape, n_groups)

            elif isinstance(data, dict):
                _check.fill_shape(data, "data", shape, maker=_check.quantity_maker(u.electron / u.s, np.float32))
                _check.fill_shape(data, "dq", shape, maker=_check.ndarray_maker(np.uint32))
                _check.fill_shape(data, "err", shape, maker=_check.quantity_maker(u.electron / u.s, np.float32))
                _check.fill_shape(data, "var_poisson", shape, maker=_check.quantity_maker((u.electron / u.s) ** 2, np.float32))
                _check.fill_shape(data, "var_rnoise", shape, maker=_check.quantity_maker((u.electron / u.s) ** 2, np.float32))
                _check.fill_shape(data, "var_flat", shape, maker=_check.quantity_maker((u.electron / u.s) ** 2, np.float32))
                _check.fill_shape(
                    data, "amp33", shape, n_shape=n_groups, border="amp33", maker=_check.quantity_maker(u.DN, np.float32)
                )
                _check.fill_shape(
                    data,
                    "border_ref_pix_left",
                    shape,
                    n_shape=n_groups,
                    border="lr",
                    maker=_check.quantity_maker(u.DN, np.float32),
                )
                _check.fill_shape(
                    data,
                    "border_ref_pix_right",
                    shape,
                    n_shape=n_groups,
                    border="lr",
                    maker=_check.quantity_maker(u.DN, np.float32),
                )
                _check.fill_shape(
                    data,
                    "border_ref_pix_top",
                    shape,
                    n_shape=n_groups,
                    border="tb",
                    maker=_check.quantity_maker(u.DN, np.float32),
                )
                _check.fill_shape(
                    data,
                    "border_ref_pix_bottom",
                    shape,
                    n_shape=n_groups,
                    border="tb",
                    maker=_check.quantity_maker(u.DN, np.float32),
                )
                _check.fill_shape(data, "dq_border_ref_pix_left", shape, border="lr", maker=_check.ndarray_maker(np.uint32))
                _check.fill_shape(data, "dq_border_ref_pix_right", shape, border="lr", maker=_check.ndarray_maker(np.uint32))
                _check.fill_shape(data, "dq_border_ref_pix_top", shape, border="tb", maker=_check.ndarray_maker(np.uint32))
                _check.fill_shape(data, "dq_border_ref_pix_bottom", shape, border="tb", maker=_check.ndarray_maker(np.uint32))

        return data
