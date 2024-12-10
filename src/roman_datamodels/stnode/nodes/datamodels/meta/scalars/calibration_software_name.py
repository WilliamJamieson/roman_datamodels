from roman_datamodels.stnode import rad

__all__ = ["CalibrationSoftwareName"]


class CalibrationSoftwareName(str, rad.TaggedScalarNode):
    """
    Name of the calibration software used
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/calibration_software_name-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/calibration_software_name-1.0.0"
