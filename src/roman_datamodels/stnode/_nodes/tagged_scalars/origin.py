from roman_datamodels.stnode import _core

__all__ = ["Origin"]


class Origin(str, _core.TaggedScalarNode):
    """
    Organization responsible for creating file
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/origin-1.0.0"
