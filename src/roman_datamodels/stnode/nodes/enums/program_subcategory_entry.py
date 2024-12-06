from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["ProgramSubcategoryEntry"]


class ProgramSubcategoryEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Program

        return Program

    @classmethod
    def asdf_property_name(cls) -> str:
        return "subcategory"


class ProgramSubcategoryEntry(ProgramSubcategoryEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible program subcategories
    """

    CAL = "CAL"
    CGI = "CGI"
    CR = "CR"
    DR = "DR"
    GBTD = "GBTD"
    HLTD = "HLTD"
    HLWA = "HLWA"
    OR = "OR"
    WFI = "WFI"
    WFSC = "WFSC"
    NONE = "None"
