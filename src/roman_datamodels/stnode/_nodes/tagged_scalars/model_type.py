from roman_datamodels.stnode import _core

__all__ = ["ModelType"]


class ModelType(str, _core.TaggedScalarNode):
    """
    Type of data model
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/model_type-1.0.0"
