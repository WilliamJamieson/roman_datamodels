from roman_datamodels.stnode import _core

__all__ = ["FpsFilename"]


class FpsFilename(str, _core.TaggedScalarNode):
    """
    Name of the file for the model
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/filename-1.0.0"
