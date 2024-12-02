from roman_datamodels.stnode import _core

__all__ = ["L3CalStep"]


class L3CalStep(_core.TaggedObjectNode):
    """
    Level 3 Calibration Step status information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/l3_cal_step-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "flux",
            "outlier_detection",
            "resample",
            "skymatch",
        )

    @property
    def flux(self) -> str:
        return self._get_node("flux", lambda: "INCOMPLETE")

    @property
    def outlier_detection(self) -> str:
        return self._get_node("outlier_detection", lambda: "INCOMPLETE")

    @property
    def skymatch(self) -> str:
        return self._get_node("skymatch", lambda: "INCOMPLETE")

    @property
    def resample(self) -> str:
        return self._get_node("resample", lambda: "INCOMPLETE")
