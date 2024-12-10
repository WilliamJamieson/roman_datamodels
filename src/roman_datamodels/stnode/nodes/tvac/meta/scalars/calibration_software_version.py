from roman_datamodels.stnode import rad

__all__ = ["TvacCalibrationSoftwareVersion"]


class TvacCalibrationSoftwareVersion(str, rad.TaggedScalarNode):
    """
    Version of the calibration software used
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/calibration_software_version-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/calibration_software_version-1.0.0"
