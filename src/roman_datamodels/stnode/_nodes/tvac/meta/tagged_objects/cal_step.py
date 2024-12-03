from roman_datamodels.stnode import _core

__all__ = ["TvacCalStep"]


class TvacCalStep(_core.TaggedObjectNode):
    """
    Tvac Level 2 Calibration Step status information
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/cal_step-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "assign_wcs",
            "flat_field",
            "flux",
            "dark",
            "dq_init",
            "jump",
            "linearity",
            "outlier_detection",
            "photom",
            "source_detection",
            "ramp_fit",
            "refpix",
            "saturation",
            "skymatch",
            "tweakreg",
        )

    @property
    def assign_wcs(self) -> str:
        return self._get_node("assign_wcs", lambda: "INCOMPLETE")

    @property
    def flat_field(self) -> str:
        return self._get_node("flat_field", lambda: "INCOMPLETE")

    @property
    def dark(self) -> str:
        return self._get_node("dark", lambda: "INCOMPLETE")

    @property
    def dq_init(self) -> str:
        return self._get_node("dq_init", lambda: "INCOMPLETE")

    @property
    def flux(self) -> str:
        return self._get_node("flux", lambda: "INCOMPLETE")

    @property
    def jump(self) -> str:
        return self._get_node("jump", lambda: "INCOMPLETE")

    @property
    def linearity(self) -> str:
        return self._get_node("linearity", lambda: "INCOMPLETE")

    @property
    def photom(self) -> str:
        return self._get_node("photom", lambda: "INCOMPLETE")

    @property
    def source_detection(self) -> str:
        return self._get_node("source_detection", lambda: "INCOMPLETE")

    @property
    def ramp_fit(self) -> str:
        return self._get_node("ramp_fit", lambda: "INCOMPLETE")

    @property
    def refpix(self) -> str:
        return self._get_node("refpix", lambda: "INCOMPLETE")

    @property
    def saturation(self) -> str:
        return self._get_node("saturation", lambda: "INCOMPLETE")

    @property
    def outlier_detection(self) -> str:
        return self._get_node("outlier_detection", lambda: "INCOMPLETE")

    @property
    def tweakreg(self) -> str:
        return self._get_node("tweakreg", lambda: "INCOMPLETE")

    @property
    def skymatch(self) -> str:
        return self._get_node("skymatch", lambda: "INCOMPLETE")
