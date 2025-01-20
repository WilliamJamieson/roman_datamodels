from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import core, rad

__all__ = ["MosaicWcsinfo", "MosaicWcsinfoProjectionEntry"]


class MosaicWcsinfoProjectionEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return MosaicWcsinfo

    @classmethod
    def asdf_property_name(cls) -> str:
        return "projection"


class MosaicWcsinfoProjectionEntry(MosaicWcsinfoProjectionEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for projection in wcsinfo
    """

    TAN = "TAN"


_MosaicWcsinfo: TypeAlias = MosaicWcsinfoProjectionEntry | core.LNode[core.LNode[float]] | core.LNode[int] | float | str


class MosaicWcsinfo(rad.TaggedObjectNode[_MosaicWcsinfo]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/mosaic_wcsinfo-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/mosaic_wcsinfo-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/mosaic_wcsinfo-1.0.0"
            }
        )

    @property
    @rad.field
    def ra_ref(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def dec_ref(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def x_ref(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def y_ref(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def rotation_matrix(self: rad.Node) -> core.LNode[core.LNode[float]]:
        return core.LNode(
            [
                core.LNode([rad.NONUM, rad.NONUM]),
                core.LNode([rad.NONUM, rad.NONUM]),
            ]
        )

    @property
    @rad.field
    def pixel_scale(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def pixel_scale_local(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def projection(self: rad.Node) -> MosaicWcsinfoProjectionEntry:
        return MosaicWcsinfoProjectionEntry.TAN

    @property
    @rad.field
    def s_region(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def pixel_shape(self: rad.Node) -> core.LNode[int]:
        return core.LNode([rad.NOINT, rad.NOINT])

    @property
    @rad.field
    def ra_center(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def dec_center(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def ra_corn1(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def dec_corn1(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def ra_corn2(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def dec_corn2(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def ra_corn3(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def dec_corn3(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def ra_corn4(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def dec_corn4(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def orientat_local(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def orientat(self: rad.Node) -> float:
        return rad.NONUM
