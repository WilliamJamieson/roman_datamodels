from roman_datamodels.stnode import _core

__all__ = ["PrdVersion"]


class PrdVersion(str, _core.TaggedScalarNode):
    """
    S&OC PRD version number used in data processing
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/prd_version-1.0.0"
