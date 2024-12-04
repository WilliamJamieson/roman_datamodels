from roman_datamodels.stnode import _core

__all__ = ["FpsSdfSoftwareVersion"]


class FpsSdfSoftwareVersion(str, _core.TaggedScalarNode):
    """
    SDF software version number
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/sdf_software_version-1.0.0"
