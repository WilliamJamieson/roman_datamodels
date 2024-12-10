from roman_datamodels.stnode import rad

__all__ = ["MosaicAssociations"]


class MosaicAssociations(rad.TaggedObjectNode):
    """
    Mosaic associations metadata keywords
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/mosaic_associations-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_associations-1.0.0"

    @rad.field
    def pool_name(self) -> str:
        return self._get_node("pool_name", lambda: rad.NOSTR)

    @rad.field
    def table_name(self) -> str:
        return self._get_node("table_name", lambda: rad.NOSTR)
