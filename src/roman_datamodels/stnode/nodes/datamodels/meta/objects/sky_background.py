from enum import Enum

from roman_datamodels.stnode import rad

__all__ = [
    "SkyBackground",
    "SkyBackgroundMethodEntry",
]


class SkyBackgroundMethodEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        return SkyBackground

    @classmethod
    def asdf_property_name(cls) -> str:
        return "method"


class SkyBackgroundMethodEntry(SkyBackgroundMethodEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for method in sky_background
    """

    NONE = "None"
    LOCAL = "local"
    GLOBAL_MATCH = "global+match"
    MATCH = "match"
    GLOBAL = "global"


class SkyBackground(rad.TaggedObjectNode):
    """
    Sky Background Information
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/sky_background-1.0.0",)

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/sky_background-1.0.0"

    @rad.field
    def level(self) -> float | None:
        return self._get_node("level", lambda: rad.NONUM)

    @rad.field
    def method(self) -> SkyBackgroundMethodEntry:
        return self._get_node("method", lambda: SkyBackgroundMethodEntry.NONE)

    @rad.field
    def subtracted(self) -> bool:
        return self._get_node("subtracted", lambda: False)
