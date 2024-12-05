from astropy.time import Time

from roman_datamodels.stnode import _base, _core, _default

from ...meta import (
    Telescope,
    WfiDetector,
    WfiOpticalElement,
)

__all__ = ["RefCommonRef"]


class RefCommonRef_InstrumentMixin(_base.AdditionalNodeMixin):
    """Mixin things present in the constructors not present in the schema"""

    @property
    def optical_element(self) -> WfiOpticalElement | str:
        return self._get_node("optical_element", WfiOpticalElement.F158)

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        return ("optical_element",)


class RefCommonRef_Instrument(RefCommonRef_InstrumentMixin, _core.ObjectNode):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "name",
            "detector",
        )

    @property
    def name(self) -> str:
        return self._get_node("name", lambda: "WFI")

    @property
    def detector(self) -> WfiDetector:
        return self._get_node("detector", WfiDetector.WFI01)


class RefCommonRef(_core.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_common-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "reftype",
            "author",
            "description",
            "pedigree",
            "useafter",
            "telescope",
            "origin",
            "instrument",
        )

    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: _default.NOSTR)

    @property
    def pedigree(self) -> str:
        return self._get_node("pedigree", lambda: "GROUND")

    @property
    def description(self) -> str:
        return self._get_node("description", lambda: "blah blah blah")

    @property
    def author(self) -> str:
        return self._get_node("author", lambda: "test system")

    @property
    def useafter(self) -> Time:
        return self._get_node("useafter", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @property
    def telescope(self) -> Telescope | str:
        return self._get_node("telescope", Telescope.ROMAN)

    @property
    def origin(self) -> str:
        return self._get_node("origin", lambda: "STSCI")

    @property
    def instrument(self) -> RefCommonRef_Instrument:
        return self._get_node("instrument", RefCommonRef_Instrument)
