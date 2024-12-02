from roman_datamodels.stnode import _core, _default

__all__ = ["Photometry"]


class Photometry(_core.TaggedObjectNode):
    """
    Photometry information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/photometry-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "conversion_megajanskys",
            "conversion_megajanskys_uncertainty",
            "pixel_area",
        )

    @property
    def conversion_megajanskys(self) -> None | float:
        return self._get_node("conversion_megajanskys", lambda: _default.NONUM)

    @property
    def conversion_megajanskys_uncertainty(self) -> None | float:
        return self._get_node("conversion_megajanskys_uncertainty", lambda: _default.NONUM)

    @property
    def pixel_area(self) -> None | float:
        return self._get_node("pixel_area", lambda: _default.NONUM)
