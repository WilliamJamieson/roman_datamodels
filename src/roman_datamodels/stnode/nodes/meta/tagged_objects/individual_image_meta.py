from astropy.table import QTable, Table

from roman_datamodels.stnode import _core, _default

__all__ = ["IndividualImageMeta"]


class IndividualImageMeta(_core.TaggedObjectNode):
    """
    Combined level 2 metadata
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/individual_image_meta-1.0.0"

    @_core.rad_field
    def basic(self) -> Table:
        return self._get_node("basic", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def background(self) -> Table:
        return self._get_node("background", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def cal_step(self) -> Table:
        return self._get_node("cal_step", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def cal_logs(self) -> Table:
        return self._get_node("cal_logs", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def coordinates(self) -> Table:
        return self._get_node("coordinates", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def ephemeris(self) -> Table:
        return self._get_node("ephemeris", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def exposure(self) -> Table:
        return self._get_node("exposure", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def guide_star(self) -> Table:
        return self._get_node("guide_star", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def instrument(self) -> Table:
        return self._get_node("instrument", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def observation(self) -> Table:
        return self._get_node("observation", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def outlier_detection(self) -> Table:
        return self._get_node("outlier_detection", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def photometry(self) -> Table:
        return self._get_node("photometry", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def pointing(self) -> Table:
        return self._get_node("pointing", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def program(self) -> Table:
        return self._get_node("program", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def rcs(self) -> Table:
        return self._get_node("rcs", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def ref_file(self) -> Table:
        return self._get_node("ref_file", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def source_catalog(self) -> Table:
        return self._get_node("source_catalog", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def velocity_aberration(self) -> Table:
        return self._get_node("velocity_aberration", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def visit(self) -> Table:
        return self._get_node("visit", lambda: QTable({"dummy": [_default.NONUM]}))

    @_core.rad_field
    def wcsinfo(self) -> Table:
        return self._get_node("wcsinfo", lambda: QTable({"dummy": [_default.NONUM]}))
