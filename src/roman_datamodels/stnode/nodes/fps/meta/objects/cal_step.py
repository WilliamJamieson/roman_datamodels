from roman_datamodels.stnode import rad

from ....datamodels import CalStepEntry

__all__ = ["FpsCalStep"]


class FpsCalStep(rad.TaggedObjectNode):
    """
    FPS Level 2 Calibration Step status information
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/cal_step-1.0.0",)

    @classmethod
    def asdf_tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/cal_step-1.0.0"

    @rad.field
    def assign_wcs(self) -> CalStepEntry:
        return self._get_node("assign_wcs", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def flat_field(self) -> CalStepEntry:
        return self._get_node("flat_field", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def dark(self) -> CalStepEntry:
        return self._get_node("dark", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def dq_init(self) -> CalStepEntry:
        return self._get_node("dq_init", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def flux(self) -> CalStepEntry:
        return self._get_node("flux", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def jump(self) -> CalStepEntry:
        return self._get_node("jump", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def linearity(self) -> CalStepEntry:
        return self._get_node("linearity", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def photom(self) -> CalStepEntry:
        return self._get_node("photom", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def source_detection(self) -> CalStepEntry:
        return self._get_node("source_detection", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def ramp_fit(self) -> CalStepEntry:
        return self._get_node("ramp_fit", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def refpix(self) -> CalStepEntry:
        return self._get_node("refpix", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def saturation(self) -> CalStepEntry:
        return self._get_node("saturation", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def outlier_detection(self) -> CalStepEntry:
        return self._get_node("outlier_detection", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def tweakreg(self) -> CalStepEntry:
        return self._get_node("tweakreg", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def skymatch(self) -> CalStepEntry:
        return self._get_node("skymatch", lambda: CalStepEntry.INCOMPLETE)
