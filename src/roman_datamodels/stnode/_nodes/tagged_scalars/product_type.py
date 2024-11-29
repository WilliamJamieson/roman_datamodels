from roman_datamodels.stnode import _core

__all__ = ["ProductType"]


class ProductType(str, _core.TaggedScalarNode):
    """
    Type of data product
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/product_type-1.0.0"
