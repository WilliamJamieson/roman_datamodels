from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["TvacModelType"]


class TvacModelType(str, rad.TaggedScalarNode):
    """
    Type of data model
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/model_type-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/tvac/model_type-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/model_type-1.0.0"
            }
        )

    @classmethod
    def default(cls) -> TvacModelType:
        return cls(rad.NOSTR)
