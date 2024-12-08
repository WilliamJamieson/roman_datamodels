from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["InstrumentNameEntry"]


class InstrumentNameEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import MosaicBasic

        return MosaicBasic

    @classmethod
    def asdf_property_name(cls) -> str:
        return "instrument"


class InstrumentNameEntry(InstrumentNameEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for instrument name in schemas
    """

    WFI = "WFI"
