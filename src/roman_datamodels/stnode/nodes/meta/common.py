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

    @property
    def coordinates(self) -> Coordinates:
        return self._get_node("coordinates", Coordinates)

    @property
    def ephemeris(self) -> Ephemeris:
        return self._get_node("ephemeris", Ephemeris)

    @property
    def exposure(self) -> Exposure:
        return self._get_node("exposure", Exposure)

    @property
    def guide_star(self) -> Guidestar:
        return self._get_node("guide_star", Guidestar)

    @property
    def instrument(self) -> WfiMode:
        return self._get_node("instrument", WfiMode)

    @property
    def observation(self) -> Observation:
        return self._get_node("observation", Observation)

    @property
    def pointing(self) -> Pointing:
        return self._get_node("pointing", Pointing)

    @property
    def program(self) -> Program:
        return self._get_node("program", Program)

    @property
    def rcs(self) -> Rcs:
        return self._get_node("rcs", Rcs)

    @property
    def ref_file(self) -> RefFile:
        return self._get_node("ref_file", RefFile)

    @property
    def velocity_aberration(self) -> VelocityAberration:
        return self._get_node("velocity_aberration", VelocityAberration)

    @property
    def visit(self) -> Visit:
        return self._get_node("visit", Visit)

    @property
    def wcsinfo(self) -> Wcsinfo:
        return self._get_node("wcsinfo", Wcsinfo)
