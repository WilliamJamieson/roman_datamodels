from typing import Annotated, ClassVar, NamedTuple

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity, NdArray
from .._config import create_shape_config
from .._core import BaseRomanDataModel
from .._defaults import default_model_factory, default_ndarray_factory, default_quantity_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._common import Common

__all__ = ["RampModel"]


class RampShapeData(NamedTuple):
    frames: int
    n_rows: int
    n_cols: int

    @property
    def boarder_lr(self) -> tuple[int, int, int]:
        return (self.frames, self.n_rows, 4)

    @property
    def boarder_tb(self) -> tuple[int, int, int]:
        return (self.frames, 4, self.n_cols)

    @property
    def dq_boarder_lr(self) -> tuple[int, int]:
        return (self.n_rows, 4)

    @property
    def dq_boarder_tb(self) -> tuple[int, int]:
        return (4, self.n_cols)

    @property
    def detector(self) -> tuple[int, int]:
        return (self.n_rows, self.n_cols)

    @property
    def amp33(self) -> tuple[int, int, int]:
        return (self.frames, self.n_rows, 128)


_SHAPE, ramp_shape_context = create_shape_config(RampShapeData(8, 4096, 4096))


class RampModel(BaseRomanDataModel):
    _uri: ClassVar = asdf_uri.RAMP.value
    _tag_uri: ClassVar = asdf_tag_uri.RAMP.value

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
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN),
            title="Science data, including the border reference pixels.",
        ),
    ]
    pixeldq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32, "detector"),
            title="2-D data quality array for all planes",
        ),
    ]
    groupdq: Annotated[
        NdArray[np.uint32, 3],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32),
            title="3-D data quality array (plane dq for each group)",
        ),
    ]
    err: Annotated[
        AstropyQuantity[np.float32, 3, (u.DN, u.electron)],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN),
            title="Error array containing the square root of the exposure-level combined variance",
        ),
    ]
    amp33: Annotated[
        AstropyQuantity[np.uint16, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.uint16, u.DN, "amp33"),
            title="Amp 33 reference pixel data",
        ),
    ]
    border_ref_pix_left: Annotated[
        AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN, "boarder_lr"),
            title="Original border reference pixels, on left (from viewers perspective).",
        ),
    ]
    border_ref_pix_right: Annotated[
        AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN, "boarder_lr"),
            title="Original border reference pixels, on right (from viewers perspective).",
        ),
    ]
    border_ref_pix_top: Annotated[
        AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN, "boarder_tb"),
            title="Original border reference pixels, on top.",
        ),
    ]
    border_ref_pix_bottom: Annotated[
        AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN, "boarder_tb"),
            title="Original border reference pixels, on bottom.",
        ),
    ]
    dq_border_ref_pix_left: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32, "dq_boarder_lr"),
            title="DQ for border reference pixels, on left (from viewers perspective).",
        ),
    ]
    dq_border_ref_pix_right: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32, "dq_boarder_lr"),
            title="DQ for border reference pixels, on right (from viewers perspective).",
        ),
    ]
    dq_border_ref_pix_top: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32, "dq_boarder_tb"),
            title="DQ for border reference pixels, on top.",
        ),
    ]
    dq_border_ref_pix_bottom: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32, "dq_boarder_tb"),
            title="DQ for border reference pixels, on bottom.",
        ),
    ]
