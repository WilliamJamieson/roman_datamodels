from roman_datamodels.stnode import rad

__all__ = ["ModelType"]


class ModelType(str, rad.TaggedScalarNode):
    """
    Type of data model
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/model_type-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/model_type-1.0.0"
