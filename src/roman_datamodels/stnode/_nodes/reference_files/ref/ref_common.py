from astropy.time import Time

from roman_datamodels.stnode import _core

from ...meta import (
    Telescope,
    WfiDetector,
    WfiOpticalElement,
)

__all__ = ["RefCommonRef"]


class RefCommonRef_Instrument(_core.ObjectNode):
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
    def detector(self) -> WfiDetector | str:
        return self._get_node("detector", lambda: WfiDetector.WFI)

    @property
    def optical_element(self) -> WfiOpticalElement | str:
        return self._get_node("optical_element", lambda: WfiOpticalElement.F158)


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
        raise NotImplementedError("reftype is not implemented")

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
        return self._get_node("telescope", coerce=False)

    @property
    def origin(self) -> str:
        return self._get_node("origin", lambda: "STSCI")

    @property
    def instrument(self) -> RefCommonRef_Instrument:
        return self._get_node("instrument", RefCommonRef_Instrument)
