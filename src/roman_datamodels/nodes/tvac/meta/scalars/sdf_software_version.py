from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["TvacSdfSoftwareVersion"]


class TvacSdfSoftwareVersion(str, rad.TaggedScalarNode):
    """
    SDF software version number
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/sdf_software_version-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/tvac/sdf_software_version-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/sdf_software_version-1.0.0"
            }
        )

    @classmethod
    def default(cls) -> TvacSdfSoftwareVersion:
        return cls("7.7.7")
