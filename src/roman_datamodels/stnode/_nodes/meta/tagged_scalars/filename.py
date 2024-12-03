from roman_datamodels.stnode import _core

__all__ = ["Filename"]


class Filename(_core.TaggedScalarNode, str):
    """
    Name of the file for the model
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/filename-1.0.0"
