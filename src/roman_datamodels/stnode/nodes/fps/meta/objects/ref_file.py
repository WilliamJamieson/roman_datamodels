from roman_datamodels.stnode import rad

__all__ = ["FpsRefFile"]


class FpsRefFile_Crds(rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return FpsRefFile

    @rad.field
    def sw_version(self) -> str:
        return self._get_node("sw_version", lambda: "12.3.1")

    @rad.field
    def context_used(self) -> str:
        return self._get_node("context_used", lambda: "roman_0815.pmap")


class FpsRefFile(rad.TaggedObjectNode):
    """
    FPS Calibration reference file names.
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/ref_file-1.0.0",)

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/ref_file-1.0.0"

    @rad.field
    def crds(self) -> FpsRefFile_Crds:
        return self._get_node("crds", FpsRefFile_Crds)

    @rad.field
    def dark(self) -> str:
        return self._get_node("dark", lambda: "N/A")

    @rad.field
    def distortion(self) -> str:
        return self._get_node("distortion", lambda: "N/A")

    @rad.field
    def mask(self) -> str:
        return self._get_node("mask", lambda: "N/A")

    @rad.field
    def flat(self) -> str:
        return self._get_node("flat", lambda: "N/A")

    @rad.field
    def gain(self) -> str:
        return self._get_node("gain", lambda: "N/A")

    @rad.field
    def readnoise(self) -> str:
        return self._get_node("readnoise", lambda: "N/A")

    @rad.field
    def linearity(self) -> str:
        return self._get_node("linearity", lambda: "N/A")

    @rad.field
    def photom(self) -> str:
        return self._get_node("photom", lambda: "N/A")

    @rad.field
    def area(self) -> str:
        return self._get_node("area", lambda: "N/A")

    @rad.field
    def saturation(self) -> str:
        return self._get_node("saturation", lambda: "N/A")
