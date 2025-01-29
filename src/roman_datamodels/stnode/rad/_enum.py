from abc import ABC, ABCMeta, abstractmethod
from enum import Enum, EnumType

from ._asdf_schema import RadSchema
from ._schema import SchemaMixin

__all__ = [
    "EnumNodeMixin",
    "NodeEnumMeta",
    "RadEnum",
]


class EnumNodeMixin(ABC):
    """
    Mixin for nodes that are enums.

    NOTE: due to mixins with built in classes (think str) ABC enforcement goes away.
          asdf_schema needs to be implemented by the enum node class itself.
          simply point this at the property that contains the enum
    """

    @classmethod
    @abstractmethod
    def asdf_container(cls) -> type[SchemaMixin]:
        """
        A class which has a property that evaluates to the enum
        """

    @classmethod
    @abstractmethod
    def asdf_property_name(cls) -> str:
        """
        The name of the property that contains the enum
        """

    @classmethod
    def asdf_schema(cls) -> RadSchema:
        """Get the schema for the enum node"""
        schema = cls.asdf_container().asdf_schema().fields[cls.asdf_property_name()]
        if "anyOf" in schema.schema:
            return RadSchema(schema.schema["anyOf"][0]["enum"])

        return RadSchema(schema.get_key("enum")[0])


class RadEnum(Enum):
    def __repr__(self) -> str:
        return repr(self.value)


class NodeEnumMeta(ABCMeta, EnumType):
    """
    Meta class for enums of nodes

    Since all nodes are ABC classes they have ABCMeta as their metaclass. But
    Enum classes have EnumType (used to be EnumMeta) as their metaclass. This
    makes it so that the enum classes cannot be ABC classes due to a metaclass
    conflict. This metaclass resolves that conflict by inheriting from both
    enabling the use of the enum
    """
