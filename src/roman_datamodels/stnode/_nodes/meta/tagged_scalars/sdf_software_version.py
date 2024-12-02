from roman_datamodels.stnode import _core

__all__ = ["SdfSoftwareVersion"]


class SdfSoftwareVersion(str, _core.TaggedScalarNode):
    """
    SDF software version number
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/sdf_software_version-1.0.0"
