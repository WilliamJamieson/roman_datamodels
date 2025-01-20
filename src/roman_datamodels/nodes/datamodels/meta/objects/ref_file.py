from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

__all__ = ["RefFile"]

_Self_Crds: TypeAlias = rad.ObjectNode[str]


class RefFile_Crds(rad.ImpliedNodeMixin[str], rad.ObjectNode[str]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefFile

    @property
    @rad.field
    def version(self: rad.Node) -> str:
        return "12.3.1"

    @property
    @rad.field
    def context(self: rad.Node) -> str:
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

    @property
    @rad.field
    def crds(self: rad.Node) -> RefFile_Crds:
        return RefFile_Crds()

    @property
    @rad.field
    def dark(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def distortion(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def mask(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def flat(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def gain(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def readnoise(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def linearity(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def inverse_linearity(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def photom(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def area(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def saturation(self: rad.Node) -> str:
        return "N/A"

    @property
    @rad.field
    def refpix(self: rad.Node) -> str:
        return "N/A"
