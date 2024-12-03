from roman_datamodels.stnode import _core

__all__ = ["TvacPrdSoftwareVersion"]


class TvacPrdSoftwareVersion(str, _core.TaggedScalarNode):
    """
    S&OC PRD version number used in data processing
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/prd_software_version-1.0.0"
