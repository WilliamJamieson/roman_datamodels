from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["SkyBackgroundMethodEntry"]


class SkyBackgroundMethodEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import SkyBackground

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
