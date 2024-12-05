from abc import ABC, abstractmethod
from enum import StrEnum, auto

import asdf

__all__ = [
    "AdditionalNodeMixin",
    "AsdfNodeMixin",
    "FlushOptions",
]


class FlushOptions(StrEnum):
    """
    Options for flushing out required fields
        NONE     -> Do not flush out any fields,
                    - this may result in an invalid object for asdf writing
        REQUIRED -> Flush out only the required fields with their default values
        ALL      -> Flush out all fields with their default values,
                    - this fills in all the fields listed in the schema with
                      their default values
        EXTRA    -> Flush out all fields with their default values including
                    extra fields that are not listed in the schema
                    - fills in everything from ALL, then fills in fields that
                      are mixedin to the object which have defaults but are not
                      listed in the schema
    """

    NONE = auto()
    REQUIRED = auto()
    ALL = auto()
    EXTRA = auto()


class AsdfNodeMixin(ABC):
    """Mixin so that Nodes can have an asdf context."""

    _ctx: asdf.AsdfFile | None = None

    @classmethod
    def asdf_ctx(cls) -> asdf.AsdfFile:
        """Get the asdf context for the class."""
        if cls._ctx is None:
            cls._ctx = asdf.AsdfFile()

        return cls._ctx

    @property
    def ctx(self) -> asdf.AsdfFile:
        """Get the asdf context for the instance."""
        return self.asdf_ctx()

    @abstractmethod
    def __asdf_traverse__(self):
        """Traverse the object to create the tree for the ASDF file."""

    @abstractmethod
    def unwrap(self):
        """
        Unwrap the current object into its native Python form.
            -> dict
            -> list
            -> base scalar

        Returns
        -------
        The data wrapped by the node
        """

    @abstractmethod
    def to_asdf_tree(self, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False):
        """
        Convert the object into a form that can be written to an ASDF file.
            -> flush out any required fields
            -> traverse the container and recursively convert not-tagged objects

        Parameters
        ----------
        flush : FlushOptions
            Options for flushing out required fields, see FlushOptions for more info
        warn : bool
            If `True`, warn if any required fields are missing.

        Returns
        -------
        unwrapped version of object ready to be written to ASDF file
        """


class AdditionalNodeMixin:
    """
    Base class for all mixin classes.
    """
