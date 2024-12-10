from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["PrdVersion"]


class PrdVersion(str, rad.TaggedScalarNode):
    """
    S&OC PRD version number used in data processing
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/prd_version-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/prd_version-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/prd_version-1.0.0"
            }
        )
