from typing import Annotated, ClassVar

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity, NdArray
from .._config import create_shape_config
from .._core import BaseRomanStepModel
from .._defaults import default_model_factory, default_ndarray_factory, default_quantity_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._common import Common

__all__ = ["ScienceRawModel"]


_SHAPE, science_raw_shape_context = create_shape_config((8, 4096, 4096))


class ScienceRawModel(BaseRomanStepModel):
    _uri: ClassVar = asdf_uri.WFI_SCIENCE_RAW.value
    _tag_uri: ClassVar = asdf_tag_uri.WFI_SCIENCE_RAW.value

    _optional_fields: ClassVar = ("resultantdq",)

    model_config = ConfigDict(title="The schema for Level 1 WFI science data (both imaging and spectrographic).")

    meta: Annotated[
        Common,
        Field(
            default_factory=default_model_factory(Common),
        ),
    ]
    data: Annotated[
        AstropyQuantity[np.uint16, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.uint16, u.DN),
            title="Science data, excluding border reference pixels.",
        ),
    ]
    amp33: Annotated[
        AstropyQuantity[np.uint16, 3, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.uint16, u.DN),
            title="Amp 33 reference pixel data",
        ),
    ]
    resultantdq: Annotated[
        NdArray[np.uint8, 3],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.uint8),
            title="Optional 3-D data quality array (plane dq for each resultant",
        ),
    ]
