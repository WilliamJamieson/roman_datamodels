from typing import Annotated, ClassVar

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity, NdArray
from .._config import create_shape_config
from .._core import BaseRomanDataModel
from .._defaults import default_model_factory, default_ndarray_factory, default_quantity_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._common import Common

__all__ = ["RampFitOutputModel"]


_SHAPE, ramp_fit_output_shape_context = create_shape_config((8, 4096, 4096))


class RampFitOutputModel(BaseRomanDataModel):
    _uri: ClassVar = asdf_uri.RAMP_FIT_OUTPUT.value
    _tag_uri: ClassVar = asdf_tag_uri.RAMP_FIT_OUTPUT.value

    model_config = ConfigDict(
        title="Ramp fit output schema",
    )

    meta: Annotated[
        Common,
        Field(
            default_factory=default_model_factory(Common),
        ),
    ]
    slope: Annotated[
        AstropyQuantity[np.float32, 3, u.electron / u.s],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron / u.s),
            title="Segment-specific slope",
        ),
    ]
    sigslope: Annotated[
        AstropyQuantity[np.float32, 3, u.electron / u.s],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron / u.s),
            title="Sigma for segment-specific slope",
        ),
    ]
    yint: Annotated[
        AstropyQuantity[np.float32, 3, u.electron],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron),
            title="Segment-specific y-intercept",
        ),
    ]
    sigyint: Annotated[
        AstropyQuantity[np.float32, 3, u.electron],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron),
            title="Sigma for segment-specific y-intercept",
        ),
    ]
    pedestal: Annotated[
        AstropyQuantity[np.float32, 3, u.electron],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron),
            title="Pedestal array",
        ),
    ]
    weights: Annotated[
        NdArray[np.float32, 3],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float32),
            title="Weights for segment-specific fits",
        ),
    ]
    crmag: Annotated[
        AstropyQuantity[np.float32, 3, u.electron],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, u.electron),
            title="Approximate CR magnitudes",
        ),
    ]
    var_poisson: Annotated[
        AstropyQuantity[np.float32, 3, (u.electron / u.s) ** 2],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, (u.electron / u.s) ** 2),
            title="Variance due to poisson noise for segment-specific slope",
        ),
    ]
    var_rnoise: Annotated[
        AstropyQuantity[np.float32, 3, (u.electron / u.s) ** 2],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.float32, (u.electron / u.s) ** 2),
            title="Variance due to read noise for segment-specific slope",
        ),
    ]
