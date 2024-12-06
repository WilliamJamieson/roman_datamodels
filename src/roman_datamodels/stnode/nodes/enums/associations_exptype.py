from enum import Enum

from roman_datamodels.stnode import _core

__all__ = ["AssociationsExptypeEntry"]


class AssociationsExptypeEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..datamodels.associations import Associations_Products_Members

        return Associations_Products_Members

    @classmethod
    def asdf_property_name(cls) -> str:
        return "exptype"


class AssociationsExptypeEntry(AssociationsExptypeEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible entries for exptype in associations
    """

    SCIENCE = "SCIENCE"
    CALIBRATION = "CALIBRATION"
    ENGINEERING = "ENGINEERING"
