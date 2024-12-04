from roman_datamodels.stnode import _core

__all__ = ["L3CalStep"]


class L3CalStep(_core.TaggedObjectNode):
    """
    Level 3 Calibration Step status information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/l3_cal_step-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
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
