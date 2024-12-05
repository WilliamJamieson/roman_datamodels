from abc import ABC, abstractmethod
from inspect import signature
from typing import get_args

from ._utils import camel_case_to_snake_case

__all__ = [
    "ImpliedNodeMixin",
    "SchemaMixin",
    "TagMixin",
]


class SchemaMixin(ABC):
    """Mixin for nodes to support linking to a schema."""

    @classmethod
    @abstractmethod
    def asdf_schema_uri(clas) -> str:
        """URI of the schema that defines this node."""

    @property
    def schema_uri(self):
        """Get the URI for this instance"""
        return self.asdf_schema_uri()


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
        return cls.asdf_ctx().extension_manager.get_tag_definition(cls.asdf_tag()).schema_uris[0]


class ImpliedNodeMixin(ABC):
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
    def asdf_implied_property(cls) -> property:
        """The name of the property that implies this node."""

        return getattr(cls.asdf_implied_by(), camel_case_to_snake_case(cls.__name__.split("_")[-1]))

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
