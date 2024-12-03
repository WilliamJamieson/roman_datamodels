from roman_datamodels.stnode._nodes import _core

from ...meta import ExposureType

__all__ = ["RefExposureTypeRef"]


class RefExposureTypeRefExposure(_core.ObjectNode):
    @property
    def required(self) -> tuple[str]:
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
    @property
    def schema_uri(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/reference_files/ref_exposure_type-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return ("exposure",)

    @property
    def exposure(self) -> RefExposureTypeRefExposure:
        return self._get_node("exposure", RefExposureTypeRefExposure)
