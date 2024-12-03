from roman_datamodels.stnode import _core

__all__ = ["CalibrationSoftwareName"]


class CalibrationSoftwareName(str, _core.TaggedScalarNode):
    """
    Name of the calibration software used
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/calibration_software_name-1.0.0"
