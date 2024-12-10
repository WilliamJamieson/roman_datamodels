from roman_datamodels.stnode import rad

__all__ = ["Filename"]


class Filename(str, rad.TaggedScalarNode):
    """
    Name of the file for the model
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/filename-1.0.0"
