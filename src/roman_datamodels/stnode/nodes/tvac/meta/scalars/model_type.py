from roman_datamodels.stnode import rad

__all__ = ["TvacModelType"]


class TvacModelType(str, rad.TaggedScalarNode):
    """
    Type of data model
    """

    @classmethod
    def asdf_schema_uri(cls):
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/model_type-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/model_type-1.0.0"
