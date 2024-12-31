from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["Filename"]


class Filename(str, rad.TaggedScalarNode):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/filename-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/filename-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/filename-1.0.0"
            }
        )

    @classmethod
    def default(cls) -> Filename:
        return cls(rad.NOFN)
