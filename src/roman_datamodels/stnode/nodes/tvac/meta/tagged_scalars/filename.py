from roman_datamodels.stnode import rad

__all__ = ["TvacFilename"]


class TvacFilename(str, rad.TaggedScalarNode):
    """
    Name of the file for the model
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/filename-1.0.0"
