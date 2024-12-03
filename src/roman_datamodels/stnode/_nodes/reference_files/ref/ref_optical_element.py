from roman_datamodels.stnode import _core

from ...meta import WfiOpticalElement

__all__ = ["RefOpticalElementRef"]


class RefOpticalElementRefInstrument(_core.ObjectNode):
    @property
    def required(self) -> tuple[str]:
        return ("optical_element",)

    @property
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", WfiOpticalElement.F158)


class RefOpticalElementRef(_core.SchemaObjectNode):
    @property
    def schema_uri(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_optical_element-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return ("instrument",)

    @property
    def instrument(self) -> RefOpticalElementRefInstrument:
        return self._coerce(RefOpticalElementRefInstrument, self._get_node("instrument", coerce=False), "instrument")
