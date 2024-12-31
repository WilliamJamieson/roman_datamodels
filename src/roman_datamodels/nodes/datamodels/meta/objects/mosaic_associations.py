from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["MosaicAssociations"]


class MosaicAssociations(rad.TaggedObjectNode):
    """
    Mosaic associations metadata keywords
    """

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

    @rad.field
    def pool_name(self) -> str:
        return rad.NOSTR

    @rad.field
    def table_name(self) -> str:
        return rad.NOSTR
