from roman_datamodels.stnode import _core

__all__ = ["CalibrationSoftwareVersion"]


class CalibrationSoftwareVersion(str, _core.TaggedScalarNode):
    """
    Version of the calibration software used
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/calibration_software_version-1.0.0"
