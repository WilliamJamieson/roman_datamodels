from types import MappingProxyType
from typing import TypeAlias

from roman_datamodels.stnode import rad

__all__ = [
    "SkyBackground",
    "SkyBackgroundMethodEntry",
]


class SkyBackgroundMethodEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return SkyBackground

    @classmethod
    def asdf_property_name(cls) -> str:
        return "method"


class SkyBackgroundMethodEntry(SkyBackgroundMethodEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for method in sky_background
    """

    NONE = "None"
    LOCAL = "local"
    GLOBAL_MATCH = "global+match"
    MATCH = "match"
    GLOBAL = "global"


_SkyBackground: TypeAlias = SkyBackgroundMethodEntry | float | bool | None


class SkyBackground(rad.TaggedObjectNode[_SkyBackground]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/sky_background-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/sky_background-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/sky_background-1.0.0",
            }
        )

    @property
    @rad.field
    def level(self: rad.Node) -> float | None:
        return None

    @property
    @rad.field
    def method(self: rad.Node) -> SkyBackgroundMethodEntry:
        return SkyBackgroundMethodEntry.NONE

    @property
    @rad.field
    def subtracted(self: rad.Node) -> bool:
        return False
