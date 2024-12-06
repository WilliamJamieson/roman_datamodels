from enum import Enum

from roman_datamodels.stnode import _core

__all__ = [
    "VisitEngineeringQualityEntry",
    "VisitPointingEngineeringSourceEntry",
    "VisitStatusEntry",
    "VisitTypeEntry",
]


class VisitEngineeringQualityEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Visit

        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "engineering_quality"


class VisitEngineeringQualityEntry(VisitEngineeringQualityEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible entries for quality in visit engineering
    """

    OK = "OK"
    SUSPECT = "SUSPECT"


class VisitPointingEngineeringSourceEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Visit

        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "pointing_engineering_source"


class VisitPointingEngineeringSourceEntry(VisitPointingEngineeringSourceEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible entries for source in visit pointing engineering
    """

    CALCULATED = "CALCULATED"
    PLANNED = "PLANNED"


class VisitTypeEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Visit

        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "type"


class VisitTypeEntry(VisitTypeEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible entries for type in visit
    """

    GENERAL_ENGINEERING = "GENERAL_ENGINEERING"
    GENERIC = "GENERIC"
    PARALLEL = "PARALLEL"
    PRIME_TARGETED_FIXED = "PRIME_TARGETED_FIXED"
    PRIME_UNTARGETED = "PRIME_UNTARGETED"


class VisitStatusEntryMixin(str, _core.EnumNodeMixin, _core.ScalarNode):
    @classmethod
    def asdf_container(cls) -> type:
        from ..meta import Visit

        return Visit

    @classmethod
    def asdf_property_name(cls) -> str:
        return "status"


class VisitStatusEntry(VisitStatusEntryMixin, Enum, metaclass=_core.NodeEnumMeta):
    """
    Enum for the possible entries for status in visit
    """

    DATALOSS = "DATALOSS"
    SUCCESSFUL = "SUCCESSFUL"
    UNSUCCESSFUL = "UNSUCCESSFUL"
