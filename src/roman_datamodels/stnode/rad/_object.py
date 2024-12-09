import warnings
from abc import ABC, abstractmethod

from asdf import AsdfFile

from ..core import DNode, FlushOptions, get_config
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
    def asdf_required(cls) -> set[str]:
        """List of required fields in this node."""
        return cls.asdf_schema().required

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
                fields = self.asdf_required()
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

    def to_asdf_tree(self, ctx: AsdfFile, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> dict:
        # Flush out any required fields
        self.flush(flush, warn)
        return super().to_asdf_tree(ctx, flush=flush, warn=warn)


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
    def primary_array_name(self) -> str:
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        if "data" in self.asdf_required():
            return "data"

        raise NotImplementedError("Primary array name not defined")

    @property
    def primary_array_shape(self) -> tuple[int] | None:
        """Shape of the primary array."""

        if self._has_node(name := self.primary_array_name):
            return getattr(self, name).shape

        return None

    @property
    @abstractmethod
    def default_array_shape(self) -> tuple[int]:
        """Default shape of the data array."""

    @property
    @abstractmethod
    def testing_array_shape(self) -> tuple[int]:
        """Shape of the data array for testing."""

    @property
    def array_shape(self) -> tuple[int]:
        """Shape of the data array."""

        if get_config().use_test_array_shape:
            return self.testing_array_shape

        if shape := self.primary_array_shape:
            return shape

        return self.default_array_shape
