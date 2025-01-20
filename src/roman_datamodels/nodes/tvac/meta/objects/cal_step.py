from types import MappingProxyType

from roman_datamodels.stnode import rad

from ....datamodels import CalStepEntry

__all__ = ["TvacCalStep"]


class TvacCalStep(rad.TaggedObjectNode[CalStepEntry]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/cal_step-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/tvac/cal_step-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/cal_step-1.0.0"
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
    def jump(self: rad.Node) -> CalStepEntry:
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
    def source_detection(self: rad.Node) -> CalStepEntry:
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
