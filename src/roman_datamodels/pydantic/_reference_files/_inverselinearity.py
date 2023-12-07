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

__all__ = ["InverselinearityRefModel"]


class InverselinearityShapeData(NamedTuple):
    frames: int
    n_rows: int
    n_cols: int

    @property
    def detector(self) -> tuple[int, int]:
        return (self.n_rows, self.n_cols)


_SHAPE, inverselinearity_ref_shape_context = create_shape_config(InverselinearityShapeData(2, 4096, 4096))


class InverselinearityRefMeta(RefCommon):
    reftype: Annotated[
        Literal[reftype.INVERSELINEARITY],
        Field(
            default_factory=default_constant_factory(reftype.INVERSELINEARITY.value),
            title="Reference file type",
        ),
    ]
    input_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            default_factory=default_constant_factory(u.DN),
            title="Units of the input to the inverse linearity polynomial.",
        ),
    ]
    output_units: Annotated[
        AstropyUnit[u.DN],
        Field(
            default_factory=default_constant_factory(u.DN),
            title="Units of the output of the inverse linearity polynomial.",
        ),
    ]


class InverselinearityRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.INVERSELINEARITY.value
    _tag_uri: ClassVar = asdf_tag_uri.INVERSELINEARITY.value

    model_config = ConfigDict(
        title="Inverse linearity correction reference schema",
    )

    meta: Annotated[
        InverselinearityRefMeta,
        Field(
            default_factory=default_model_factory(InverselinearityRefMeta),
        ),
    ]
    coeffs: Annotated[
        NdArray[np.float32, 3],
        Field(
            default_factory=default_ndarray_factory(_SHAPE, np.float32),
            title="Inverse linearly coefficients",
            description=(
                "Contains the coefficients of a polynomial to add classic non-linearity "
                "to pixels. Both the input to and output from the polynomial are in units "
                "of DN. The coefficients have units that contain various powers of DN."
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
