from roman_datamodels.stnode import rad

__all__ = ["Statistics"]


class Statistics(rad.TaggedObjectNode):
    """
    Basic Statistical Information
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/statistics-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/statistics-1.0.0"

    @rad.field
    def zodiacal_light(self) -> float:
        return self._get_node("zodiacal_light", lambda: rad.NONUM)

    @rad.field
    def image_median(self) -> float:
        return self._get_node("image_median", lambda: rad.NONUM)

    @rad.field
    def image_rms(self) -> float:
        return self._get_node("image_rms", lambda: rad.NONUM)

    @rad.field
    def good_pixel_fraction(self) -> float:
        return self._get_node("good_pixel_fraction", lambda: rad.NONUM)
