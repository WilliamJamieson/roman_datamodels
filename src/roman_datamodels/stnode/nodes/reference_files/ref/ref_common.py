from astropy.time import Time

from roman_datamodels.stnode import core, rad

from ...enums import InstrumentNameEntry, RefCommonPedigreeEntry, RefTypeEntry
from ...meta import (
    Telescope,
    WfiDetector,
    WfiOpticalElement,
)

__all__ = ["RefCommonRef"]


class RefCommonRef_InstrumentMixin(core.AdditionalNodeMixin):
    """Mixin things present in the constructors not present in the schema"""

    @rad.field
    def optical_element(self) -> WfiOpticalElement | str:
        return self._get_node("optical_element", lambda: WfiOpticalElement.F158)

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("optical_element",)


class RefCommonRef_Instrument(RefCommonRef_InstrumentMixin, rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefCommonRef

    @rad.field
    def name(self) -> InstrumentNameEntry:
        return self._get_node("name", lambda: InstrumentNameEntry.WFI)

    @rad.field
    def detector(self) -> WfiDetector:
        return self._get_node("detector", lambda: WfiDetector.WFI01)


class RefCommonRef(rad.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_common-1.0.0"

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.NA)

    @rad.field
    def pedigree(self) -> RefCommonPedigreeEntry:
        return self._get_node("pedigree", lambda: RefCommonPedigreeEntry.GROUND)

    @rad.field
    def description(self) -> str:
        return self._get_node("description", lambda: "blah blah blah")

    @rad.field
    def author(self) -> str:
        return self._get_node("author", lambda: "test system")

    @rad.field
    def useafter(self) -> Time:
        return self._get_node("useafter", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def telescope(self) -> Telescope | str:
        return self._get_node("telescope", lambda: Telescope.ROMAN)

    @rad.field
    def origin(self) -> str:
        return self._get_node("origin", lambda: "STSCI")

    @rad.field
    def instrument(self) -> RefCommonRef_Instrument:
        return self._get_node("instrument", RefCommonRef_Instrument)
