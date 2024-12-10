from roman_datamodels.stnode import rad

__all__ = ["FpsCalibrationSoftwareVersion"]


class FpsCalibrationSoftwareVersion(str, rad.TaggedScalarNode):
    """
    Version of the calibration software used
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/calibration_software_version-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/calibration_software_version-1.0.0"
