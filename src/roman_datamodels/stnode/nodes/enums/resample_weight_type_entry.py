from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["ResampleWeightTypeEntry"]


class ResampleWeightTypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Resample

        return Resample

    @classmethod
    def asdf_property_name(cls) -> str:
        return "weight_type"


class ResampleWeightTypeEntry(ResampleWeightTypeEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for resample weight type
    """

    EXPTIME = "exptime"
    IVM = "ivm"
