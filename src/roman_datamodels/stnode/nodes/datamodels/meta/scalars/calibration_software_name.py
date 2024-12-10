from roman_datamodels.stnode import rad

__all__ = ["CalibrationSoftwareName"]


class CalibrationSoftwareName(str, rad.TaggedScalarNode):
    """
    Name of the calibration software used
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/calibration_software_name-1.0.0"
