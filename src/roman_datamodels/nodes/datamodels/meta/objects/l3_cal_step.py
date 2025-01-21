from types import MappingProxyType

from roman_datamodels.stnode import rad

from .l2_cal_step import CalStepEntry

__all__ = ["L3CalStep"]


class L3CalStep(rad.TaggedObjectNode):
    """
    Level 3 Calibration Step status information
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/l3_cal_step-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/l3_cal_step-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/l3_cal_step-1.0.0"
            }
        )

    @rad.field
    def flux(self) -> CalStepEntry:
        return self._get_node("flux", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def outlier_detection(self) -> CalStepEntry:
        return self._get_node("outlier_detection", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def skymatch(self) -> CalStepEntry:
        return self._get_node("skymatch", lambda: CalStepEntry.INCOMPLETE)

    @rad.field
    def resample(self) -> CalStepEntry:
        return self._get_node("resample", lambda: CalStepEntry.INCOMPLETE)
