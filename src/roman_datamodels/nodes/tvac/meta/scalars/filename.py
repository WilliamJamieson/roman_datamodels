from __future__ import annotations

from roman_datamodels.stnode import rad

__all__ = ["TvacFilename"]


class TvacFilename(str, rad.TaggedScalarNode):
    @classmethod
    def _asdf_tag_uris(cls) -> dict[str, str]:
        return {
            "asdf://stsci.edu/datamodels/roman/tags/tvac/filename-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/filename-1.0.0"
        }

    @classmethod
    def default(cls) -> TvacFilename:
        return cls(rad.NOSTR)
