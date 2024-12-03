from abc import ABC, abstractmethod

from .._base import DNode
from ._mixins import SchemaMixin, TagMixin

__all__ = [
    "DataModelNode",
    "ObjectNode",
    "SchemaObjectNode",
    "TaggedObjectNode",
]


class ObjectNode(DNode, ABC):
    @classmethod
    @abstractmethod
    def asdf_required(cls) -> tuple[str]:
        """List of required fields in this node."""

    @property
    def required(self) -> tuple[str]:
        return self.asdf_required()


class SchemaObjectNode(ObjectNode, SchemaMixin, ABC): ...


class TaggedObjectNode(SchemaObjectNode, TagMixin, ABC): ...


class DataModelNode(TaggedObjectNode, ABC):
    @property
    @abstractmethod
    def array_shape(self) -> tuple[int]:
        """Shape of the data array."""
