from abc import ABC, abstractmethod
from enum import StrEnum, auto
from typing import Any, Generic, TypeVar

from asdf import AsdfFile

__all__ = [
    "AsdfNodeMixin",
    "FlushOptions",
    "NodeKeyMixin",
]

_T = TypeVar("_T")


class NodeKeyMixin:
    """
    Mixin to enable correct handling of node keys vs field keys
    -> pass vs pass_ issue
    """

    @staticmethod
    def _to_schema_key(key: str) -> str:
        """
        This exists to make it so that the _data storage always
        uses "pass" instead of "pass_" as the key.

        This is a workaround for the fact that "pass" is a very
        reserved word in Python and can't be used as function name
        for example.

        Note that this means that "pass_" and "pass" will be equivalent
        for the purposes of DNode.

        Any time we access self._data this should be used to make sure
        pass is correctly handled.
        """
        return "pass" if key == "pass_" else key

    @staticmethod
    def _to_field_key(key: str) -> str:
        """
        Matching to _handle_data_key, this is used to make sure that
        when we are using keys in reference to property (fields) names that
        "pass_" is used instead of "pass".

        Anytime fields is accessed this should be used to make sure pass is correctly handled.
        """

        return "pass_" if key == "pass" else key


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


class AsdfNodeMixin(NodeKeyMixin, Generic[_T], ABC):
    """Mixin so that Nodes can have an asdf context."""

    @abstractmethod
    def __asdf_traverse__(self) -> dict[str, _T] | list[_T] | _T:
        """Traverse the object to create the tree for the ASDF file."""

    @abstractmethod
    def unwrap(self) -> dict[str, _T] | list[_T] | _T:
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
    def to_asdf_tree(
        self, ctx: AsdfFile, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False
    ) -> dict[str, Any] | list[Any] | Any:
        """
        Convert the object into a form that can be written to an ASDF file.
            -> flush out any required fields
            -> traverse the container and recursively convert not-tagged objects

        Parameters
        ----------
        ctx : AsdfFile
            The ASDF context to use for the conversion
        flush : FlushOptions
            Options for flushing out required fields, see FlushOptions for more info
        warn : bool
            If `True`, warn if any required fields are missing.

        Returns
        -------
        unwrapped version of object ready to be written to ASDF file
        """
