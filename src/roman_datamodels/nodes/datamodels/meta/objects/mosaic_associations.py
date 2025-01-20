from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["MosaicAssociations"]


class MosaicAssociations(rad.TaggedObjectNode[str]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/mosaic_associations-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/mosaic_associations-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/mosaic_associations-1.0.0"
            }
        )

    @property
    @rad.field
    def pool_name(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def table_name(self: rad.Node) -> str:
        return rad.NOSTR
