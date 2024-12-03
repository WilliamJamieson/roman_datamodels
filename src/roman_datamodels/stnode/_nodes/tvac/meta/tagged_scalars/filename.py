from roman_datamodels.stnode import _core

__all__ = ["TvacFilename"]


class TvacFilename(str, _core.TaggedScalarNode):
    """
    Name of the file for the model
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/filename-1.0.0"
