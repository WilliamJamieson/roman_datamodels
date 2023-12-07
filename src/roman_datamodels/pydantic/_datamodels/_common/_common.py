from typing import Annotated, ClassVar

from pydantic import Field
from pydantic.config import ConfigDict

from ..._defaults import default_model_factory
from ..._uri import asdf_uri
from ._aperture import Aperture
from ._basic import Basic
from ._cal_step import CalStep
from ._coordinates import Coordinates
from ._ephemeris import Ephemeris
from ._exposure import Exposure
from ._guidestar import Guidestar
from ._observation import Observation
from ._pointing import Pointing
from ._program import Program
from ._ref_file import RefFile
from ._target import Target
from ._velocity_aberration import VelocityAberration
from ._visit import Visit
from ._wcsinfo import Wcsinfo
from ._wfi_mode import WfiMode

__all__ = ["Common"]


class Common(Basic):
    _uri: ClassVar = asdf_uri.COMMON.value

    model_config = ConfigDict(
        title="Common metadata properties",
    )

    aperture: Annotated[
        Aperture,
        Field(
            default_factory=default_model_factory(Aperture),
        ),
    ]
    cal_step: Annotated[
        CalStep,
        Field(
            default_factory=default_model_factory(CalStep),
        ),
    ]
    coordinates: Annotated[
        Coordinates,
        Field(
            default_factory=default_model_factory(Coordinates),
        ),
    ]
    ephemeris: Annotated[
        Ephemeris,
        Field(
            default_factory=default_model_factory(Ephemeris),
        ),
    ]
    exposure: Annotated[
        Exposure,
        Field(
            default_factory=default_model_factory(Exposure),
        ),
    ]
    guidestar: Annotated[
        Guidestar,
        Field(
            default_factory=default_model_factory(Guidestar),
        ),
    ]
    instrument: Annotated[
        WfiMode,
        Field(
            default_factory=default_model_factory(WfiMode),
        ),
    ]
    observation: Annotated[
        Observation,
        Field(
            default_factory=default_model_factory(Observation),
        ),
    ]
    pointing: Annotated[
        Pointing,
        Field(
            default_factory=default_model_factory(Pointing),
        ),
    ]
    program: Annotated[
        Program,
        Field(
            default_factory=default_model_factory(Program),
        ),
    ]
    ref_file: Annotated[
        RefFile,
        Field(
            default_factory=default_model_factory(RefFile),
        ),
    ]
    target: Annotated[
        Target,
        Field(
            default_factory=default_model_factory(Target),
        ),
    ]
    velocity_aberration: Annotated[
        VelocityAberration,
        Field(
            default_factory=default_model_factory(VelocityAberration),
        ),
    ]
    visit: Annotated[
        Visit,
        Field(
            default_factory=default_model_factory(Visit),
        ),
    ]
    wcsinfo: Annotated[
        Wcsinfo,
        Field(
            default_factory=default_model_factory(Wcsinfo),
        ),
    ]
