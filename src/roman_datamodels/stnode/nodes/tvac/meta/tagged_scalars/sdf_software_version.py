from roman_datamodels.stnode import rad

__all__ = ["TvacSdfSoftwareVersion"]


class TvacSdfSoftwareVersion(str, rad.TaggedScalarNode):
    """
    SDF software version number
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/sdf_software_version-1.0.0"
