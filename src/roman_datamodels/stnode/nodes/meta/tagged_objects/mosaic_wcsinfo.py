from roman_datamodels.stnode import _default, core, rad

from ...enums import WcsinfoMosaicProjectionEntry

__all__ = ["MosaicWcsinfo"]


class MosaicWcsinfo(rad.TaggedObjectNode):
    """
    Mosaic WCS parameters
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_wcsinfo-1.0.0"

    @rad.field
    def ra_ref(self) -> float:
        return self._get_node("ra_ref", lambda: _default.NONUM)

    @rad.field
    def dec_ref(self) -> float:
        return self._get_node("dec_ref", lambda: _default.NONUM)

    @rad.field
    def x_ref(self) -> float:
        return self._get_node("x_ref", lambda: _default.NONUM)

    @rad.field
    def y_ref(self) -> float:
        return self._get_node("y_ref", lambda: _default.NONUM)

    @rad.field
    def rotation_matrix(self) -> core.LNode[core.LNode[float]]:
        return self._get_node(
            "rotation_matrix",
            lambda: core.LNode(
                [
                    core.LNode([_default.NONUM, _default.NONUM]),
                    core.LNode([_default.NONUM, _default.NONUM]),
                ]
            ),
        )

    @rad.field
    def pixel_scale(self) -> float:
        return self._get_node("pixel_scale", lambda: _default.NONUM)

    @rad.field
    def pixel_scale_local(self) -> float:
        return self._get_node("pixel_scale_local", lambda: _default.NONUM)

    @rad.field
    def projection(self) -> WcsinfoMosaicProjectionEntry:
        return self._get_node("projection", lambda: WcsinfoMosaicProjectionEntry.TAN)

    @rad.field
    def s_region(self) -> str:
        return self._get_node("s_region", lambda: _default.NOSTR)

    @rad.field
    def pixel_shape(self) -> core.LNode[int]:
        return self._get_node("pixel_shape", lambda: core.LNode([_default.NOINT, _default.NOINT]))

    @rad.field
    def ra_center(self) -> float:
        return self._get_node("ra_center", lambda: _default.NONUM)

    @rad.field
    def dec_center(self) -> float:
        return self._get_node("dec_center", lambda: _default.NONUM)

    @rad.field
    def ra_corn1(self) -> float:
        return self._get_node("ra_corn1", lambda: _default.NONUM)

    @rad.field
    def dec_corn1(self) -> float:
        return self._get_node("dec_corn1", lambda: _default.NONUM)

    @rad.field
    def ra_corn2(self) -> float:
        return self._get_node("ra_corn2", lambda: _default.NONUM)

    @rad.field
    def dec_corn2(self) -> float:
        return self._get_node("dec_corn2", lambda: _default.NONUM)

    @rad.field
    def ra_corn3(self) -> float:
        return self._get_node("ra_corn3", lambda: _default.NONUM)

    @rad.field
    def dec_corn3(self) -> float:
        return self._get_node("dec_corn3", lambda: _default.NONUM)

    @rad.field
    def ra_corn4(self) -> float:
        return self._get_node("ra_corn4", lambda: _default.NONUM)

    @rad.field
    def dec_corn4(self) -> float:
        return self._get_node("dec_corn4", lambda: _default.NONUM)

    @rad.field
    def orientat_local(self) -> float:
        return self._get_node("orientat_local", lambda: _default.NONUM)

    @rad.field
    def orientat(self) -> float:
        return self._get_node("orientat", lambda: _default.NONUM)
