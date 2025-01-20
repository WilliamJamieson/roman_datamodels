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

    @property
    @rad.field
    def assign_wcs(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def flat_field(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def dark(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def dq_init(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def flux(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def linearity(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def photom(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def source_catalog(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def ramp_fit(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def refpix(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def saturation(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def outlier_detection(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def tweakreg(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE

    @property
    @rad.field
    def skymatch(self: rad.Node) -> CalStepEntry:
        return CalStepEntry.INCOMPLETE
