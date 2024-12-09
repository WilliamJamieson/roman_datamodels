from roman_datamodels.stnode import rad

from ...meta import WfiOpticalElement

__all__ = ["RefOpticalElementRef"]


class RefOpticalElementRef_Instrument(rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefOpticalElementRef

    @rad.field
    def optical_element(self) -> WfiOpticalElement:
        return self._get_node("optical_element", lambda: WfiOpticalElement.F158)


class RefOpticalElementRef(rad.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_optical_element-1.0.0"

    @rad.field
    def instrument(self) -> RefOpticalElementRef_Instrument:
        return self._get_node("instrument", RefOpticalElementRef_Instrument)
