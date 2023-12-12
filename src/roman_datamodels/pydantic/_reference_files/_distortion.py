from typing import Annotated, Any, ClassVar, Literal

import astropy.units as u
from astropy.modeling.models import Shift
from pydantic import ConfigDict, Field

from .._adaptors import AstropyUnit
from .._core import BaseRomanRefModel
from .._defaults import default_constant_factory, default_model_factory
from .._uri import asdf_tag_uri, asdf_uri
from ._ref_common import RefCommon, RefOpticalElement, ref_type

__all__ = ["DistortionRefModel"]


class DistortionRefMeta(RefOpticalElement, RefCommon):
    reftype: Annotated[
        Literal[ref_type.DISTORTION],
        Field(
            default_factory=default_constant_factory(ref_type.DISTORTION.value),
            title="Reference file type",
        ),
    ]
    input_units: Annotated[
        AstropyUnit[u.pixel],
        Field(
            default_factory=default_constant_factory(u.pixel),
            title="Units of the detector coordinate inputs to this model.",
        ),
    ]
    output_units: Annotated[
        AstropyUnit[u.arcsec],
        Field(
            default_factory=default_constant_factory(u.arcsec),
            title="Output units of V2/V3 coordinates after the model is applied.",
        ),
    ]


class DistortionRefModel(BaseRomanRefModel):
    _uri: ClassVar = asdf_uri.DISTORTION.value
    _tag_uri: ClassVar = asdf_tag_uri.DISTORTION.value

    model_config = ConfigDict(
        title="Distortion reference schema",
    )

    meta: Annotated[
        DistortionRefMeta,
        Field(
            default_factory=default_model_factory(DistortionRefMeta),
            title="Distortion reference metadata",
        ),
    ]
    coordinate_transform: Annotated[
        Any,
        Field(
            default_factory=default_constant_factory(Shift(1) & Shift(2)),
            title="Distortion transform as an instance of astropy.modeling.Model.",
        ),
    ]
