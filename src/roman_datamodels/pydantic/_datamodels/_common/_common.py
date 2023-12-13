from typing import Annotated, ClassVar

from pydantic import Field
from pydantic.config import ConfigDict

from roman_datamodels.pydantic import _defaults as defaults
from roman_datamodels.pydantic import _uri as uri

from . import (
    _aperture,
    _basic,
    _cal_step,
    _coordinates,
    _ephemeris,
    _exposure,
    _guidestar,
    _observation,
    _pointing,
    _program,
    _ref_file,
    _target,
    _velocity_aberration,
    _visit,
    _wcsinfo,
    _wfi_mode,
)

__all__ = ["Common"]


class Common(_basic.Basic):
    _uri: ClassVar = uri.asdf_uri.COMMON.value

    model_config = ConfigDict(
        title="Common metadata properties",
    )

    aperture: Annotated[
        _aperture.Aperture,
        Field(
            default_factory=defaults.default_model_factory(_aperture.Aperture),
        ),
    ]
    cal_step: Annotated[
        _cal_step.CalStep,
        Field(
            default_factory=defaults.default_model_factory(_cal_step.CalStep),
        ),
    ]
    coordinates: Annotated[
        _coordinates.Coordinates,
        Field(
            default_factory=defaults.default_model_factory(_coordinates.Coordinates),
        ),
    ]
    ephemeris: Annotated[
        _ephemeris.Ephemeris,
        Field(
            default_factory=defaults.default_model_factory(_ephemeris.Ephemeris),
        ),
    ]
    exposure: Annotated[
        _exposure.Exposure,
        Field(
            default_factory=defaults.default_model_factory(_exposure.Exposure),
        ),
    ]
    guidestar: Annotated[
        _guidestar.Guidestar,
        Field(
            default_factory=defaults.default_model_factory(_guidestar.Guidestar),
        ),
    ]
    instrument: Annotated[
        _wfi_mode.WfiMode,
        Field(
            default_factory=defaults.default_model_factory(_wfi_mode.WfiMode),
        ),
    ]
    observation: Annotated[
        _observation.Observation,
        Field(
            default_factory=defaults.default_model_factory(_observation.Observation),
        ),
    ]
    pointing: Annotated[
        _pointing.Pointing,
        Field(
            default_factory=defaults.default_model_factory(_pointing.Pointing),
        ),
    ]
    program: Annotated[
        _program.Program,
        Field(
            default_factory=defaults.default_model_factory(_program.Program),
        ),
    ]
    ref_file: Annotated[
        _ref_file.RefFile,
        Field(
            default_factory=defaults.default_model_factory(_ref_file.RefFile),
        ),
    ]
    target: Annotated[
        _target.Target,
        Field(
            default_factory=defaults.default_model_factory(_target.Target),
        ),
    ]
    velocity_aberration: Annotated[
        _velocity_aberration.VelocityAberration,
        Field(
            default_factory=defaults.default_model_factory(_velocity_aberration.VelocityAberration),
        ),
    ]
    visit: Annotated[
        _visit.Visit,
        Field(
            default_factory=defaults.default_model_factory(_visit.Visit),
        ),
    ]
    wcsinfo: Annotated[
        _wcsinfo.Wcsinfo,
        Field(
            default_factory=defaults.default_model_factory(_wcsinfo.Wcsinfo),
        ),
    ]
