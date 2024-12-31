from __future__ import annotations

import datetime
import re
from abc import ABC, abstractmethod
from collections.abc import Callable, Generator, MutableMapping
from functools import wraps
from inspect import signature
from typing import Annotated, Any, Generic, TypeVar

import numpy as np
from asdf import AsdfFile
from asdf.lazy_nodes import AsdfDictNode, AsdfListNode
from asdf.tags.core import ndarray
from astropy.time import Time

from ._mixins import AsdfNodeMixin, FlushOptions

# from ._typing import type_checked

__all__ = [
    "DNode",
    "MissingFieldError",
    "PatternDNode",
    "field",
    "field_property",
]

T = TypeVar("T")


class MissingFieldError(AttributeError):
    """Error when a field is attempted to be accessed but is missing"""


# Once we are >3.11 -> DNode[T] can replace the Generic[T] in the class definition
class DNode(AsdfNodeMixin, MutableMapping, Generic[T]):
    """
    Base class describing all "object" (dict-like) data nodes for STNode classes.
    """

    _fields: tuple[str] | None = None
    _field_signatures: dict[str, type] | None = None

    def _pre_initialize_node(self, init=None, **kwargs) -> Any:
        """Preprocessing for initialization of the node"""

        return init

    def _post_initialize_node(self) -> None:
        """Postprocessing for initialization of the node"""
        pass

    def __init__(self, node=None, **kwargs) -> None:
        node = self._pre_initialize_node(node, **kwargs)

        # Handle if we are passed different data types
        if node is None:
            self.__dict__["_data"] = {}
        elif isinstance(node, dict | AsdfDictNode):
            self.__dict__["_data"] = node
        elif isinstance(node, DNode):
            self.__dict__["_data"] = node._data
        else:
            raise ValueError(f"Initializer only accepts dict-like, not {type(node)}")

        self._post_initialize_node()

    def __class_getitem__(cls, item_type: type) -> type[DNode[T]]:
        """Enable type hinting for the class"""

        return Annotated[cls, item_type]

    @classmethod
    def _extra_fields(self) -> tuple[str]:
        """List of extra fields that are not in the schema."""
        return tuple()

    @property
    def fields(self) -> tuple[str]:
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

    def _wrap_into_node(self, key: str, value: Any, wrap: bool = True) -> T:
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

    def __contains__(self, key: str) -> bool:
        return self._has_node(key)

    def _pull_node(self, key: str, wrap: bool = True) -> T:
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

    def __getattr__(self, key: str) -> T:
        """
        Permit accessing dict keys as attributes, assuming they are legal Python
        variable names.
        """
        # Private values should have already been handled by the __getattribute__ method
        #   bail out if we are falling back on this method
        if key.startswith("_"):
            raise AttributeError(f"No attribute {key}")

        return self._pull_node(key)

    def __getitem__(self, key: str) -> T:
        """Dictionary style access data"""
        # Try to directly access the attribute
        try:
            return self._pull_node(key)

        except MissingFieldError:
            # For lazy nodes, we need to check if the key is in the fields and
            # grab the value from the property
            if self._to_field_key(key) in self.fields:
                return getattr(self, key)

    def _check_key(self, key: str) -> bool:
        """
        Check if the key is settable
        """
        return self._to_schema_key(key) in self._data or self._to_field_key(key) in self.fields

    def _set_node(self, key: str, value: T, check: bool = True, wrap: bool = True) -> None:
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

    def __setattr__(self, key: str, value: T) -> None:
        """
        Permit assigning dict keys as attributes.
        """
        self._set_node(key, value)

    def __setitem__(self, key: str, value: T) -> None:
        """Dictionary style access set data"""
        self._set_node(key, value, check=False, wrap=False)

    def _get_node(self, key: str, default: Callable[[], T]) -> T:
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

    def _recursive_items(self) -> Generator[tuple[str, T], None, None]:
        from ._l_node import LNode

        def recurse(tree, path=None):
            path = path or []  # Avoid mutable default arguments
            if isinstance(tree, DNode | dict | AsdfDictNode):
                for key, val in tree.items():
                    yield from recurse(val, [*path, key])
            elif isinstance(tree, LNode | list | tuple | AsdfListNode):
                for i, val in enumerate(tree):
                    yield from recurse(val, [*path, i])
            elif tree is not None:
                yield (".".join(str(x) for x in path), tree)

        yield from recurse(self)

    def to_flat_dict(self, include_arrays: bool = True, recursive: bool = False) -> dict[str, T]:
        """
        Returns a dictionary of all of the schema items as a flat dictionary.

        Each dictionary key is a dot-separated name.  For example, the
        schema element ``meta.observation.date`` will end up in the
        dictionary as::

            { "meta.observation.date": "2012-04-22T03:22:05.432" }

        """

        def convert_val(val):
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

    # def items(self) -> Generator[tuple[str, T], None, None]:
    #     yield from self._recursive_items()

    def __len__(self) -> int:
        """Define length of the node"""
        return len(self._data)

    def __delitem__(self, key: str) -> None:
        """Dictionary style access delete data"""
        del self._data[self._to_schema_key(key)]

    def __iter__(self) -> iter[dict[str, T]]:
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

    def copy(self) -> DNode:
        """Handle copying of the node"""
        instance = self.__class__.__new__(self.__class__)
        instance.__dict__.update(self.__dict__.copy())
        instance.__dict__["_data"] = self.__dict__["_data"].copy()

        return instance

    def unwrap(self) -> dict:
        return dict(self)

    def to_asdf_tree(self, ctx: AsdfFile, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> dict:
        from ..rad import TagMixin

        tree = self.unwrap()

        for key, value in tree.items():
            # Wrap the value into node so that it can be written to ASDF correctly
            value = self._wrap_into_node(key, value)
            tree[key] = value

            # Leave tagged objects alone, ASDF will take care of them
            if isinstance(value, TagMixin):
                continue

            # Recursively convert not-tagged nodes
            if isinstance(value, AsdfNodeMixin):
                tree[key] = value.to_asdf_tree(ctx, flush=flush, warn=warn)

            # Don't need to touch anything else

        return tree

    def __asdf_traverse__(self) -> dict[str, T]:
        """Asdf traverse method for things like info/search"""
        return self.unwrap()

    def __eq__(self, other: Any) -> bool:
        """Equality check"""
        if not isinstance(other, DNode):
            return False

        return self._data == other._data


class PatternDNode(DNode, ABC):
    """
    Support for pattern nodes.
    """

    @classmethod
    @abstractmethod
    def asdf_key_pattern(cls) -> str:
        """
        Get the key pattern for the node.
        """

    def _check_key(self, key):
        if re.match(self.asdf_key_pattern(), key):
            return True

        return super()._check_key(key)


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
        return self._get_node(function.__name__, lambda: function(self, *args, **kwargs))

    return field_property(wrapper)
