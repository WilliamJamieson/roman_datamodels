from roman_datamodels.stnode import _core

__all__ = ["TvacPrdSoftwareVersion"]


class TvacPrdSoftwareVersion(str, _core.TaggedScalarNode):
    """
    S&OC PRD version number used in data processing
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/prd_software_version-1.0.0"
