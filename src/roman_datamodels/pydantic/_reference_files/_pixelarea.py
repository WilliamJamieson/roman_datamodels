from typing import Annotated, ClassVar, Literal, Optional

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity, NdArray
from .._config import create_shape_config
from .._core import BaseRomanModel, BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_ndarray_factory, default_num_value
from .._enums import reftype
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefOpticalElement

__all__ = ["PixelareaRefModel"]


_SHAPE, pixelarea_ref_shape_context = create_shape_config((4096, 4096))


class Photometry(BaseRomanModel):
    pixelarea_steradians: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.steradian]],
        Field(
            default_factory=default_constant_factory(float(default_num_value.NONUM.value) * u.steradian),
            title="Nominal pixel area in steradians",
        ),
    ]
    pixelarea_arcsecsq: Annotated[
        Optional[AstropyQuantity[np.float64, 0, u.arcsec**2]],
        Field(
            default_factory=default_constant_factory(float(default_num_value.NONUM.value) * (u.arcsec**2)),
            title="Nominal pixel area in arcsec^2",
        ),
    ]


class PixelareaRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[reftype.PIXELAREA],
        Field(
            default_factory=default_constant_factory(reftype.PIXELAREA.value),
            title="Reference file type",
        ),
    ]
    photometry: Annotated[
        Photometry,
        Field(
            default_factory=default_model_factory(Photometry),
        ),
    ]


class PixelareaRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.PIXELAREA.value
    _tag_uri: ClassVar = asdf_tag_uri.PIXELAREA.value

    model_config = ConfigDict(
        title="Pixel area reference schema",
    )

    meta: Annotated[
        PixelareaRefMeta,
        Field(
            default_factory=default_model_factory(PixelareaRefMeta),
        ),
    ]
    data: Annotated[
        NdArray[np.float32, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float32),
            title="Pixel area array",
        ),
    ]
