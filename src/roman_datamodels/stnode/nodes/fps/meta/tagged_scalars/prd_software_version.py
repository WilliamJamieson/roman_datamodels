from roman_datamodels.stnode import _core

__all__ = ["FpsPrdSoftwareVersion"]


class FpsPrdSoftwareVersion(str, _core.TaggedScalarNode):
    """
    S&OC PRD version number used in data processing
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/prd_software_version-1.0.0"
