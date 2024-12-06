from roman_datamodels.stnode import _core

from .basic import Basic
from .tagged_objects import (
    Coordinates,
    Ephemeris,
    Exposure,
    Guidestar,
    Observation,
    Pointing,
    Program,
    Rcs,
    RefFile,
    VelocityAberration,
    Visit,
    Wcsinfo,
    WfiMode,
)

__all__ = ["Common"]


class Common(Basic):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/common-1.0.0"

    @_core.rad_field
    def coordinates(self) -> Coordinates:
        return self._get_node("coordinates", Coordinates)

    @_core.rad_field
    def ephemeris(self) -> Ephemeris:
        return self._get_node("ephemeris", Ephemeris)

    @_core.rad_field
    def exposure(self) -> Exposure:
        return self._get_node("exposure", Exposure)

    @_core.rad_field
    def guide_star(self) -> Guidestar:
        return self._get_node("guide_star", Guidestar)

    @_core.rad_field
    def instrument(self) -> WfiMode:
        return self._get_node("instrument", WfiMode)

    @_core.rad_field
    def observation(self) -> Observation:
        return self._get_node("observation", Observation)

    @_core.rad_field
    def pointing(self) -> Pointing:
        return self._get_node("pointing", Pointing)

    @_core.rad_field
    def program(self) -> Program:
        return self._get_node("program", Program)

    @_core.rad_field
    def rcs(self) -> Rcs:
        return self._get_node("rcs", Rcs)

    @_core.rad_field
    def ref_file(self) -> RefFile:
        return self._get_node("ref_file", RefFile)

    @_core.rad_field
    def velocity_aberration(self) -> VelocityAberration:
        return self._get_node("velocity_aberration", VelocityAberration)

    @_core.rad_field
    def visit(self) -> Visit:
        return self._get_node("visit", Visit)

    @_core.rad_field
    def wcsinfo(self) -> Wcsinfo:
        return self._get_node("wcsinfo", Wcsinfo)
