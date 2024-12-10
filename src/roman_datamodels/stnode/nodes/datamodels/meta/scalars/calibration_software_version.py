from roman_datamodels.stnode import rad

__all__ = ["CalibrationSoftwareVersion"]


class CalibrationSoftwareVersion(str, rad.TaggedScalarNode):
    """
    Version of the calibration software used
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/calibration_software_version-1.0.0",)

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/calibration_software_version-1.0.0"
