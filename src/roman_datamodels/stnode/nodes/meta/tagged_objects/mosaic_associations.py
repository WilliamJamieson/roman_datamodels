from roman_datamodels.stnode import _default, rad

__all__ = ["MosaicAssociations"]


class MosaicAssociations(rad.TaggedObjectNode):
    """
    Mosaic associations metadata keywords
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_associations-1.0.0"

    @rad.rad_field
    def pool_name(self) -> str:
        return self._get_node("pool_name", lambda: _default.NOSTR)

    @rad.rad_field
    def table_name(self) -> str:
        return self._get_node("table_name", lambda: _default.NOSTR)
