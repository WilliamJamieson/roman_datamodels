from types import MappingProxyType

from astropy.table import QTable, Table

from roman_datamodels.stnode import rad

__all__ = ["IndividualImageMeta"]


class IndividualImageMeta(rad.TaggedObjectNode[Table]):
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

    @property
    @rad.field
    def basic(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def background(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def cal_step(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def cal_logs(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def coordinates(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def ephemeris(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def exposure(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def guide_star(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def instrument(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def observation(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def outlier_detection(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def photometry(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def pointing(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def program(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def rcs(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def ref_file(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def source_catalog(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def velocity_aberration(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def visit(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})

    @property
    @rad.field
    def wcsinfo(self: rad.Node) -> Table:
        return QTable({"dummy": [rad.NONUM]})
