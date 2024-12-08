from roman_datamodels.stnode import rad

__all__ = ["ProductType"]


class ProductType(str, rad.TaggedScalarNode):
    """
    Type of data product
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/product_type-1.0.0"
