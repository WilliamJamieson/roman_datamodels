from roman_datamodels.stnode import _core

from ...meta import ExposureType

__all__ = ["RefExposureTypeRef"]


class RefExposureTypeRef_Exposure(_core.ObjectNode):
    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "type",
            "p_exptype",
        )

    @property
    def type(self) -> ExposureType:
        return self._get_node("type", ExposureType.WFI_IMAGE)

    @property
    def p_exptype(self) -> str:
        return self._get_node("p_exptype", "WFI_IMAGE|WFI_GRISM|WFI_PRISM|")


class RefExposureTypeRef(_core.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_exposure_type-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return ("exposure",)

    @property
    def exposure(self) -> RefExposureTypeRef_Exposure:
        return self._get_node("exposure", RefExposureTypeRef_Exposure)
