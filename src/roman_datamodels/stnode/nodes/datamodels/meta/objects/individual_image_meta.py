from astropy.table import QTable, Table

from roman_datamodels.stnode import rad

__all__ = ["IndividualImageMeta"]


class IndividualImageMeta(rad.TaggedObjectNode):
    """
    Combined level 2 metadata
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/individual_image_meta-1.0.0",)

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/individual_image_meta-1.0.0"

    @rad.field
    def basic(self) -> Table:
        return self._get_node("basic", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def background(self) -> Table:
        return self._get_node("background", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def cal_step(self) -> Table:
        return self._get_node("cal_step", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def cal_logs(self) -> Table:
        return self._get_node("cal_logs", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def coordinates(self) -> Table:
        return self._get_node("coordinates", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def ephemeris(self) -> Table:
        return self._get_node("ephemeris", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def exposure(self) -> Table:
        return self._get_node("exposure", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def guide_star(self) -> Table:
        return self._get_node("guide_star", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def instrument(self) -> Table:
        return self._get_node("instrument", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def observation(self) -> Table:
        return self._get_node("observation", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def outlier_detection(self) -> Table:
        return self._get_node("outlier_detection", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def photometry(self) -> Table:
        return self._get_node("photometry", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def pointing(self) -> Table:
        return self._get_node("pointing", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def program(self) -> Table:
        return self._get_node("program", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def rcs(self) -> Table:
        return self._get_node("rcs", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def ref_file(self) -> Table:
        return self._get_node("ref_file", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def source_catalog(self) -> Table:
        return self._get_node("source_catalog", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def velocity_aberration(self) -> Table:
        return self._get_node("velocity_aberration", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def visit(self) -> Table:
        return self._get_node("visit", lambda: QTable({"dummy": [rad.NONUM]}))

    @rad.field
    def wcsinfo(self) -> Table:
        return self._get_node("wcsinfo", lambda: QTable({"dummy": [rad.NONUM]}))
