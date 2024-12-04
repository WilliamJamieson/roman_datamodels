from roman_datamodels.stnode import _core, _default

__all__ = ["MosaicAssociations"]


class MosaicAssociations(_core.TaggedObjectNode):
    """
    Mosaic associations metadata keywords
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/mosaic_associations-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "pool_name",
            "table_name",
        )

    @property
    def pool_name(self) -> str:
        return self._get_node("pool_name", lambda: _default.NOSTR)

    @property
    def table_name(self) -> str:
        return self._get_node("table_name", lambda: _default.NOSTR)
