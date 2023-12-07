from typing import Annotated, ClassVar, Literal

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyUnit, NdArray
from .._config import create_shape_config
from .._core import BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_ndarray_factory
from .._enums import reftype
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon

__all__ = ["RefpixRefModel"]


_SHAPE, refpix_ref_shape_context = create_shape_config((32, 286721))


class RefpixRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.REFPIX],
        Field(
            default_factory=default_constant_factory(reftype.REFPIX.value),
            title="Reference file type",
        ),
    ]
    input_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            default_factory=default_constant_factory(u.DN),
            title="Units of the input to the input to the reference pixel correction.",
        ),
    ]
    output_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            default_factory=default_constant_factory(u.DN),
            title="Units of the output of the reference pixel correction.",
        ),
    ]


class RefpixRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.REFPIX.value
    _tag_uri: ClassVar = asdf_tag_uri.REFPIX.value

    model_config = ConfigDict(
        title="Reference pixel correction reference schema",
    )

    meta: Annotated[
        RefpixRefMeta,
        Field(
            default_factory=default_model_factory(RefpixRefMeta),
        ),
    ]
    gamma: Annotated[
        NdArray[np.complex128, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.complex128),
            title="Left column correction coefficients",
        ),
    ]
    zeta: Annotated[
        NdArray[np.complex128, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.complex128),
            title="Right column correction coefficients",
        ),
    ]
    alpha: Annotated[
        NdArray[np.complex128, 2],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.complex128),
            title="Reference amplifier (amp33) correction coefficients",
        ),
    ]
