from types import MappingProxyType

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
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/individual_image_meta-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/individual_image_meta-1.0.0"
            }
        )

    @rad.field
    def basic(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def background(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def cal_step(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def cal_logs(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def coordinates(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def ephemeris(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def exposure(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def guide_star(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def instrument(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def observation(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def outlier_detection(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def photometry(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def pointing(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def program(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def rcs(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def ref_file(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def source_catalog(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def velocity_aberration(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def visit(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @rad.field
    def wcsinfo(self) -> Table:
        return QTable({"dummy": [rad.NONUM]})
