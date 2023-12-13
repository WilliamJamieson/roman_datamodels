from __future__ import annotations

from typing import Annotated, Any, ClassVar

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from roman_datamodels.pydantic import _adaptors, _check, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

from . import _common

__all__ = ["MosaicModel"]


_SHAPE = (4088, 4088)
_N_IMAGES = 2


class MosaicMeta(_common.Common):
    photometry: Annotated[
        _common.Photometry,
        Field(
            default_factory=_defaults.default_model_factory(_common.Photometry),
        ),
    ]
    resample: Annotated[
        _common.Resample | None,
        Field(
            default_factory=_defaults.default_model_factory(_common.Resample),
        ),
    ]


class MosaicModel(_core.BaseRomanStepModel):
    _uri: ClassVar = uri.asdf_uri.WFI_MOSAIC.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.WFI_MOSAIC.value

    model_config = ConfigDict(title="The schema for WFI Level 3 mosaics.")

    _testing_default = {"shape": (8, 8), "n_images": 2}

    meta: Annotated[
        MosaicMeta,
        Field(
            default_factory=_defaults.default_model_factory(MosaicMeta),
        ),
    ]
    data: Annotated[
        _adaptors.AstropyQuantity[np.float32, 2, u.electron / u.s],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.electron / u.s),
            title="Science data, excluding border reference pixels.",
        ),
    ]
    err: Annotated[
        _adaptors.AstropyQuantity[np.float32, 2, u.electron / u.s],
        Field(
            default_factory=_defaults.default_quantity_factory(np.float32, _SHAPE, u.electron / u.s),
        ),
    ]
    context: Annotated[
        _adaptors.NdArray[np.uint32, 3],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.uint32, (_N_IMAGES, *_SHAPE)),
        ),
    ]
    weight: Annotated[
        _adaptors.NdArray[np.float32, 2],
        Field(
            default_factory=_defaults.default_ndarray_factory(np.float32, _SHAPE),
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
    cal_logs: _common.CalLogs

    def _check_shapes(self, shape: tuple[int] | None, n_images: int | None) -> None:
        """Check all the shapes are consistent"""

        _check.check_shape("data", shape, value=self.data)
        _check.check_shape("err", shape, value=self.err)
        _check.check_shape("weight", shape, value=self.weight)
        _check.check_shape("var_poisson", shape, value=self.var_poisson)
        _check.check_shape("var_rnoise", shape, value=self.var_rnoise)
        _check.check_shape("var_flat", shape, value=self.var_flat)

        _check.check_shape("context", shape, n_shape=n_images, value=self.context)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> MosaicModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.data.shape) != 2:
            raise ValueError(f"Expected 2-D data, got {self.data.shape}")

        if len(self.context.shape) != 3:
            raise ValueError(f"Expected 3-D context, got {self.context.shape}")

        self._check_shapes(self.data.shape, self.context.shape[0])

        return self

    @model_validator(mode="before")
    @classmethod
    def _handle_input_shape(cls, data: Any, info: ValidationInfo) -> Any:
        """Handle shaping the default input data"""
        context = info.context

        if context:
            if not set(context.keys()).issubset({"shape", "n_images"}):
                raise ValueError(f"Only 'shape' and 'n_images' are allowed in context, got {list(context.keys())}")

            shape = context.get("shape", None)
            if shape and len(shape) != 2:
                raise ValueError(f"Expected 2-D shape, got {shape}")

            n_images = context.get("n_images", None)
            if shape is not None and n_images is None:
                raise ValueError("If shape is provided, n_images must also be provided")

            if isinstance(data, MosaicModel):
                data._check_shapes(shape, n_images)

            elif isinstance(data, dict):
                _check.fill_shape(data, "data", shape, maker=_check.quantity_maker(u.electron / u.s, np.float32))
                _check.fill_shape(data, "err", shape, maker=_check.quantity_maker(u.electron / u.s, np.float32))
                _check.fill_shape(data, "weight", shape, maker=_check.ndarray_maker(np.float32))
                _check.fill_shape(data, "var_poisson", shape, maker=_check.quantity_maker((u.electron / u.s) ** 2, np.float32))
                _check.fill_shape(data, "var_rnoise", shape, maker=_check.quantity_maker((u.electron / u.s) ** 2, np.float32))
                _check.fill_shape(data, "var_flat", shape, maker=_check.quantity_maker((u.electron / u.s) ** 2, np.float32))
                _check.fill_shape(data, "context", shape, n_shape=n_images, maker=_check.ndarray_maker(np.uint32))

            else:
                raise ValueError(f"Expected dict or MosaicModel, got {type(data)}")

        return data
