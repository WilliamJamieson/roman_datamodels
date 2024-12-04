from __future__ import annotations

import datetime
from collections.abc import Callable, MutableMapping
from typing import Annotated, Generic, TypeVar

import numpy as np
from asdf.lazy_nodes import AsdfDictNode, AsdfListNode
from asdf.tags.core import ndarray
from astropy.time import Time

__all__ = ["DNode"]

T = TypeVar("T")


# Once we are >3.11 -> DNode[T] can replace the Generic[T] in the class definition
class DNode(MutableMapping, Generic[T]):
    """
    Base class describing all "object" (dict-like) data nodes for STNode classes.
    """

    def __init__(self, node=None) -> None:
        # Handle if we are passed different data types
        if node is None:
            self.__dict__["_data"] = {}
        elif isinstance(node, dict | AsdfDictNode):
            self.__dict__["_data"] = node
        else:
            raise ValueError("Initializer only accepts dicts")

    def __class_getitem__(cls, item_type: type) -> type[DNode[T]]:
        """Enable type hinting for the class"""

        return Annotated[cls, item_type]

    def _has_node(self, key: str) -> bool:
        """
        Check if a node exists in the dictionary.
        """
        return key in self._data

    def __contains__(self, key: str) -> bool:
        return self._has_node(key)

    def _pull_node(self, key: str) -> T:
        """
        Get a node from the dictionary, coercing it to the correct type if necessary.
        """

        if self._has_node(key):
            return self._data[key]

        raise AttributeError(f"No such attribute ({key}) found in node")

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
        return self._pull_node(key)

    def _set_node(self, key: str, value: T) -> None:
        """
        Attempt to set a value in for the node
        """
        # Private keys should just be in the normal __dict__
        if key[0] == "_":
            self.__dict__[key] = value
        else:
            self._data[key] = value

    def __setattr__(self, key: str, value: T) -> None:
        """
        Permit assigning dict keys as attributes.
        """
        self._set_node(key, value)

    def __setitem__(self, key: str, value: T) -> None:
        """Dictionary style access set data"""
        self._set_node(key, value)

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

    def _recursive_items(self):
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

    def __asdf_traverse__(self) -> dict[str, T]:
        """Asdf traverse method for things like info/search"""
        return dict(self)

    def __len__(self) -> int:
        """Define length of the node"""
        return len(self._data)

    def __delitem__(self, key: str) -> None:
        """Dictionary style access delete data"""
        del self._data[key]

    def __iter__(self) -> iter[dict[str, T]]:
        """Define iteration"""
        return iter(self._data)

    def __repr__(self) -> str:
        """Define a representation"""
        return repr(self._data)

    def copy(self) -> DNode:
        """Handle copying of the node"""
        instance = self.__class__.__new__(self.__class__)
        instance.__dict__.update(self.__dict__.copy())
        instance.__dict__["_data"] = self.__dict__["_data"].copy()

        return instance
