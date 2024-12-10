from roman_datamodels.stnode import rad

__all__ = ["RefFile"]


class RefFile_Crds(rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefFile

    @rad.field
    def version(self) -> str:
        return self._get_node("version", lambda: "12.3.1")

    @rad.field
    def context(self) -> str:
        return self._get_node("context", lambda: "roman_0815.pmap")


class RefFile(rad.TaggedObjectNode):
    """
    Calibration reference file names.
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/ref_file-1.0.0"

    @rad.field
    def crds(self) -> RefFile_Crds:
        return self._get_node("crds", RefFile_Crds)

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
    def inverse_linearity(self) -> str:
        return self._get_node("inverse_linearity", lambda: "N/A")

    @rad.field
    def photom(self) -> str:
        return self._get_node("photom", lambda: "N/A")

    @rad.field
    def area(self) -> str:
        return self._get_node("area", lambda: "N/A")

    @rad.field
    def saturation(self) -> str:
        return self._get_node("saturation", lambda: "N/A")

    @rad.field
    def refpix(self) -> str:
        return self._get_node("refpix", lambda: "N/A")
