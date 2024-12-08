from roman_datamodels.stnode import rad

from ...meta import ExposureType

__all__ = ["RefExposureTypeRef"]


class RefExposureTypeRef_Exposure(rad.ImpliedNodeMixin, rad.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return RefExposureTypeRef

    @rad.rad_field
    def type(self) -> ExposureType:
        return self._get_node("type", lambda: ExposureType.WFI_IMAGE)

    @rad.rad_field
    def p_exptype(self) -> str:
        return self._get_node("p_exptype", lambda: "WFI_IMAGE|WFI_GRISM|WFI_PRISM|")


class RefExposureTypeRef(rad.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_exposure_type-1.0.0"

    @rad.rad_field
    def exposure(self) -> RefExposureTypeRef_Exposure:
        return self._get_node("exposure", RefExposureTypeRef_Exposure)
