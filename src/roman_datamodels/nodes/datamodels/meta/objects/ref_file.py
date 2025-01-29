from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

__all__ = ["RefFile", "RefFile_Crds"]

_Self_Crds: TypeAlias = rad.ObjectNode[str]


class RefFile_Crds(rad.ImpliedNodeMixin[str], rad.ObjectNode[str]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefFile

    @rad.field
    def version(self) -> str:
        return "12.3.1"

    @rad.field
    def context(self) -> str:
        return "roman_0815.pmap"


_RefFile: TypeAlias = RefFile_Crds | str


class RefFile(rad.TaggedObjectNode[_RefFile]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/ref_file-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {"asdf://stsci.edu/datamodels/roman/tags/ref_file-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/ref_file-1.0.0"}
        )

    @rad.field
    def crds(self) -> RefFile_Crds:
        return RefFile_Crds()

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
    def inverse_linearity(self) -> str:
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

    @rad.field
    def refpix(self) -> str:
        return "N/A"
