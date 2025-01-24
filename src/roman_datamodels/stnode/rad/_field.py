import threading
import warnings
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeAlias, TypeVar, cast

from ..core import DNode, type_checked
from ._tagged import TaggedObjectNode

__all__ = ["FIELD_REGISTRY", "FieldPropertyWarning", "Node", "field"]

_T = TypeVar("_T")


class FieldPropertyWarning(UserWarning):
    """
    Warning to be raised by a field property during its introspection
    """


def _default(function: Callable[[DNode[Any]], _T]) -> Callable[[DNode[Any]], _T]:
    """
    Wrap the function (which was defined like a property) on an ObjectNode so that
    two things are checked:
        1. Perform a check on the ObjectNode instance to provide a warning if the
           instance is not on the latest tag.
        2. Add a type check wrapper method which is only active during certain
           testing conditions (falling back on a no-op identity decorator when
           not testing).
    The resulting function will be used as a default value producer for the property
    on the node
    """

    @wraps(function)
    def wrapper(self: DNode[Any]) -> _T:
        """
        Raises a warning if the tag does not match the latest one
        """
        if isinstance(self, TaggedObjectNode) and self._tag != self.asdf_tag_uri():
            msg = (
                f"Node is not on the latest tag: {self._tag} != {self.asdf_tag_uri()} "
                "and a default value is being created.\n"
                "This may result in a value that is inconsistent with the tag used, "
                "indeed this field may not even be present in the tag's schema!"
            )
            warnings.warn(msg, FieldPropertyWarning, stacklevel=2)

        return type_checked(function)(self)

    return wrapper


class _FieldRegistry:
    """
    Registry of all the active fields in the nodes
    """

    def __init__(self) -> None:
        self._fields: dict[str, set[str]] = {}
        self._lock = threading.RLock()

    def add_field(self, field: Callable[[DNode[Any]], _T]) -> None:
        """
        Add a field to the registry
        """
        with self._lock:
            name = field.__name__
            cls_name = field.__qualname__.split(".")[0]

            if cls_name not in self._fields:
                self._fields[cls_name] = set()

            if name in self._fields[cls_name]:
                raise ValueError(f"Field {name} already exists on {cls_name}")

            self._fields[cls_name].add(name)

    def get_fields(self, cls: type) -> set[str]:
        fields = self._fields.get(cls.__name__, set())
        for base in cls.__bases__:
            fields |= self._fields.get(base.__name__, set())

        return fields


FIELD_REGISTRY = _FieldRegistry()


def field(function: Callable[[DNode[Any]], _T]) -> Callable[[DNode[Any]], _T]:
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
    FIELD_REGISTRY.add_field(function)

    @wraps(function)
    def wrapper(self: DNode[Any]) -> _T:
        """
        Wrap the function (which is defined on the node) to handle getting the value
        from the node and then falling back on evaluating the function itself to
        get, set, and then return the default value.
        """

        # Note the lambda is used to delay the evaluation of the default value all the way
        # until the default is actually needed. This is important for things like numpy arrays
        # which can be expensive to create (memory and time wise).
        return cast(_T, self._get_node(function.__name__, lambda: _default(function)(self)))

    return wrapper


Node: TypeAlias = DNode[Any]
