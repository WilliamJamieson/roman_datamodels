from roman_datamodels.stnode import _core

__all__ = ["TvacModelType"]


class TvacModelType(str, _core.TaggedScalarNode):
    """
    Type of data model
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/model_type-1.0.0"
