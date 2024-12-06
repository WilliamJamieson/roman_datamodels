from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["CalStepEntry"]


class CalStepEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import L2CalStep

        return L2CalStep

    @classmethod
    def asdf_property_name(cls) -> str:
        return "assign_wcs"


class CalStepEntry(CalStepEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible CalStep entries
    """

    NA = "N/A"
    COMPLETE = "COMPLETE"
    SKIPPED = "SKIPPED"
    INCOMPLETE = "INCOMPLETE"
