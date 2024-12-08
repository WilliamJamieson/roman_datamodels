from roman_datamodels.stnode import rad

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

    @rad.rad_field
    def coordinates(self) -> Coordinates:
        return self._get_node("coordinates", Coordinates)

    @rad.rad_field
    def ephemeris(self) -> Ephemeris:
        return self._get_node("ephemeris", Ephemeris)

    @rad.rad_field
    def exposure(self) -> Exposure:
        return self._get_node("exposure", Exposure)

    @rad.rad_field
    def guide_star(self) -> Guidestar:
        return self._get_node("guide_star", Guidestar)

    @rad.rad_field
    def instrument(self) -> WfiMode:
        return self._get_node("instrument", WfiMode)

    @rad.rad_field
    def observation(self) -> Observation:
        return self._get_node("observation", Observation)

    @rad.rad_field
    def pointing(self) -> Pointing:
        return self._get_node("pointing", Pointing)

    @rad.rad_field
    def program(self) -> Program:
        return self._get_node("program", Program)

    @rad.rad_field
    def rcs(self) -> Rcs:
        return self._get_node("rcs", Rcs)

    @rad.rad_field
    def ref_file(self) -> RefFile:
        return self._get_node("ref_file", RefFile)

    @rad.rad_field
    def velocity_aberration(self) -> VelocityAberration:
        return self._get_node("velocity_aberration", VelocityAberration)

    @rad.rad_field
    def visit(self) -> Visit:
        return self._get_node("visit", Visit)

    @rad.rad_field
    def wcsinfo(self) -> Wcsinfo:
        return self._get_node("wcsinfo", Wcsinfo)
