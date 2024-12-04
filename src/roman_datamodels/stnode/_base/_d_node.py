from __future__ import annotations

import datetime
from collections.abc import MutableMapping
from typing import Annotated, Generic, TypeVar

import numpy as np
from asdf.lazy_nodes import AsdfDictNode, AsdfListNode
from asdf.tags.core import ndarray
from astropy.time import Time

from ._utils import SchemaProperties, get_schema_for_property

__all__ = ["DNode"]

T = TypeVar("T")


# Once we are >3.11 -> DNode[T] can replace the Generic[T] in the class definition
class DNode(MutableMapping, Generic[T]):
    """
    Base class describing all "object" (dict-like) data nodes for STNode classes.
    """

    def __init__(self, node=None, parent=None, name=None):
        # Handle if we are passed different data types
        if node is None:
            self.__dict__["_data"] = {}
        elif isinstance(node, dict | AsdfDictNode):
            self.__dict__["_data"] = node
        else:
            raise ValueError("Initializer only accepts dicts")

        # Set the metadata tracked by the node
        self._x_schema = None
        self._schema_uri = None
        self._parent = parent
        self._name = name
        self._x_schema_attributes = None

    def __class_getitem__(cls, item_type: type) -> type[DNode[T]]:
        """Enable type hinting for the class"""

        return Annotated[cls, item_type]

    def _has_node(self, key):
        """
        Check if a node exists in the dictionary.
        """
        return key in self._data

    def __contains__(self, key):
        return self._has_node(key)

    def _coerce(self, key, value):
        from ._l_node import LNode

        # Return objects as node classes, if applicable
        if isinstance(value, dict | AsdfDictNode):
            return DNode(value, parent=self, name=key)

        if isinstance(value, list | AsdfListNode):
            return LNode(value)

        return value

    def _pull_node(self, key, coerce=True):
        """
        Get a node from the dictionary, coercing it to the correct type if necessary.
        """

        if self._has_node(key):
            value = self._data[key]
            if coerce:
                return self._coerce(key, value)
            return value

        raise AttributeError(f"No such attribute ({key}) found in node")

    def __getattr__(self, key):
        """
        Permit accessing dict keys as attributes, assuming they are legal Python
        variable names.
        """
        # Private values should have already been handled by the __getattribute__ method
        #   bail out if we are falling back on this method
        if key.startswith("_"):
            raise AttributeError(f"No attribute {key}")

        return self._pull_node(key, coerce=True)

    def _set_node(self, key, value, coerce=True):
        """
        Attempt to set a value in for the node
        """
        # Private keys should just be in the normal __dict__
        if key[0] != "_":
            self._data[key] = value

        else:
            self.__dict__[key] = value

    def __setattr__(self, key, value):
        """
        Permit assigning dict keys as attributes.
        """
        self._set_node(key, value)

    def _get_node(self, key, default, coerce=True):
        """
        Get a node and if not found construct it with the default value.

        Parameters
        ----------
        key : str
            The key to look for in the dictionary.
        default : Callable
            The constructor for a default. Its callable to allow for lazy instantiation.
            This will often take the form of a lambda, that way the argument to the lambda
            is not evaluated until the default is actually needed, saving time and memory.
            for things like numpy arrays.
        coerce : bool
            If type coercion should be applied to the value.
        """

        if not self._has_node(key):
            self._set_node(key, default(), coerce=coerce)

        return self._pull_node(key, coerce=coerce)

    @property
    def _schema_attributes(self):
        """
        Get the schema attributes for this node.
        """
        if self._x_schema_attributes is None:
            self._x_schema_attributes = SchemaProperties.from_schema(self._schema())
        return self._x_schema_attributes

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

    def to_flat_dict(self, include_arrays=True, recursive=False):
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

    def _schema(self):
        """
        If not overridden by a subclass, it will search for a schema from
        the parent class, recursing if necessary until one is found.
        """
        if self._x_schema is None:
            parent_schema = self._parent._schema()
            # Extract the subschema corresponding to this node.
            subschema = get_schema_for_property(parent_schema, self._name)
            self._x_schema = subschema
        return self._x_schema

    def __asdf_traverse__(self):
        """Asdf traverse method for things like info/search"""
        return dict(self)

    def __len__(self):
        """Define length of the node"""
        return len(self._data)

    def __getitem__(self, key):
        """Dictionary style access data"""
        if key in self._data:
            return self._data[key]

        raise KeyError(f"No such key ({key}) found in node")

    def __setitem__(self, key, value):
        """Dictionary style access set data"""

        # If the value is a dictionary, loop over its keys and convert them to tagged scalars
        if isinstance(value, dict | AsdfDictNode):
            for sub_key, sub_value in value.items():
                value[sub_key] = sub_value

        self._data[key] = value

    def __delitem__(self, key):
        """Dictionary style access delete data"""
        del self._data[key]

    def __iter__(self):
        """Define iteration"""
        return iter(self._data)

    def __repr__(self):
        """Define a representation"""
        return repr(self._data)

    def copy(self):
        """Handle copying of the node"""
        instance = self.__class__.__new__(self.__class__)
        instance.__dict__.update(self.__dict__.copy())
        instance.__dict__["_data"] = self.__dict__["_data"].copy()

        return instance
