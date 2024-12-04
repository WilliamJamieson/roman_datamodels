from roman_datamodels.stnode import _core

from ...meta import WfiOpticalElement

__all__ = ["RefOpticalElementRef"]


class RefOpticalElementRef_Instrument(_core.ObjectNode):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return ("optical_element",)

    @property
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", WfiOpticalElement.F158)


class RefOpticalElementRef(_core.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_optical_element-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return ("instrument",)

    @property
    def instrument(self) -> RefOpticalElementRef_Instrument:
        return self._get_node("instrument", RefOpticalElementRef_Instrument)
