from roman_datamodels.stnode import _core, _default

__all__ = ["Photometry"]


class Photometry(_core.TaggedObjectNode):
    """
    Photometry information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/photometry-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "conversion_megajanskys",
            "conversion_megajanskys_uncertainty",
            "pixel_area",
        )

    @property
    def conversion_megajanskys(self) -> float | None:
        return self._get_node("conversion_megajanskys", lambda: _default.NONUM)

    @property
    def conversion_megajanskys_uncertainty(self) -> float | None:
        return self._get_node("conversion_megajanskys_uncertainty", lambda: _default.NONUM)

    @property
    def pixel_area(self) -> float | None:
        return self._get_node("pixel_area", lambda: _default.NONUM)
