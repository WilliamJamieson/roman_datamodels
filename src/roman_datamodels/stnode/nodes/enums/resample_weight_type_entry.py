from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["ResampleWeightTypeEntry"]


class ResampleWeightTypeEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Resample

        return Resample

    @classmethod
    def asdf_property_name(cls) -> str:
        return "weight_type"


class ResampleWeightTypeEntry(ResampleWeightTypeEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible entries for resample weight type
    """

    EXPTIME = "exptime"
    IVM = "ivm"
