from roman_datamodels.stnode import _core

from ...enums import CalStepEntry

__all__ = ["L2CalStep"]


class L2CalStep(_core.TaggedObjectNode):
    """
    Level 2 Calibration Step status information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/l2_cal_step-1.0.0"

    @_core.rad_field
    def assign_wcs(self) -> CalStepEntry:
        return self._get_node("assign_wcs", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def flat_field(self) -> CalStepEntry:
        return self._get_node("flat_field", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def dark(self) -> CalStepEntry:
        return self._get_node("dark", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def dq_init(self) -> CalStepEntry:
        return self._get_node("dq_init", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def flux(self) -> CalStepEntry:
        return self._get_node("flux", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def linearity(self) -> CalStepEntry:
        return self._get_node("linearity", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def photom(self) -> CalStepEntry:
        return self._get_node("photom", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def source_catalog(self) -> CalStepEntry:
        return self._get_node("source_catalog", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def ramp_fit(self) -> CalStepEntry:
        return self._get_node("ramp_fit", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def refpix(self) -> CalStepEntry:
        return self._get_node("refpix", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def saturation(self) -> CalStepEntry:
        return self._get_node("saturation", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def outlier_detection(self) -> CalStepEntry:
        return self._get_node("outlier_detection", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def tweakreg(self) -> CalStepEntry:
        return self._get_node("tweakreg", lambda: CalStepEntry.INCOMPLETE)

    @_core.rad_field
    def skymatch(self) -> CalStepEntry:
        return self._get_node("skymatch", lambda: CalStepEntry.INCOMPLETE)
