from abc import ABC, abstractmethod

from ..core import AsdfNodeMixin, get_config

__all__ = ["ArrayFieldMixin", "RadNodeMixin"]


class RadNodeMixin(AsdfNodeMixin, ABC):
    """
    Mixin for direct interaction with RAD nodes.
    """

    @classmethod
    @abstractmethod
    def asdf_schema(cls) -> dict:
        """Get the schema in rad for this class."""


class ArrayFieldMixin(ABC):
    """
    Mixin for objects that have arrays
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
