# Generated by RAD using generator based on datamodel-code-generator
#    source schema: common-1.0.0.yaml
#    time stamp:    VERSION CONTROLLED
# DO NOT EDIT THIS FILE DIRECTLY!

from __future__ import annotations

from typing import ClassVar

from . import (
    aperture,
    cal_step,
    coordinates,
    ephemeris,
    exposure,
    guidestar,
    observation,
    pointing,
    program,
    ref_file,
    target,
    velocity_aberration,
    visit,
    wcsinfo,
    wfi_mode,
)
from .basic import Basic


class Common(Basic):
    schema_uri: ClassVar[None] = None
    aperture: aperture.Aperture
    cal_step: cal_step.CalStep
    coordinates: coordinates.Coordinates
    ephemeris: ephemeris.Ephemeris
    exposure: exposure.Exposure
    guidestar: guidestar.Guidestar
    instrument: wfi_mode.WfiMode
    observation: observation.Observation
    pointing: pointing.Pointing
    program: program.Program
    ref_file: ref_file.RefFile
    target: target.Target
    velocity_aberration: velocity_aberration.VelocityAberration
    visit: visit.Visit
    wcsinfo: wcsinfo.Wcsinfo