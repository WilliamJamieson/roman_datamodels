from roman_datamodels.stnode import _core

__all__ = ["FpsRefFile"]


class FpsRefFile_Crds(_core.ImpliedNodeMixin, _core.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return FpsRefFile

    @property
    def sw_version(self) -> str:
        return self._get_node("sw_version", lambda: "12.3.1")

    @property
    def context_used(self) -> str:
        return self._get_node("context_used", lambda: "roman_0815.pmap")


class FpsRefFile(_core.TaggedObjectNode):
    """
    FPS Calibration reference file names.
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/ref_file-1.0.0"

    @property
    def crds(self) -> FpsRefFile_Crds:
        return self._get_node("crds", FpsRefFile_Crds)

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
    def photom(self) -> str:
        return self._get_node("photom", lambda: "N/A")

    @property
    def area(self) -> str:
        return self._get_node("area", lambda: "N/A")

    @property
    def saturation(self) -> str:
        return self._get_node("saturation", lambda: "N/A")
