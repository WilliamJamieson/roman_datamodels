from abc import ABC, abstractmethod
from inspect import signature
from typing import TypeVar, get_args

from ._asdf_schema import RadSchema
from ._base import RadNodeMixin
from ._schema import SchemaMixin
from ._utils import camel_case_to_snake_case

__all__ = [
    "ImpliedNodeMixin",
]

_T = TypeVar("_T")


class ImpliedNodeMixin(RadNodeMixin[_T], ABC):
    """
    Mixin for nodes that are implied by other nodes.

    These nodes should have names following the convention:
        <implying_node_name>_<camel_case(implied_property_name)>
    """

    @classmethod
    @abstractmethod
    def asdf_implied_by(cls) -> type[SchemaMixin[_T]]:
        """The name of the field that implies this node."""

    @classmethod
    def asdf_implied_property_name(cls) -> str:
        """The name of the property that implies this node."""

        return camel_case_to_snake_case(cls.__name__.split("_")[-1])

    @classmethod
    def asdf_implied_property(cls) -> property:
        """Get the raw property object that will accept this node"""

        implied: property = getattr(cls.asdf_implied_by(), cls.asdf_implied_property_name())
        return implied

    @classmethod
    def asdf_property_container(cls) -> type | None:
        """The container class used by the property that implies this node."""
        from ..core import DNode, LNode

        sig = signature(lambda: cls.asdf_implied_property().fget).return_annotation

        if args := get_args(sig):
            container: type = args[0]
            element: type = args[1]
            # container, element = args

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

    # TODO: Figure out why I need to redefine this here
    @property
    def schema(self) -> RadSchema:
        """Get the schema for this instance."""
        return self.asdf_schema()
