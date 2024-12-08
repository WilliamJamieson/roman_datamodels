from roman_datamodels.stnode import _default, rad

__all__ = ["Photometry"]


class Photometry(rad.TaggedObjectNode):
    """
    Photometry information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/photometry-1.0.0"

    @rad.rad_field
    def conversion_megajanskys(self) -> float | None:
        return self._get_node("conversion_megajanskys", lambda: _default.NONUM)

    @rad.rad_field
    def conversion_megajanskys_uncertainty(self) -> float | None:
        return self._get_node("conversion_megajanskys_uncertainty", lambda: _default.NONUM)

    @rad.rad_field
    def pixel_area(self) -> float | None:
        return self._get_node("pixel_area", lambda: _default.NONUM)
