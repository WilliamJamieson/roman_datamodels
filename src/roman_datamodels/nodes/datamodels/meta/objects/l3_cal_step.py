from types import MappingProxyType

from roman_datamodels.stnode import rad

from .l2_cal_step import CalStepEntry

__all__ = ["L3CalStep"]


class L3CalStep(rad.TaggedObjectNode[CalStepEntry]):
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

    @property
    @rad.field
    def flux(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def outlier_detection(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def skymatch(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def resample(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE
