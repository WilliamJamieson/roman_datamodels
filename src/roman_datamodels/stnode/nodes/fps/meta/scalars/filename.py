from roman_datamodels.stnode import rad

__all__ = ["FpsFilename"]


class FpsFilename(str, rad.TaggedScalarNode):
    """
    Name of the file for the model
    """

    @classmethod
    def asdf_schema_uri(clas):
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/filename-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/filename-1.0.0"
