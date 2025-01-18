from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

__all__ = ["Photometry"]


_Photometry: TypeAlias = float | None


class Photometry(rad.TaggedObjectNode[_Photometry]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/photometry-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/photometry-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/photometry-1.0.0"
            }
        )

    @rad.field
    def conversion_megajanskys(self) -> float | None:
        return rad.NONUM

    @rad.field
    def conversion_megajanskys_uncertainty(self) -> float | None:
        return rad.NONUM

    @rad.field
    def pixel_area(self) -> float | None:
        return rad.NONUM
