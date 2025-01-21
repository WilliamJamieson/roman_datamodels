from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["SdfSoftwareVersion"]


class SdfSoftwareVersion(str, rad.TaggedScalarNode):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/sdf_software_version-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/sdf_software_version-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/sdf_software_version-1.0.0"
            }
        )

    @classmethod
    def default(cls) -> SdfSoftwareVersion:
        return cls("7.7.7")
