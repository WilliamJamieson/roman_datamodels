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
from ._wcsinfo import Wcsinfo
from ._wfi_mode import WfiMode

__all__ = ["Common"]


class Common(Basic):
    aperture: Aperture
    cal_step: CalStep
    coordinates: Coordinates
    ephemeris: Ephemeris
    exposure: Exposure
    guidestar: Guidestar
    instrument: WfiMode
    observation: Observation
    pointing: Pointing
    program: Program
    ref_file: RefFile
    target: Target
    velocity_aberration: VelocityAberration
    wcsinfo: Wcsinfo
