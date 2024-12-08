from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["CalStepEntry"]


class CalStepEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import L2CalStep

        return L2CalStep

    @classmethod
    def asdf_property_name(cls) -> str:
        return "assign_wcs"


class CalStepEntry(CalStepEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible CalStep entries
    """

    NA = "N/A"
    COMPLETE = "COMPLETE"
    SKIPPED = "SKIPPED"
    INCOMPLETE = "INCOMPLETE"
