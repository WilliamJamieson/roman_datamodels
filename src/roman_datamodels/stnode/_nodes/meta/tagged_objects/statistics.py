from roman_datamodels.stnode import _core, _default

__all__ = ["Statistics"]


class Statistics(_core.TaggedObjectNode):
    """
    Basic Statistical Information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/statistics-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "zodiacal_light",
            "image_median",
            "image_rms",
            "good_pixel_fraction",
        )

    @property
    def zodiacal_light(self) -> float:
        return self._get_node("zodiacal_light", lambda: _default.NONUM)

    @property
    def image_median(self) -> float:
        return self._get_node("image_median", lambda: _default.NONUM)

    @property
    def image_rms(self) -> float:
        return self._get_node("image_rms", lambda: _default.NONUM)

    @property
    def good_pixel_fraction(self) -> float:
        return self._get_node("good_pixel_fraction", lambda: _default.NONUM)
