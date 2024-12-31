import warnings
from abc import ABC
from collections.abc import Callable
from enum import Enum
from functools import wraps
from typing import Any, TypeVar

from asdf import AsdfFile

from ..core import DNode, FlushOptions, LNode, get_config, type_checked
from ._base import RadNodeMixin
from ._utils import get_node_fields

__all__ = [
    "ListNode",
    "ObjectNode",
    "ScalarNode",
    "field",
    "field_property",
]

T = TypeVar("T")


class ObjectNode(DNode, RadNodeMixin, ABC):
    @classmethod
    def asdf_required(cls) -> set[str]:
        """List of required fields in this node."""
        return cls.asdf_schema().required

    def flush(self, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False, recurse: bool = False) -> None:
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
        recurse : bool
            If we recurese the flush into subnodes

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
                field_value = getattr(self, field)
                if recurse and isinstance(field_value, ObjectNode):
                    field_value.flush(flush=flush, warn=warn, recurse=recurse)

    def to_asdf_tree(self, ctx: AsdfFile, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> dict:
        # Flush out any required fields
        self.flush(flush, warn)
        return super().to_asdf_tree(ctx, flush=flush, warn=warn)

    def __asdf_traverse__(self):
        return self.to_asdf_tree(ctx=get_config().asdf_ctx, flush=FlushOptions.REQUIRED, warn=False)


class ListNode(LNode, RadNodeMixin, ABC):
    """
    Base class for all list nodes
    """


class ScalarNode(RadNodeMixin, ABC):
    """
    Base class for all scalars with descriptions in RAD
    -> this is for enums that are not tagged
    """

    def unwrap(self) -> Any:
        base = self.value if isinstance(self, Enum) else self

        return type(base).__bases__[0](base)

    def to_asdf_tree(self, ctx: AsdfFile, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> Any:
        return self.unwrap()

    def __asdf_traverse__(self):
        return self.to_asdf_tree(ctx=get_config().asdf_ctx, flush=FlushOptions.REQUIRED, warn=False)


class field_property(property):
    """
    Special subclass of property to mark schema fields out
    """


def field(function: Callable[[DNode], T]) -> field_property:
    """
    Create a special property decorator for node methods that does several
    things:
        1. Marks them out as `field_property` so that they can be identified as
           schema fields.
        2. Wraps the method itself so that it acts a a pure default value
           producer, using the value in the node before falling back on the method
           itself to get the default value.
        3. Adds a type check wrapper method which is only active during certain
           testing conditions (falling back on a no-op identity decorator when
           not testing).
    """

    @wraps(function)
    def wrapper(self: DNode, *args, **kwargs):
        """
        Wrap the function (which is defined on the node) to handle getting the value
        from the node and then falling back on evaluating the function itself to
        get, set, and then return the default value.
        """

        # Note the lambda is used to delay the evaluation of the default value all the way
        # until the default is actually needed. This is important for things like numpy arrays
        # which can be expensive to create (memory and time wise).
        return self._get_node(function.__name__, lambda: type_checked(function)(self, *args, **kwargs))

    return field_property(wrapper)
