from roman_datamodels.stnode import _core

__all__ = ["FpsCalStep"]


class FpsCalStep(_core.TaggedObjectNode):
    """
    FPS Level 2 Calibration Step status information
    """

    @classmethod
    def asdf_tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/cal_step-1.0.0"

    @_core.rad_field
    def assign_wcs(self) -> str:
        return self._get_node("assign_wcs", lambda: "INCOMPLETE")

    @_core.rad_field
    def flat_field(self) -> str:
        return self._get_node("flat_field", lambda: "INCOMPLETE")

    @_core.rad_field
    def dark(self) -> str:
        return self._get_node("dark", lambda: "INCOMPLETE")

    @_core.rad_field
    def dq_init(self) -> str:
        return self._get_node("dq_init", lambda: "INCOMPLETE")

    @_core.rad_field
    def flux(self) -> str:
        return self._get_node("flux", lambda: "INCOMPLETE")

    @_core.rad_field
    def jump(self) -> str:
        return self._get_node("jump", lambda: "INCOMPLETE")

    @_core.rad_field
    def linearity(self) -> str:
        return self._get_node("linearity", lambda: "INCOMPLETE")

    @_core.rad_field
    def photom(self) -> str:
        return self._get_node("photom", lambda: "INCOMPLETE")

    @_core.rad_field
    def source_detection(self) -> str:
        return self._get_node("source_detection", lambda: "INCOMPLETE")

    @_core.rad_field
    def ramp_fit(self) -> str:
        return self._get_node("ramp_fit", lambda: "INCOMPLETE")

    @_core.rad_field
    def refpix(self) -> str:
        return self._get_node("refpix", lambda: "INCOMPLETE")

    @_core.rad_field
    def saturation(self) -> str:
        return self._get_node("saturation", lambda: "INCOMPLETE")

    @_core.rad_field
    def outlier_detection(self) -> str:
        return self._get_node("outlier_detection", lambda: "INCOMPLETE")

    @_core.rad_field
    def tweakreg(self) -> str:
        return self._get_node("tweakreg", lambda: "INCOMPLETE")

    @_core.rad_field
    def skymatch(self) -> str:
        return self._get_node("skymatch", lambda: "INCOMPLETE")
