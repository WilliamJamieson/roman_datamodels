from roman_datamodels.stnode import _core

__all__ = ["TvacSdfSoftwareVersion"]


class TvacSdfSoftwareVersion(str, _core.TaggedScalarNode):
    """
    SDF software version number
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/sdf_software_version-1.0.0"
