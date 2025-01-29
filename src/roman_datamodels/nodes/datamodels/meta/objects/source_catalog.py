from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["SourceCatalog"]


class SourceCatalog(rad.TaggedObjectNode):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/source_catalog-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/source_catalog-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/source_catalog-1.0.0"
            }
        )

    @rad.field
    def tweakreg_catalog_name(self) -> str:
        return "catalog"
