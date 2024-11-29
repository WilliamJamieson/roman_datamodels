from roman_datamodels.stnode import _core

__all__ = ["Telescope"]


class Telescope(str, _core.TaggedScalarNode):
    """
    Telescope used to acquire the data
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/telescope-1.0.0"
