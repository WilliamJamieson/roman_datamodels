from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

__all__ = ["TvacRefFile", "TvacRefFile_Crds"]


class TvacRefFile_Crds(rad.ImpliedNodeMixin[str], rad.ObjectNode[str]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return TvacRefFile

    @rad.field
    def sw_version(self) -> str:
        return "12.3.1"

    @rad.field
    def context_used(self) -> str:
        return "roman_0815.pmap"


_TvacRefFile: TypeAlias = TvacRefFile_Crds | str


class TvacRefFile(rad.TaggedObjectNode[_TvacRefFile]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/ref_file-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/tvac/ref_file-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/ref_file-1.0.0"
            }
        )

    @rad.field
    def crds(self) -> TvacRefFile_Crds:
        return TvacRefFile_Crds()

    @rad.field
    def dark(self) -> str:
        return "N/A"

    @rad.field
    def distortion(self) -> str:
        return "N/A"

    @rad.field
    def mask(self) -> str:
        return "N/A"

    @rad.field
    def flat(self) -> str:
        return "N/A"

    @rad.field
    def gain(self) -> str:
        return "N/A"

    @rad.field
    def readnoise(self) -> str:
        return "N/A"

    @rad.field
    def linearity(self) -> str:
        return "N/A"

    @rad.field
    def photom(self) -> str:
        return "N/A"

    @rad.field
    def area(self) -> str:
        return "N/A"

    @rad.field
    def saturation(self) -> str:
        return "N/A"
