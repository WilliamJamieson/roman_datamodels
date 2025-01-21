from __future__ import annotations

import datetime
import re
from abc import ABC, abstractmethod
from collections.abc import Callable, Generator, Iterator, MutableMapping
from inspect import signature
from typing import TYPE_CHECKING, Annotated, Any, TypeVar

import numpy as np
from asdf import AsdfFile
from asdf.lazy_nodes import AsdfDictNode, AsdfListNode
from asdf.tags.core import ndarray
from astropy.time import Time

from ._mixins import AsdfNodeMixin, FlushOptions

if TYPE_CHECKING:
    from ..rad import TagMixin

__all__ = [
    "AdditionalNodeMixin",
    "DNode",
    "MissingFieldError",
    "PatternDNode",
]

_T = TypeVar("_T")


class MissingFieldError(AttributeError):
    """Error when a field is attempted to be accessed but is missing"""


# Once we are >3.11 -> DNode[T] can replace the Generic[T] in the class definition
class DNode(AsdfNodeMixin[_T], MutableMapping[str, _T]):
    """
    Base class describing all "object" (dict-like) data nodes for STNode classes.
    """

    _fields: tuple[str, ...] | None = None
    _field_signatures: dict[str, type] | None = None

    def _pre_initialize_node(self, init: dict[str, Any] | DNode[_T] | None = None, **kwargs: Any) -> Any:
        """Preprocessing for initialization of the node"""

        return init

    def _post_initialize_node(self) -> None:
        """Postprocessing for initialization of the node"""
        pass

    def __init__(self, node: dict[str, Any] | DNode[_T] | None = None, **kwargs: Any) -> None:
        node = self._pre_initialize_node(node, **kwargs)

        # Handle if we are passed different data types
        if node is None:
            self._data: dict[str, _T] = {}
        elif isinstance(node, dict | AsdfDictNode):
            self._data = node
        elif isinstance(node, DNode):
            self._data = node._data
        else:
            raise ValueError(f"Initializer only accepts dict-like, not {type(node)}")

        self._post_initialize_node()

    def __class_getitem__(cls, item_type: _T) -> DNode[_T]:
        """Enable type hinting for the class"""

        # Annotated for __class_getitem__ does not quite work in MyPy
        # see python/mypy#11501
        return Annotated[cls, item_type]  # type: ignore[return-value]

    @classmethod
    def _extra_fields(self) -> tuple[str, ...]:
        """List of extra fields that are not in the schema."""
        return tuple()

    @property
    def fields(self) -> tuple[str, ...]:
        """
        Get the keys of the node as defined by the schema
            Note this only works on instances
            (not sure why I can't get it to work on the class)
        """
        from ..rad import get_node_fields

        if self._fields is None:
            self._fields = get_node_fields(type(self)) + type(self)._extra_fields()

        return self._fields

    def field_signature(self, key: str) -> type:
        """
        The field signatures for the node.
        """
        # Make change upfront as the key will be reused several times
        key = self._to_field_key(key)

        # Note we cache these as inspect an be expensive
        if key not in self.fields:
            raise KeyError(f"{key} is not a schema field for {type(self)}")

        if self._field_signatures is None:
            self._field_signatures = {}

        if key not in self._field_signatures:
            self._field_signatures[key] = signature(getattr(type(self), key).fget).return_annotation

        return self._field_signatures[key]

    def _wrap_into_node(self, key: str, value: Any | _T, wrap: bool = True) -> Any:
        """
        Wrap things into node containers if necessary.
        """
        from ..rad import wrap_into_node

        if self._to_field_key(key) in self.fields and wrap:
            # Get the return signature for the field property
            return wrap_into_node(value, self.field_signature(key))

        return value

    def _has_node(self, key: str) -> bool:
        """
        Check if a node exists in the dictionary.
        """
        return self._to_schema_key(key) in self._data

    # Technical Liskov substitution principle violation from MutableMapping
    # -> however in our case our keys are always strings
    def __contains__(self, key: str) -> bool:  # type: ignore[override]
        return self._has_node(key)

    def _pull_node(self, key: str, wrap: bool = True) -> _T:
        """
        Get a node from the dictionary, wrapping if necessary.
        """
        if self._has_node(key):
            value = self._data[self._to_schema_key(key)]
            # Save currently stored value's type for comparison
            stored_type = type(value)
            value = self._wrap_into_node(key, value, wrap=wrap)

            # If the stored type is different from the coerced type, update the stored value
            # so coercion only happens once
            if stored_type is not type(value):
                self._data[self._to_schema_key(key)] = value

            return value

        raise MissingFieldError(f"No such attribute ({key}) found in node")

    def __getattr__(self, key: str) -> _T:
        """
        Permit accessing dict keys as attributes, assuming they are legal Python
        variable names.
        """
        # Private values should have already been handled by the __getattribute__ method
        #   bail out if we are falling back on this method
        if key.startswith("_"):
            raise AttributeError(f"No attribute {key}")

        return self._pull_node(key)

    def __getitem__(self, key: str) -> _T:
        """Dictionary style access data"""
        # Try to directly access the attribute
        try:
            return self._pull_node(key)

        except MissingFieldError as err:
            # For lazy nodes, we need to check if the key is in the fields and
            # grab the value from the property
            if self._to_field_key(key) in self.fields:
                value: _T = getattr(self, key)
                return value

            raise err

    def _check_key(self, key: str) -> bool:
        """
        Check if the key is settable
        """
        return self._to_schema_key(key) in self._data or self._to_field_key(key) in self.fields

    def _set_node(self, key: str, value: _T, check: bool = True, wrap: bool = True) -> None:
        """
        Attempt to set a value in for the node, wrapping data if necessary.
        """
        # Private keys should just be in the normal __dict__
        if key[0] == "_":
            self.__dict__[key] = value
        else:
            if check and not self._check_key(key):
                raise AttributeError(f"No such attribute ({key}) found in node")

            self._data[self._to_schema_key(key)] = self._wrap_into_node(key, value, wrap=wrap)

    def __setattr__(self, key: str, value: _T) -> None:
        """
        Permit assigning dict keys as attributes.
        """
        self._set_node(key, value)

    def __setitem__(self, key: str, value: _T) -> None:
        """Dictionary style access set data"""
        self._set_node(key, value, check=False, wrap=False)

    def _get_node(self, key: str, default: Callable[[], _T]) -> _T:
        """
        Get a node and if not found construct it with the default value.

        Note: This is what creates the lazy instantiation of the default values
        This is what all the schema related properties should use to get their values.

        Parameters
        ----------
        key : str
            The key to look for in the dictionary.
        default : Callable
            The constructor for a default. Its callable to allow for lazy instantiation.
            This will often take the form of a lambda, that way the argument to the lambda
            is not evaluated until the default is actually needed, saving time and memory.
            for things like numpy arrays.
        """

        if not self._has_node(key):
            self._set_node(key, default())

        return self._pull_node(key)

    def _recursive_items(self) -> Generator[tuple[str, _T], None, None]:
        from ._l_node import LNode

        def recurse(tree: Any, path: list[Any] | None = None) -> Generator[tuple[str, _T], None, None]:
            path = path or []  # Avoid mutable default arguments
            if isinstance(tree, DNode | dict | AsdfDictNode):
                for key, val in tree.items():
                    yield from recurse(val, [*path, key])
            # This is actually reacable, but MyPy cannot determine this statically
            # because we are passing the object itself into the function
            elif isinstance(tree, LNode | list | tuple | AsdfListNode):  # type: ignore[unreachable]
                for i, val in enumerate(tree):
                    yield from recurse(val, [*path, i])
            elif tree is not None:
                yield (".".join(str(x) for x in path), tree)

        yield from recurse(self)

    def to_flat_dict(self, include_arrays: bool = True, recursive: bool = False) -> dict[str, _T]:
        """
        Returns a dictionary of all of the schema items as a flat dictionary.

        Each dictionary key is a dot-separated name.  For example, the
        schema element ``meta.observation.date`` will end up in the
        dictionary as::

            { "meta.observation.date": "2012-04-22T03:22:05.432" }

        """

        def convert_val(val: Any) -> Any:
            """
            Unwrap the tagged scalars if necessary.
            """
            if isinstance(val, datetime.datetime):
                return val.isoformat()
            elif isinstance(val, Time):
                return str(val)
            return val

        item_getter = self._recursive_items if recursive else self.items

        if include_arrays:
            return {key: convert_val(val) for (key, val) in item_getter()}
        else:
            return {
                key: convert_val(val) for (key, val) in item_getter() if not isinstance(val, np.ndarray | ndarray.NDArrayType)
            }

    def __len__(self) -> int:
        """Define length of the node"""
        return len(self._data)

    def __delitem__(self, key: str) -> None:
        """Dictionary style access delete data"""
        del self._data[self._to_schema_key(key)]

    def __iter__(self) -> Iterator[str]:
        """Define iteration"""
        return iter(self._data)

    def _repr_order(self) -> list[str]:
        """
        Representation order for the node
        """
        keys = list(self._data.keys())
        keys.sort()
        return keys

    def __repr__(self) -> str:
        """Define a representation"""
        keys = list(self._data.keys())
        keys.sort()
        return repr({key: self._data[key] for key in keys})

    def copy(self) -> DNode[_T]:
        """Handle copying of the node"""
        instance = self.__class__.__new__(self.__class__)
        instance.__dict__.update(self.__dict__.copy())
        instance.__dict__["_data"] = self.__dict__["_data"].copy()

        return instance

    def unwrap(self) -> dict[str, _T]:
        return dict(self)

    def to_asdf_tree(
        self, ctx: AsdfFile, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False
    ) -> dict[str, dict[str, Any] | list[Any] | Any | _T | TagMixin[_T]]:
        from ..rad import TagMixin

        return {
            key: value.to_asdf_tree(ctx, flush=flush, warn=warn)
            # Only wrap if it is an AsdfNode, but not tagged,
            # ASDF will handle the tagged objects in the tree
            # itself
            if isinstance(value, AsdfNodeMixin) and not isinstance(value, TagMixin)
            else value
            for key, value in self.items()
        }

    def __asdf_traverse__(self) -> dict[str, _T]:
        """Asdf traverse method for things like info/search"""
        return self.unwrap()

    def __eq__(self, other: Any) -> bool:
        """Equality check"""
        if not isinstance(other, DNode):
            return False

        return self._data == other._data


class PatternDNode(DNode[_T], ABC):
    """
    Support for pattern nodes.
    """

    @classmethod
    @abstractmethod
    def asdf_key_pattern(cls) -> str:
        """
        Get the key pattern for the node.
        """

    def _check_key(self, key: str) -> bool:
        if re.match(self.asdf_key_pattern(), key):
            return True

        return super()._check_key(key)


class AdditionalNodeMixin(DNode[_T], ABC):
    """
    Base class for all mixin classes.
    """
