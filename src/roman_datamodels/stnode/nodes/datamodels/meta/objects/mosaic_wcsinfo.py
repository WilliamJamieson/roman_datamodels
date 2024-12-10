from enum import Enum

from roman_datamodels.stnode import core, rad

__all__ = ["MosaicWcsinfo", "MosaicWcsinfoProjectionEntry"]


class MosaicWcsinfoProjectionEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return MosaicWcsinfo

    @classmethod
    def asdf_property_name(cls) -> str:
        return "projection"


class MosaicWcsinfoProjectionEntry(MosaicWcsinfoProjectionEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for projection in wcsinfo
    """

    TAN = "TAN"


class MosaicWcsinfo(rad.TaggedObjectNode):
    """
    Mosaic WCS parameters
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/mosaic_wcsinfo-1.0.0",)

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_wcsinfo-1.0.0"

    @rad.field
    def ra_ref(self) -> float:
        return self._get_node("ra_ref", lambda: rad.NONUM)

    @rad.field
    def dec_ref(self) -> float:
        return self._get_node("dec_ref", lambda: rad.NONUM)

    @rad.field
    def x_ref(self) -> float:
        return self._get_node("x_ref", lambda: rad.NONUM)

    @rad.field
    def y_ref(self) -> float:
        return self._get_node("y_ref", lambda: rad.NONUM)

    @rad.field
    def rotation_matrix(self) -> core.LNode[core.LNode[float]]:
        return self._get_node(
            "rotation_matrix",
            lambda: core.LNode(
                [
                    core.LNode([rad.NONUM, rad.NONUM]),
                    core.LNode([rad.NONUM, rad.NONUM]),
                ]
            ),
        )

    @rad.field
    def pixel_scale(self) -> float:
        return self._get_node("pixel_scale", lambda: rad.NONUM)

    @rad.field
    def pixel_scale_local(self) -> float:
        return self._get_node("pixel_scale_local", lambda: rad.NONUM)

    @rad.field
    def projection(self) -> MosaicWcsinfoProjectionEntry:
        return self._get_node("projection", lambda: MosaicWcsinfoProjectionEntry.TAN)

    @rad.field
    def s_region(self) -> str:
        return self._get_node("s_region", lambda: rad.NOSTR)

    @rad.field
    def pixel_shape(self) -> core.LNode[int]:
        return self._get_node("pixel_shape", lambda: core.LNode([rad.NOINT, rad.NOINT]))

    @rad.field
    def ra_center(self) -> float:
        return self._get_node("ra_center", lambda: rad.NONUM)

    @rad.field
    def dec_center(self) -> float:
        return self._get_node("dec_center", lambda: rad.NONUM)

    @rad.field
    def ra_corn1(self) -> float:
        return self._get_node("ra_corn1", lambda: rad.NONUM)

    @rad.field
    def dec_corn1(self) -> float:
        return self._get_node("dec_corn1", lambda: rad.NONUM)

    @rad.field
    def ra_corn2(self) -> float:
        return self._get_node("ra_corn2", lambda: rad.NONUM)

    @rad.field
    def dec_corn2(self) -> float:
        return self._get_node("dec_corn2", lambda: rad.NONUM)

    @rad.field
    def ra_corn3(self) -> float:
        return self._get_node("ra_corn3", lambda: rad.NONUM)

    @rad.field
    def dec_corn3(self) -> float:
        return self._get_node("dec_corn3", lambda: rad.NONUM)

    @rad.field
    def ra_corn4(self) -> float:
        return self._get_node("ra_corn4", lambda: rad.NONUM)

    @rad.field
    def dec_corn4(self) -> float:
        return self._get_node("dec_corn4", lambda: rad.NONUM)

    @rad.field
    def orientat_local(self) -> float:
        return self._get_node("orientat_local", lambda: rad.NONUM)

    @rad.field
    def orientat(self) -> float:
        return self._get_node("orientat", lambda: rad.NONUM)
