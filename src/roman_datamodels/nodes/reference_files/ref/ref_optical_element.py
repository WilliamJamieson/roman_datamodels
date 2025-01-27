from typing import TypeVar

from roman_datamodels.stnode import rad

from ...datamodels import WfiOpticalElement

__all__ = ["RefOpticalElementRef"]

_T = TypeVar("_T")


class RefOpticalElementRef_Instrument(rad.ImpliedNodeMixin[WfiOpticalElement], rad.ObjectNode[WfiOpticalElement]):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefOpticalElementRef

    @rad.field
    def optical_element(self) -> WfiOpticalElement:
        return WfiOpticalElement.F158


class RefOpticalElementRef(rad.SchemaObjectNode[RefOpticalElementRef_Instrument | _T]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_optical_element-1.0.0",)

    @rad.field
    def instrument(self) -> RefOpticalElementRef_Instrument:
        return RefOpticalElementRef_Instrument()
