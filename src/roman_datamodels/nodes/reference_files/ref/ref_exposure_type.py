from typing import TypeAlias, TypeVar

from roman_datamodels.stnode import rad

from ...datamodels import ExposureType

__all__ = ["RefExposureTypeRef"]

_T = TypeVar("_T")

_RefExposureTypeRef_Exposure: TypeAlias = ExposureType | str


class RefExposureTypeRef_Exposure(
    rad.ImpliedNodeMixin[_RefExposureTypeRef_Exposure | _T], rad.ObjectNode[_RefExposureTypeRef_Exposure | _T]
):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefExposureTypeRef

    @property
    @rad.field
    def type(self: rad.Node) -> ExposureType:
        return ExposureType.WFI_IMAGE

    @property
    @rad.field
    def p_exptype(self: rad.Node) -> str:
        return "WFI_IMAGE|WFI_GRISM|WFI_PRISM|"


_RefExposureTypeRef: TypeAlias = RefExposureTypeRef_Exposure[_RefExposureTypeRef_Exposure]


class RefExposureTypeRef(rad.SchemaObjectNode[_RefExposureTypeRef | _T]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_exposure_type-1.0.0",)

    @property
    @rad.field
    def exposure(self: rad.Node) -> _RefExposureTypeRef:
        return RefExposureTypeRef_Exposure()
