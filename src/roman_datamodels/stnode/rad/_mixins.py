from abc import ABC, ABCMeta, abstractmethod
from enum import EnumType
from inspect import signature
from pathlib import Path
from typing import get_args

from ..core import AsdfNodeMixin
from ._schema import RadSchema
from ._utils import camel_case_to_snake_case

__all__ = [
    "EnumNodeMixin",
    "ImpliedNodeMixin",
    "NodeEnumMeta",
    "SchemaMixin",
    "TagMixin",
]


class RadNodeMixin(AsdfNodeMixin, ABC):
    """
    Mixin for direct interaction with RAD nodes.
    """

    @classmethod
    @abstractmethod
    def asdf_schema(cls) -> dict:
        """Get the schema in rad for this class."""


class SchemaMixin(RadNodeMixin, ABC):
    """Mixin for nodes to support linking to a schema."""

    @classmethod
    @abstractmethod
    def asdf_schema_uri(clas) -> str:
        """URI of the schema that defines this node."""

    @property
    def schema_uri(self):
        """Get the URI for this instance"""
        return self.asdf_schema_uri()

    @classmethod
    def asdf_schema(cls) -> RadSchema:
        # Pull the schema through ASDF
        return RadSchema(cls.get_schema(cls.asdf_schema_uri()))


class TagMixin(SchemaMixin, ABC):
    """Mixin for nodes to support linking to a tag."""

    @classmethod
    @abstractmethod
    def asdf_tag(cls) -> str:
        """Tag of the node."""

    @property
    def tag(self) -> str:
        """Get the tag for this instance."""
        return self.asdf_tag()

    @classmethod
    def asdf_schema_uri(cls) -> str:
        """Get the schema URI for the class using the asdf_tag"""
        from ._scalar import TaggedScalarNode

        head, tail = cls.asdf_tag().split("tags")

        head = Path(head.split("asdf://")[-1]) / "schemas"  # remove the asdf:// as it gets messed up by Path
        tail = Path(tail[1:])  # remove the leading '/' as it messes with recombination

        if issubclass(cls, TaggedScalarNode):
            tail = tail.parent / "tagged_scalars" / tail.name

        return f"asdf://{head / tail}"  # recombine the paths and add the asdf:// back


class ImpliedNodeMixin(RadNodeMixin, ABC):
    """
    Mixin for nodes that are implied by other nodes.

    These nodes should have names following the convention:
        <implying_node_name>_<camel_case(implied_property_name)>
    """

    @classmethod
    @abstractmethod
    def asdf_implied_by(cls) -> type:
        """The name of the field that implies this node."""

    @classmethod
    def asdf_implied_property_name(cls) -> str:
        """The name of the property that implies this node."""

        return camel_case_to_snake_case(cls.__name__.split("_")[-1])

    @classmethod
    def asdf_implied_property(cls) -> property:
        """Get the raw property object that will accept this node"""

        return getattr(cls.asdf_implied_by(), cls.asdf_implied_property_name())

    @classmethod
    def asdf_property_container(cls) -> type | None:
        """The container class used by the property that implies this node."""
        from .._base import DNode, LNode

        sig = signature(cls.asdf_implied_property().fget).return_annotation

        if args := get_args(sig):
            container, element = args

            if element is not cls:
                raise TypeError(f"Expected {cls} to be the element of {container}")

            if container is DNode or container is LNode:
                return container

            raise TypeError(f"Expected {container} to be a DNode or LNode")
        return None

    @classmethod
    def asdf_schema(cls) -> RadSchema:
        """Get the schema for the implied node"""
        return cls.asdf_implied_by().asdf_schema().fields[cls.asdf_implied_property_name()]


class EnumNodeMixin(ABC):
    """
    Mixin for nodes that are enums.

    NOTE: due to mixins with built in classes (think str) ABC enforcement goes away.
          asdf_schema needs to be implemented by the enum node class itself.
          simply point this at the property that contains the enum
    """

    @classmethod
    @abstractmethod
    def asdf_container(cls) -> type:
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


class NodeEnumMeta(ABCMeta, EnumType):
    """
    Meta class for enums of nodes

    Since all nodes are ABC classes they have ABCMeta as their metaclass. But
    Enum classes have EnumType (used to be EnumMeta) as their metaclass. This
    makes it so that the enum classes cannot be ABC classes due to a metaclass
    conflict. This metaclass resolves that conflict by inheriting from both
    enabling the use of the enum
    """
