from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["FpsRefFile", "FpsRefFile_Crds"]


class FpsRefFile_Crds(rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return FpsRefFile

    @rad.field
    def sw_version(self) -> str:
        return "12.3.1"

    @rad.field
    def context_used(self) -> str:
        return "roman_0815.pmap"


class FpsRefFile(rad.TaggedObjectNode):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/ref_file-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/fps/ref_file-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/fps/ref_file-1.0.0"
            }
        )

    @rad.field
    def crds(self) -> FpsRefFile_Crds:
        return FpsRefFile_Crds()

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
