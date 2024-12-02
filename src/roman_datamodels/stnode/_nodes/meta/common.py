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
    @property
    def schema_uri(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/common-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            *super().required,
            "coordinates",
            "ephemeris",
            "exposure",
            "guidestar",
            "instrument",
            "observation",
            "pointing",
            "program",
            "ref_file",
            "rcs",
            "velocity_aberration",
            "visit",
            "wcsinfo",
        )

    @property
    def coordinates(self) -> Coordinates:
        return self._coerce(Coordinates, self._get_node("coordinates", coerce=False), "coordinates")

    @property
    def ephemeris(self) -> Ephemeris:
        return self._coerce(Ephemeris, self._get_node("ephemeris", coerce=False), "ephemeris")

    @property
    def exposure(self) -> Exposure:
        return self._coerce(Exposure, self._get_node("exposure", coerce=False), "exposure")

    @property
    def guide_star(self) -> Guidestar:
        return self._coerce(Guidestar, self._get_node("guidestar", coerce=False), "guidestar")

    @property
    def instrument(self) -> WfiMode:
        return self._coerce(WfiMode, self._get_node("instrument", coerce=False), "instrument")

    @property
    def observation(self) -> Observation:
        return self._coerce(Observation, self._get_node("observation", coerce=False), "observation")

    @property
    def pointing(self) -> Pointing:
        return self._coerce(Pointing, self._get_node("pointing", coerce=False), "pointing")

    @property
    def program(self) -> Program:
        return self._coerce(Program, self._get_node("program", coerce=False), "program")

    @property
    def rcs(self) -> Rcs:
        return self._coerce(Rcs, self._get_node("rcs", coerce=False), "rcs")

    @property
    def ref_file(self) -> RefFile:
        return self._coerce(RefFile, self._get_node("ref_file", coerce=False), "ref_file")

    @property
    def velocity_aberration(self) -> VelocityAberration:
        return self._coerce(VelocityAberration, self._get_node("velocity_aberration", coerce=False), "velocity_aberration")

    @property
    def visit(self) -> Visit:
        return self._coerce(Visit, self._get_node("visit", coerce=False), "visit")

    @property
    def wcsinfo(self) -> Wcsinfo:
        return self._coerce(Wcsinfo, self._get_node("wcsinfo", coerce=False), "wcsinfo")
