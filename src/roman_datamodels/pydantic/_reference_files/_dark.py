from typing import Annotated, ClassVar, Literal, NamedTuple

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity, NdArray
from .._config import create_shape_config
from .._core import BaseRomanModel, BaseRomanRefModel
from .._defaults import (
    default_constant_factory,
    default_model_factory,
    default_ndarray_factory,
    default_num_value,
    default_quantity_factory,
    default_str_value,
)
from .._enums import reftype
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefExposureType, RefOpticalElement

__all__ = ["DarkRefModel"]


class DarkShapeData(NamedTuple):
    frames: int
    n_rows: int
    n_cols: int

    @property
    def detector(self) -> tuple[int, int]:
        return (self.n_rows, self.n_cols)


_SHAPE, dark_ref_shape_context = create_shape_config(DarkShapeData(2, 4096, 4096))


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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Name of the multi-accumulation table used",
        ),
    ]
    ma_table_number: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Number of the multi-accumulation table used",
        ),
    ]


class DarkRefMeta(RefOpticalElement, RefExposureType, RefCommon):
    reftype: Annotated[
        Literal[reftype.DARK],
        Field(
            default_factory=default_constant_factory(reftype.DARK.value),
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
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN),
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
            default_factory=default_ndarray_factory(_SHAPE, np.uint32, "detector"),
            title="2-D data quality array for all planes",
        ),
    ]
    dark_slope: Annotated[
        AstropyQuantity[np.float32, 2, u.DN / u.s],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN / u.s, "detector"),
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
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN / u.s, "detector"),
            title="Uncertainty in dark current slope array",
        ),
    ]
