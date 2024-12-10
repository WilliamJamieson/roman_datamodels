from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["FpsModelType"]


class FpsModelType(str, rad.TaggedScalarNode):
    """
    Type of data model
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/model_type-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/fps/model_type-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/model_type-1.0.0"
            }
        )
