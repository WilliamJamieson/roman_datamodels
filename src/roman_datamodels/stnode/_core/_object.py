import warnings
from abc import ABC, abstractmethod

from .._base import DNode, FlushOptions
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

    def flush(self, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> None:
        """
        Flush out the object.
            This will be used by asdf to ensure that all required fields are present
            prior to writing the tree to disk. These objects are intended to be
            filled in lazily, so this method will fill in any missing required fields
            making sure that the object is in a valid state for writing to disk.

        Parameters
        ----------
        flush : FlushOptions
            Options for flushing out required fields, see FlushOptions for more info
        warn : bool
            If `True`, warn if any required fields are missing.

        Results
        -------
        All required fields are flushed out with their default values.
        """
        match flush:
            case FlushOptions.NONE:
                return
            case FlushOptions.REQUIRED:
                fields = self.required
            case FlushOptions.ALL:
                fields = get_node_fields(type(self))
            case FlushOptions.EXTRA:
                fields = get_node_fields(type(self)) + self._extra_fields()
            case _:
                raise ValueError(f"Invalid flush option: {flush}")

        for field in fields:
            if not self._has_node(field):
                if warn:
                    warnings.warn(f"Filling in missing required field '{field}' with default value.", UserWarning, stacklevel=2)
                # access the field to trigger its default value
                getattr(self, field)

    def to_asdf_tree(self, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> dict:
        # Flush out any required fields
        self.flush(flush, warn)
        return super().to_asdf_tree(flush=flush, warn=warn)


class SchemaObjectNode(ObjectNode, SchemaMixin, ABC):
    """
    Base class for all objects described by their own schema in RAD.
    """


class TaggedObjectNode(SchemaObjectNode, TagMixin, ABC):
    """
    Base class for all objects that are tagged in RAD.
    """


class DataModelNode(TaggedObjectNode, ABC):
    """
    Base class for all objects in RAD that are marked as data models
    """

    @property
    @abstractmethod
    def array_shape(self) -> tuple[int]:
        """Shape of the data array."""
