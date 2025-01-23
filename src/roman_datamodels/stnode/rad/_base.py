from abc import ABC, abstractmethod
from textwrap import indent
from typing import TypeVar

from ..core import AsdfNodeMixin, DNode, get_config
from ._asdf_schema import RadSchema

__all__ = [
    "ArrayFieldMixin",
    "RadNodeMixin",
]

_T = TypeVar("_T")


class RadNodeMixin(AsdfNodeMixin[_T], ABC):
    """
    Mixin for direct interaction with RAD nodes.
    """

    @classmethod
    @abstractmethod
    def asdf_schema(cls) -> RadSchema:
        """Get the schema in rad for this class."""

    @classmethod
    def fill_docs(cls) -> None:
        """Fill in the docstrings for the class."""
        docstring = indent(cls.asdf_schema().docstring, "    ")
        if cls.__doc__:
            docstring = f"{cls.__doc__}\n\n{docstring}"

        cls.__doc__ = docstring


class ArrayFieldMixin(DNode[_T], ABC):
    """
    Mixin for objects that have arrays
    """

    @classmethod
    @abstractmethod
    def asdf_required(cls) -> set[str]:
        """List of required fields in this node."""

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
    def primary_array_shape(self) -> tuple[int, ...] | None:
        """Shape of the primary array."""

        if self._has_node(name := self.primary_array_name):
            shape: tuple[int, ...] = getattr(self, name).shape
            return shape

        return None

    @property
    def _largest_array_shape_(self) -> tuple[int, ...] | None:
        """
        Shape of the primary array for the array_shape property.
        -> Normally the largest in dimension array is the primary array,
           but sometimes this is not the case. This property allows for
           a model to override this behavior
        """
        return self.primary_array_shape

    @property
    @abstractmethod
    def default_array_shape(self) -> tuple[int, ...]:
        """Default shape of the data array."""

    @property
    @abstractmethod
    def testing_array_shape(self) -> tuple[int, ...]:
        """Shape of the data array for testing."""

    @property
    def array_shape(self) -> tuple[int, ...]:
        """The full shape of the largest (in dimension) array in the model."""

        if self._array_shape_ is not None:
            return self._array_shape_

        if get_config().use_test_array_shape:
            return self.testing_array_shape

        if shape := self._largest_array_shape_:
            return shape

        return self.default_array_shape
