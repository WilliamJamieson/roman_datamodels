from typing import TypeAlias, TypeVar

from roman_datamodels.stnode import rad

from .basic import Basic, _Basic
from .objects import (
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


# So that when we inherit from this we can include it's parts too
_T = TypeVar("_T")


_Common: TypeAlias = (
    _Basic
    | Coordinates
    | Ephemeris
    | Exposure
    | Guidestar
    | Observation
    | Pointing
    | Program
    | Rcs
    | RefFile
    | VelocityAberration
    | Visit
    | Wcsinfo
    | WfiMode
)


class Common(Basic[_Common | _T]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/common-1.0.0",)

    @property
    @rad.field
    def coordinates(self: rad.Node) -> Coordinates:
        return Coordinates()

    @property
    @rad.field
    def ephemeris(self: rad.Node) -> Ephemeris:
        return Ephemeris()

    @property
    @rad.field
    def exposure(self: rad.Node) -> Exposure:
        return Exposure()

    @property
    @rad.field
    def guide_star(self: rad.Node) -> Guidestar:
        return Guidestar()

    @property
    @rad.field
    def instrument(self: rad.Node) -> WfiMode:
        return WfiMode()

    @property
    @rad.field
    def observation(self: rad.Node) -> Observation:
        return Observation()

    @property
    @rad.field
    def pointing(self: rad.Node) -> Pointing:
        return Pointing()

    @property
    @rad.field
    def program(self: rad.Node) -> Program:
        return Program()

    @property
    @rad.field
    def rcs(self: rad.Node) -> Rcs:
        return Rcs()

    @property
    @rad.field
    def ref_file(self: rad.Node) -> RefFile:
        return RefFile()

    @property
    @rad.field
    def velocity_aberration(self: rad.Node) -> VelocityAberration:
        return VelocityAberration()

    @property
    @rad.field
    def visit(self: rad.Node) -> Visit:
        return Visit()

    @property
    @rad.field
    def wcsinfo(self: rad.Node) -> Wcsinfo:
        return Wcsinfo()
