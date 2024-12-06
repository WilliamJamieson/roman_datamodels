from astropy.time import Time

from roman_datamodels.stnode import _base, _core

from ...enums import InstrumentNameEntry, RefCommonPedigreeEntry, RefTypeEntry
from ...meta import (
    Telescope,
    WfiDetector,
    WfiOpticalElement,
)

__all__ = ["RefCommonRef"]


class RefCommonRef_InstrumentMixin(_base.AdditionalNodeMixin):
    """Mixin things present in the constructors not present in the schema"""

    @_core.rad_field
    def optical_element(self) -> WfiOpticalElement | str:
        return self._get_node("optical_element", lambda: WfiOpticalElement.F158)

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("optical_element",)


class RefCommonRef_Instrument(RefCommonRef_InstrumentMixin, _core.ImpliedNodeMixin, _core.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefCommonRef

    @_core.rad_field
    def name(self) -> InstrumentNameEntry:
        return self._get_node("name", lambda: InstrumentNameEntry.WFI)

    @_core.rad_field
    def detector(self) -> WfiDetector:
        return self._get_node("detector", lambda: WfiDetector.WFI01)


class RefCommonRef(_core.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_common-1.0.0"

    @_core.rad_field
    def reftype(self) -> RefTypeEntry:
        return self._get_node("reftype", lambda: RefTypeEntry.NA)

    @_core.rad_field
    def pedigree(self) -> RefCommonPedigreeEntry:
        return self._get_node("pedigree", lambda: RefCommonPedigreeEntry.GROUND)

    @_core.rad_field
    def description(self) -> str:
        return self._get_node("description", lambda: "blah blah blah")

    @_core.rad_field
    def author(self) -> str:
        return self._get_node("author", lambda: "test system")

    @_core.rad_field
    def useafter(self) -> Time:
        return self._get_node("useafter", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @_core.rad_field
    def telescope(self) -> Telescope | str:
        return self._get_node("telescope", lambda: Telescope.ROMAN)

    @_core.rad_field
    def origin(self) -> str:
        return self._get_node("origin", lambda: "STSCI")

    @_core.rad_field
    def instrument(self) -> RefCommonRef_Instrument:
        return self._get_node("instrument", RefCommonRef_Instrument)
