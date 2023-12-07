from typing import Annotated, ClassVar, NamedTuple, Optional

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity, NdArray
from .._config import create_shape_config
from .._core import BaseRomanDataModel
from .._defaults import default_model_factory, default_ndarray_factory, default_quantity_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._common import CalLogs, Common, Photometry, Resample

__all__ = ["MosaicModel"]


class MosaicShapeData(NamedTuple):
    n_rows: int
    n_cols: int
    n_images: int

    @property
    def detector(self) -> tuple[int, int]:
        return (self.n_rows, self.n_cols)

    @property
    def context(self) -> tuple[int, int, int]:
        return (self.n_images, self.n_rows, self.n_cols)


_SHAPE, mosaic_shape_context = create_shape_config(MosaicShapeData(4088, 4088, 2))


class MosaicMeta(Common):
    photometry: Annotated[
        Photometry,
        Field(
            default_factory=default_model_factory(Photometry),
        ),
    ]
    resample: Annotated[
        Optional[Resample],
        Field(
            default_factory=default_model_factory(Resample),
        ),
    ]


class MosaicModel(BaseRomanDataModel):
    _uri: ClassVar = asdf_uri.WFI_MOSAIC.value
    _tag_uri: ClassVar = asdf_tag_uri.WFI_MOSAIC.value

    model_config = ConfigDict(title="The schema for WFI Level 3 mosaics.")

    meta: Annotated[
        MosaicMeta,
        Field(
            default_factory=default_model_factory(MosaicMeta),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.float32, 2, u.electron / u.s],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron / u.s, "detector"),
            title="Science data, excluding border reference pixels.",
        ),
    ]
    err: Annotated[
        AstropyQuantity[np.float32, 2, u.electron / u.s],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron / u.s, "detector"),
        ),
    ]
    context: Annotated[
        NdArray[np.uint32, 3],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint32, "context"),
        ),
    ]
    weight: Annotated[
        NdArray[np.float32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float32, "detector"),
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
    cal_logs: CalLogs
