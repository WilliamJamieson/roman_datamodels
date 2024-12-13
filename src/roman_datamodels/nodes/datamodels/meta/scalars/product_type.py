from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["ProductType"]


class ProductType(str, rad.TaggedScalarNode):
    """
    Type of data product
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/product_type-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/product_type-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/product_type-1.0.0"
            }
        )

    @classmethod
    def default(cls) -> ProductType:
        return cls("l2")
