from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["Statistics"]


class Statistics(rad.TaggedObjectNode[float]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/statistics-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/statistics-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/statistics-1.0.0"
            }
        )

    @rad.field
    def zodiacal_light(self) -> float:
        return rad.NONUM

    @rad.field
    def image_median(self) -> float:
        return rad.NONUM

    @rad.field
    def image_rms(self) -> float:
        return rad.NONUM

    @rad.field
    def good_pixel_fraction(self) -> float:
        return rad.NONUM
