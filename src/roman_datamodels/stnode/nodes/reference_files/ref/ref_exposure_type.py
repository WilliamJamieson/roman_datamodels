from roman_datamodels.stnode import _core

from ...meta import ExposureType

__all__ = ["RefExposureTypeRef"]


class RefExposureTypeRef_Exposure(_core.ImpliedNodeMixin, _core.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefExposureTypeRef

    @_core.rad_field
    def type(self) -> ExposureType:
        return self._get_node("type", ExposureType.WFI_IMAGE)

    @_core.rad_field
    def p_exptype(self) -> str:
        return self._get_node("p_exptype", lambda: "WFI_IMAGE|WFI_GRISM|WFI_PRISM|")


class RefExposureTypeRef(_core.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_exposure_type-1.0.0"

    @_core.rad_field
    def exposure(self) -> RefExposureTypeRef_Exposure:
        return self._get_node("exposure", RefExposureTypeRef_Exposure)
