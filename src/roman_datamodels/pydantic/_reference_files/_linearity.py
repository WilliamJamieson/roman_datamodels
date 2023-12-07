from typing import Annotated, ClassVar, Literal, NamedTuple

import astropy.units as u
import numpy as np
from pydantic import ConfigDict, Field

from .._adaptors import AstropyUnit, NdArray
from .._config import create_shape_config
from .._core import BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory, default_ndarray_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, reftype

__all__ = ["LinearityRefModel"]


class LinearityShapeData(NamedTuple):
    frames: int
    n_rows: int
    n_cols: int

    @property
    def detector(self) -> tuple[int, int]:
        return (self.n_rows, self.n_cols)


_SHAPE, linearity_ref_shape_context = create_shape_config(LinearityShapeData(2, 4096, 4096))


class LinearityRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.LINEARITY],
        Field(
            default_factory=default_constant_factory(reftype.LINEARITY.value),
            title="Reference file type",
        ),
    ]
    input_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            default_factory=default_constant_factory(u.DN),
            title="Units of the input to the linearity polynomial",
        ),
    ]
    output_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            default_factory=default_constant_factory(u.DN),
            title="Units of the output of the linearity polynomial.",
        ),
    ]


class LinearityRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.LINEARITY.value
    _tag_uri: ClassVar = asdf_tag_uri.LINEARITY.value

    model_config = ConfigDict(
        title="Linearity correction reference schema",
    )

    meta: Annotated[
        LinearityRefMeta,
        Field(
            default_factory=default_model_factory(LinearityRefMeta),
        ),
    ]
    coeffs: Annotated[
        NdArray[np.float32, 3],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float32),
            title="Linearly coefficients",
            description=(
                "Contains the coefficients of a polynomial to correct pixel "
                "values for classic non-linearity. Both the input to and "
                "output from the polynomial are in units of DN. The coefficients "
                "have units that contain various powers of DN."
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
