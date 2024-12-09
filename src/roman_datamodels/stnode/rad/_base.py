from abc import ABC, abstractmethod

from ..core import AsdfNodeMixin

__all__ = ["RadNodeMixin"]


class RadNodeMixin(AsdfNodeMixin, ABC):
    """
    Mixin for direct interaction with RAD nodes.
    """

    @classmethod
    @abstractmethod
    def asdf_schema(cls) -> dict:
        """Get the schema in rad for this class."""
