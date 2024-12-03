from roman_datamodels.stnode import _core

__all__ = ["FpsModelType"]


class FpsModelType(str, _core.TaggedScalarNode):
    """
    Type of data model
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/model_type-1.0.0"
