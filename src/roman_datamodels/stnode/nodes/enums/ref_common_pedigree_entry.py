from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["RefCommonPedigreeEntry"]


class RefCommonPedigreeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..reference_files import RefCommonRef

        return RefCommonRef

    @classmethod
    def asdf_property_name(cls) -> str:
        return "pedigree"


class RefCommonPedigreeEntry(RefCommonPedigreeEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible entries for pedigree in ref_common
    """

    GROUND = "GROUND"
    MODEL = "MODEL"
    DUMMY = "DUMMY"
    SIMULATION = "SIMULATION"
