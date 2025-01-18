from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["CalStepEntry", "L2CalStep"]


class CalStepEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return L2CalStep

    @classmethod
    def asdf_property_name(cls) -> str:
        return "assign_wcs"


class CalStepEntry(CalStepEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible CalStep entries
    """

    NA = "N/A"
    COMPLETE = "COMPLETE"
    SKIPPED = "SKIPPED"
    INCOMPLETE = "INCOMPLETE"


class L2CalStep(rad.TaggedObjectNode[CalStepEntry]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/l2_cal_step-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/l2_cal_step-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/l2_cal_step-1.0.0"
            }
        )

    @rad.field
    def assign_wcs(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def flat_field(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def dark(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def dq_init(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def flux(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def linearity(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def photom(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def source_catalog(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def ramp_fit(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def refpix(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def saturation(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def outlier_detection(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def tweakreg(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @rad.field
    def skymatch(self) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE
