import warnings
from abc import ABC, abstractmethod

from .._base import DNode
from ._mixins import SchemaMixin, TagMixin
from ._utils import get_node_fields

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

    def flush_out_required(self, warn: bool = False) -> None:
        """
        Flush out the required fields.
            This will be used by asdf to ensure that all required fields are present
            prior to writing the tree to disk. These objects are intended to be
            filled in lazily, so this method will fill in any missing required fields
            making sure that the object is in a valid state for writing to disk.

        Parameters
        ----------
        warn : bool
            If `True`, warn if any required fields are missing.

        Results
        -------
        All required fields are flushed out with their default values.
        """

        for field in self.required:
            if not self._has_node(field):
                if warn:
                    warnings.warn(f"Filling in missing required field '{field}' with default value.", UserWarning, stacklevel=2)
                getattr(self, field)

    def flush_out_all(self, warn: bool = False) -> None:
        """
        Flush out all fields.

        Parameters
        ----------
        warn : bool
            If `True`, warn if any fields are missing.

        Results
        -------
        All fields are flushed out with their default values.
        """

        for field in get_node_fields(type(self)):
            if not self._has_node(field):
                if warn:
                    warnings.warn(f"Filling in missing field '{field}' with default value.", UserWarning, stacklevel=2)
                getattr(self, field)


class SchemaObjectNode(ObjectNode, SchemaMixin, ABC): ...


class TaggedObjectNode(SchemaObjectNode, TagMixin, ABC): ...


class DataModelNode(TaggedObjectNode, ABC):
    @property
    @abstractmethod
    def array_shape(self) -> tuple[int]:
        """Shape of the data array."""
