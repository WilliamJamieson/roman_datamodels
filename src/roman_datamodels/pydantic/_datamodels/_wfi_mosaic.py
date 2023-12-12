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
from ._common import CalLogs, Common, Photometry, Resample

__all__ = ["MosaicModel"]


_SHAPE = (4088, 4088)
_N_IMAGES = 2


class MosaicMeta(Common):
    photometry: Annotated[
        Photometry,
        Field(
            default_factory=default_model_factory(Photometry),
        ),
    ]
    resample: Annotated[
        Resample | None,
        Field(
            default_factory=default_model_factory(Resample),
        ),
    ]


class MosaicModel(BaseRomanStepModel):
    _uri: ClassVar = asdf_uri.WFI_MOSAIC.value
    _tag_uri: ClassVar = asdf_tag_uri.WFI_MOSAIC.value

    model_config = ConfigDict(title="The schema for WFI Level 3 mosaics.")

    _testing_default = {"shape": (8, 8), "n_images": 2}

    meta: Annotated[
        MosaicMeta,
        Field(
            default_factory=default_model_factory(MosaicMeta),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, 2, u.electron / u.s],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.electron / u.s),
            title="Science data, excluding border reference pixels.",
        ),
    ]
    err: Annotated[
        AstropyQuantity[np.float32, 2, u.electron / u.s],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, u.electron / u.s),
        ),
    ]
    context: Annotated[
        NdArray[np.uint32, 3],
        Field(
            default_factory=default_ndarray_factory(np.uint32, (_N_IMAGES, *_SHAPE)),
        ),
    ]
    weight: Annotated[
        NdArray[np.float32, 2],
        Field(
            default_factory=default_ndarray_factory(np.float32, _SHAPE),
        ),
    ]
    var_poisson: Annotated[
        AstropyQuantity[np.float32, 2, (u.electron / u.s) ** 2],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, (u.electron / u.s) ** 2),
        ),
    ]
    var_rnoise: Annotated[
        AstropyQuantity[np.float32, 2, (u.electron / u.s) ** 2],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, (u.electron / u.s) ** 2),
        ),
    ]
    var_flat: Annotated[
        AstropyQuantity[np.float32, 2, (u.electron / u.s) ** 2],
        Field(
            default_factory=default_quantity_factory(np.float32, _SHAPE, (u.electron / u.s) ** 2),
        ),
    ]
    cal_logs: CalLogs

    def _check_shapes(self, shape: tuple[int] | None, n_images: int | None) -> None:
        """Check all the shapes are consistent"""

        check_shape("data", shape, value=self.data)
        check_shape("err", shape, value=self.err)
        check_shape("weight", shape, value=self.weight)
        check_shape("var_poisson", shape, value=self.var_poisson)
        check_shape("var_rnoise", shape, value=self.var_rnoise)
        check_shape("var_flat", shape, value=self.var_flat)

        check_shape("context", shape, n_shape=n_images, value=self.context)

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
                fill_shape(data, "data", shape, factory=quantity_factory(u.electron / u.s, np.float32))
                fill_shape(data, "err", shape, factory=quantity_factory(u.electron / u.s, np.float32))
                fill_shape(data, "weight", shape, factory=ndarray_factory(np.float32))
                fill_shape(data, "var_poisson", shape, factory=quantity_factory((u.electron / u.s) ** 2, np.float32))
                fill_shape(data, "var_rnoise", shape, factory=quantity_factory((u.electron / u.s) ** 2, np.float32))
                fill_shape(data, "var_flat", shape, factory=quantity_factory((u.electron / u.s) ** 2, np.float32))
                fill_shape(data, "context", shape, n_shape=n_images, factory=ndarray_factory(np.uint32))

            else:
                raise ValueError(f"Expected dict or MosaicModel, got {type(data)}")

        return data
