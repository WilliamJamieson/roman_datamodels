from roman_datamodels.stnode import _core

__all__ = ["FpsRefFile"]


class FpsCrds(_core.ObjectNode):
    @property
    def required(self) -> tuple[str]:
        return (
            "version",
            "context",
        )

    @property
    def version(self) -> str:
        return self._get_node("version", lambda: "12.3.1")

    @property
    def context(self) -> str:
        return self._get_node("context", lambda: "roman_0815.pmap")


class FpsRefFile(_core.TaggedObjectNode):
    """
    FPS Calibration reference file names.
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/ref_file-1.0.0"

    @property
    def required(self) -> str:
        return (
            "crds",
            "dark",
            "distortion",
            "mask",
            "flat",
            "gain",
            "readnoise",
            "linearity",
            "photom",
            "area",
            "saturation",
        )

    @property
    def crds(self) -> FpsCrds:
        return self._get_node("crds", FpsCrds)

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
