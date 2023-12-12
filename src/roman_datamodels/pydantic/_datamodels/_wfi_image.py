from typing import Annotated, ClassVar, NamedTuple, Optional

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity, NdArray
from .._config import create_shape_config
from .._core import BaseRomanStepModel
from .._defaults import default_model_factory, default_ndarray_factory, default_quantity_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._common import Common, Photometry, SourceDetection

__all__ = ["ImageModel"]


class ImageShapeData(NamedTuple):
    n_rows: int
    n_cols: int
    n_groups: int

    @property
    def detector(self) -> tuple[int, int]:
        return (self.n_rows, self.n_cols)

    @property
    def boarder_lr(self) -> tuple[int, int, int]:
        return (self.n_groups, self.n_rows + 8, 4)

    @property
    def boarder_tb(self) -> tuple[int, int, int]:
        return (self.n_groups, 4, self.n_cols + 8)

    @property
    def dq_boarder_lr(self) -> tuple[int, int]:
        return (self.n_rows + 8, 4)

    @property
    def dq_boarder_tb(self) -> tuple[int, int]:
        return (4, self.n_cols + 8)

    @property
    def amp33(self) -> tuple[int, int, int]:
        return (self.n_groups, self.n_rows + 8, 128)


_SHAPE, image_shape_context = create_shape_config(ImageShapeData(4088, 4088, 8))


class ImageMeta(Common):
    photometry: Annotated[
        Photometry,
        Field(
            default_factory=default_model_factory(Photometry),
            title="Photometry data",
        ),
    ]
    source_detection: Annotated[
        Optional[SourceDetection],
        Field(
            default_factory=default_model_factory(SourceDetection),
            title="Source Detection data",
        ),
    ]


class ImageModel(BaseRomanStepModel):
    _uri: ClassVar = asdf_uri.WFI_IMAGE.value
    _tag_uri: ClassVar = asdf_tag_uri.WFI_IMAGE.value

    _optional_fields: ClassVar = ("var_flat",)

    model_config = ConfigDict(
        title="The schema for WFI Level 2 images.",
    )

    meta: Annotated[
        ImageMeta,
        Field(
            default_factory=default_model_factory(ImageMeta),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, 2, u.electron / u.s],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron / u.s, "detector"),
            title="Science data, excluding border reference pixels.",
        ),
    ]
    dq: Annotated[
        NdArray[np.uint32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32, "detector"),
        ),
    ]
    err: Annotated[
        AstropyQuantity[np.float32, 2, u.electron / u.s],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron / u.s, "detector"),
        ),
    ]
    var_poisson: Annotated[
        AstropyQuantity[np.float32, 2, (u.electron / u.s) ** 2],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, (u.electron / u.s) ** 2, "detector"),
        ),
    ]
    var_rnoise: Annotated[
        AstropyQuantity[np.float32, 2, (u.electron / u.s) ** 2],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, (u.electron / u.s) ** 2, "detector"),
        ),
    ]
    var_flat: Annotated[
        AstropyQuantity[np.float32, 2, (u.electron / u.s) ** 2],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, (u.electron / u.s) ** 2, "detector"),
        ),
    ]
    amp33: Annotated[
        AstropyQuantity[np.float32, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.DN, "amp33"),
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
