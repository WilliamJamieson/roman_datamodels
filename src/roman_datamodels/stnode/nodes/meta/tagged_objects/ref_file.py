from roman_datamodels.stnode import _core

__all__ = ["RefFile"]


class RefFile_Crds(_core.ImpliedNodeMixin, _core.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefFile

    @_core.rad_field
    def version(self) -> str:
        return self._get_node("version", lambda: "12.3.1")

    @_core.rad_field
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

    @_core.rad_field
    def crds(self) -> RefFile_Crds:
        return self._get_node("crds", RefFile_Crds)

    @_core.rad_field
    def dark(self) -> str:
        return self._get_node("dark", lambda: "N/A")

    @_core.rad_field
    def distortion(self) -> str:
        return self._get_node("distortion", lambda: "N/A")

    @_core.rad_field
    def mask(self) -> str:
        return self._get_node("mask", lambda: "N/A")

    @_core.rad_field
    def flat(self) -> str:
        return self._get_node("flat", lambda: "N/A")

    @_core.rad_field
    def gain(self) -> str:
        return self._get_node("gain", lambda: "N/A")

    @_core.rad_field
    def readnoise(self) -> str:
        return self._get_node("readnoise", lambda: "N/A")

    @_core.rad_field
    def linearity(self) -> str:
        return self._get_node("linearity", lambda: "N/A")

    @_core.rad_field
    def inverse_linearity(self) -> str:
        return self._get_node("inverse_linearity", lambda: "N/A")

    @_core.rad_field
    def photom(self) -> str:
        return self._get_node("photom", lambda: "N/A")

    @_core.rad_field
    def area(self) -> str:
        return self._get_node("area", lambda: "N/A")

    @_core.rad_field
    def saturation(self) -> str:
        return self._get_node("saturation", lambda: "N/A")

    @_core.rad_field
    def refpix(self) -> str:
        return self._get_node("refpix", lambda: "N/A")
