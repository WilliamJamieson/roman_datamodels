from roman_datamodels.stnode import _core

__all__ = ["SourceCatalog"]


class SourceCatalog(_core.TaggedObjectNode):
    """
    Source detection catalog for TweakReg
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/source_catalog-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return tuple()

    @property
    def tweakreg_catalog_name(self) -> str:
        return self._get_node("tweakreg_catalog_name", lambda: "catalog")
