from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["SourceCatalog"]


class SourceCatalog(rad.TaggedObjectNode[str]):
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

    @property
    @rad.field
    def tweakreg_catalog_name(self: rad.Node) -> str:
        return "catalog"
