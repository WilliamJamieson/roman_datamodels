from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["TvacFilename"]


class TvacFilename(str, rad.TaggedScalarNode[str]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/filename-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/tvac/filename-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/filename-1.0.0"
            }
        )

    @classmethod
    def default(cls) -> TvacFilename:
        return cls(rad.NOSTR)
