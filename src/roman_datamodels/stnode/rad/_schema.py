from abc import ABC, abstractmethod

from ._asdf_schema import RadSchema
from ._base import RadNodeMixin
from ._node import ListNode, ObjectNode, ScalarNode

__all__ = [
    "SchemaListNode",
    "SchemaMixin",
    "SchemaObjectNode",
    "SchemaScalarNode",
]


class SchemaMixin(RadNodeMixin, ABC):
    """Mixin for nodes to support linking to a schema."""

    @classmethod
    @abstractmethod
    def asdf_schema_uri(clas) -> str:
        """URI of the schema that defines this node."""

    @classmethod
    def asdf_schema(cls) -> RadSchema:
        # Pull the schema through ASDF
        return RadSchema.from_class(cls.asdf_schema_uri())


class SchemaObjectNode(ObjectNode, SchemaMixin, ABC):
    """
    Base class for all objects described by their own schema in RAD.
    """


class SchemaListNode(ListNode, SchemaMixin, ABC):
    """
    Base class for all list nodes described by their own schema in RAD.
    """


class SchemaScalarNode(ScalarNode, SchemaMixin, ABC):
    """
    Base class for all scalars that are described by their own schema in RAD.
    """
