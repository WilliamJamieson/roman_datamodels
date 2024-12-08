from roman_datamodels.stnode import rad

__all__ = ["TvacModelType"]


class TvacModelType(str, rad.TaggedScalarNode):
    """
    Type of data model
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/model_type-1.0.0"
