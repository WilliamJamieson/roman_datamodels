from astropy.table import QTable, Table

from roman_datamodels.stnode import _core, _default

__all__ = ["IndividualImageMeta"]


class IndividualImageMeta(_core.TaggedObjectNode):
    """
    Combined level 2 metadata
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/individual_image_meta-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return ("basic",)

    # @property
    # def required(self) -> tuple[str]:
    #     return (
    #         "basic",
    #         "background",
    #         "cal_step",
    #         "cal_logs",
    #         "coordinates",
    #         "ephemeris",
    #         "exposure",
    #         "guide_star",
    #         "instrument",
    #         "observation",
    #         "outlier_detection",
    #         "photometry",
    #         "pointing",
    #         "program",
    #         "rcs",
    #         "ref_file",
    #         "source_detection",
    #         "velocity_aberration",
    #         "visit",
    #         "wcsinfo",
    #     )

    @property
    def basic(self) -> Table:
        return self._get_node("basic", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def coordinates(self) -> Table:
        return self._get_node("coordinates", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def ephemeris(self) -> Table:
        return self._get_node("ephemeris", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def exposure(self) -> Table:
        return self._get_node("exposure", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def guide_star(self) -> Table:
        return self._get_node("guide_star", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def instrument(self) -> Table:
        return self._get_node("instrument", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def observation(self) -> Table:
        return self._get_node("observation", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def photometry(self) -> Table:
        return self._get_node("photometry", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def pointing(self) -> Table:
        return self._get_node("pointing", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def program(self) -> Table:
        return self._get_node("program", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def ref_file(self) -> Table:
        return self._get_node("ref_file", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def target(self) -> Table:
        return self._get_node("target", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def velocity_aberration(self) -> Table:
        return self._get_node("velocity_aberration", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def visit(self) -> Table:
        return self._get_node("visit", lambda: QTable({"dummy": [_default.NONUM]}))

    @property
    def wcsinfo(self) -> Table:
        return self._get_node("wcsinfo", lambda: QTable({"dummy": [_default.NONUM]}))
