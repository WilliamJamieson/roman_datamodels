from abc import ABC, abstractmethod
from typing import TypeVar

from ._asdf_schema import RadSchema
from ._base import RadNodeMixin
from ._node import ListNode, ObjectNode, ScalarNode

__all__ = [
    "SchemaListNode",
    "SchemaMixin",
    "SchemaObjectNode",
    "SchemaScalarNode",
]

_T = TypeVar("_T")


class SchemaMixin(RadNodeMixin[_T], ABC):
    """Mixin for nodes to support linking to a schema."""

    @classmethod
    @abstractmethod
    def asdf_schema_uris(cls) -> tuple[str, ...]:
        """URI of the schema that defines this node."""

    @classmethod
    def asdf_schema_uri(cls) -> str:
        """
        The latest schema for this class.
        """
        return cls.asdf_schema_uris()[-1]

    @property
    def schema_uri(self) -> str:
        """
        The schema_uri for this instance.
        -> Note we cannot determine the schema_uri for an untagged node from
           the asdf file.
        """
        return self.asdf_schema_uri()

    @classmethod
    def asdf_schema(cls) -> RadSchema:
        """
        The latest schema for this class.
        """
        return RadSchema.from_class(cls.asdf_schema_uri())

    @property
    def schema(self) -> RadSchema:
        """
        The schema for this instance.
        """
        return RadSchema.from_class(self.schema_uri)


class SchemaObjectNode(ObjectNode[_T], SchemaMixin[_T], ABC):
    """
    Base class for all objects described by their own schema in RAD.
    """


class SchemaListNode(ListNode[_T], SchemaMixin[_T], ABC):
    """
    Base class for all list nodes described by their own schema in RAD.
    """


class SchemaScalarNode(ScalarNode[_T], SchemaMixin[_T], ABC):
    """
    Base class for all scalars that are described by their own schema in RAD.
    """
