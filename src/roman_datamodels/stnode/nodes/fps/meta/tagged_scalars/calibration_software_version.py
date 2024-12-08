from roman_datamodels.stnode import rad

__all__ = ["FpsCalibrationSoftwareVersion"]


class FpsCalibrationSoftwareVersion(str, rad.TaggedScalarNode):
    """
    Version of the calibration software used
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/calibration_software_version-1.0.0"
