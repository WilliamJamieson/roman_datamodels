from roman_datamodels.stnode import rad

__all__ = ["SourceCatalog"]


class SourceCatalog(rad.TaggedObjectNode):
    """
    Source detection catalog for TweakReg
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/source_catalog-1.0.0"

    @rad.field
    def tweakreg_catalog_name(self) -> str:
        return self._get_node("tweakreg_catalog_name", lambda: "catalog")
