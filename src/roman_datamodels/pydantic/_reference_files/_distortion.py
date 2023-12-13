from typing import Annotated, Any, ClassVar, Literal

import astropy.units as u
from astropy.modeling.models import Shift
from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _adaptors, _core, _defaults
from roman_datamodels.pydantic import _uri as uri

from . import _ref_common

__all__ = ["DistortionRefModel"]


class DistortionRefMeta(_ref_common.RefOpticalElement, _ref_common.RefCommon):
    reftype: Annotated[
        Literal[_ref_common.ref_type.DISTORTION],
        Field(
            default_factory=_defaults.default_constant_factory(_ref_common.ref_type.DISTORTION.value),
            title="Reference file type",
        ),
    ]
    input_units: Annotated[
        _adaptors.AstropyUnit[u.pixel],
        Field(
            default_factory=_defaults.default_constant_factory(u.pixel),
            title="Units of the detector coordinate inputs to this model.",
        ),
    ]
    output_units: Annotated[
        _adaptors.AstropyUnit[u.arcsec],
        Field(
            default_factory=_defaults.default_constant_factory(u.arcsec),
            title="Output units of V2/V3 coordinates after the model is applied.",
        ),
    ]


class DistortionRefModel(_core.BaseRomanRefModel):
    _uri: ClassVar = uri.asdf_uri.DISTORTION.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.DISTORTION.value

    model_config = ConfigDict(
        title="Distortion reference schema",
    )

    meta: Annotated[
        DistortionRefMeta,
        Field(
            default_factory=_defaults.default_model_factory(DistortionRefMeta),
            title="Distortion reference metadata",
        ),
    ]
    coordinate_transform: Annotated[
        Any,
        Field(
            default_factory=_defaults.default_constant_factory(Shift(1) & Shift(2)),
            title="Distortion transform as an instance of astropy.modeling.Model.",
        ),
    ]
