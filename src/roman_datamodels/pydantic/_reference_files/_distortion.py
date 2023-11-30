from typing import Annotated, Any, Literal

import astropy.units as u
from pydantic import Field

from .._adaptors import AstropyUnit
from .._core import BaseRomanRefModel
from .._enums import reftype
from ._ref_common import RefCommon, RefOpticalElement

__all__ = ["DistortionRefModel"]


class DistortionRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[reftype.DISTORTION],
        Field(
            json_schema_extra={
                "title": "Reference file type",
            },
        ),
    ]
    input_units: Annotated[
        AstropyUnit[u.pixel],
        Field(
            json_schema_extra={
                "title": "Units of the detector coordinate inputs to this model.",
            },
        ),
    ]
    output_units: Annotated[
        AstropyUnit[u.arcsec],
        Field(
            json_schema_extra={
                "title": "Output units of V2/V3 coordinates after the model is applied.",
            },
        ),
    ]


class DistortionRefModel(BaseRomanRefModel):
    meta: Annotated[
        DistortionRefMeta,
        Field(
            json_schema_extra={
                "title": "Distortion reference metadata",
            },
        ),
    ]
    coordinate_transform: Annotated[
        Any,
        Field(
            json_schema_extra={"title": "Distortion transform as an instance of astropy.modeling.Model."},
        ),
    ]
