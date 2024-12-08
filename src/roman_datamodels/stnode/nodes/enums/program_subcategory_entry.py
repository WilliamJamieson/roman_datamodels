from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["ProgramSubcategoryEntry"]


class ProgramSubcategoryEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Program

        return Program

    @classmethod
    def asdf_property_name(cls) -> str:
        return "subcategory"


class ProgramSubcategoryEntry(ProgramSubcategoryEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
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
