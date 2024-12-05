from roman_datamodels.stnode import _core

__all__ = ["RefFile"]


class RefFile_Crds(_core.ImpliedNodeMixin, _core.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefFile

    @property
    def version(self) -> str:
        return self._get_node("version", lambda: "12.3.1")

    @property
    def context(self) -> str:
        return self._get_node("context", lambda: "roman_0815.pmap")


class RefFile(_core.TaggedObjectNode):
    """
    Calibration reference file names.

    Class generated from tag 'asdf://stsci.edu/datamodels/roman/tags/ref_file-1.0.0'
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/ref_file-1.0.0"

    @property
    def crds(self) -> RefFile_Crds:
        return self._get_node("crds", RefFile_Crds)

    @property
    def dark(self) -> str:
        return self._get_node("dark", lambda: "N/A")

    @property
    def distortion(self) -> str:
        return self._get_node("distortion", lambda: "N/A")

    @property
    def mask(self) -> str:
        return self._get_node("mask", lambda: "N/A")

    @property
    def flat(self) -> str:
        return self._get_node("flat", lambda: "N/A")

    @property
    def gain(self) -> str:
        return self._get_node("gain", lambda: "N/A")

    @property
    def readnoise(self) -> str:
        return self._get_node("readnoise", lambda: "N/A")

    @property
    def linearity(self) -> str:
        return self._get_node("linearity", lambda: "N/A")

    @property
    def inverse_linearity(self) -> str:
        return self._get_node("inverse_linearity", lambda: "N/A")

    @property
    def photom(self) -> str:
        return self._get_node("photom", lambda: "N/A")

    @property
    def area(self) -> str:
        return self._get_node("area", lambda: "N/A")

    @property
    def saturation(self) -> str:
        return self._get_node("saturation", lambda: "N/A")

    @property
    def refpix(self) -> str:
        return self._get_node("refpix", lambda: "N/A")
