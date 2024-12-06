from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["InstrumentNameEntry"]


class InstrumentNameEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import MosaicBasic

        return MosaicBasic

    @classmethod
    def asdf_property_name(cls) -> str:
        return "instrument"


class InstrumentNameEntry(InstrumentNameEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible entries for instrument name in schemas
    """

    WFI = "WFI"
