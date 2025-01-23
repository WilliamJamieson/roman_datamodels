import warnings
from abc import ABC
from collections.abc import Callable, Generator
from enum import Enum
from functools import wraps
from typing import Any, TypeAlias, TypeVar, cast

from asdf import AsdfFile
from asdf.lazy_nodes import AsdfDictNode, AsdfListNode

from ..core import DNode, FlushOptions, LNode, get_config, type_checked
from ._base import RadNodeMixin
from ._utils import get_node_fields

__all__ = [
    "ListNode",
    "Node",
    "ObjectNode",
    "ScalarNode",
    "field",
]

_T = TypeVar("_T")


class ObjectNode(DNode[_T], RadNodeMixin[_T], ABC):
    @classmethod
    def asdf_required(cls) -> set[str]:
        """List of required fields in this node."""
        return cls.asdf_schema().required

    @classmethod
    def asdf_property_order(cls) -> tuple[str, ...]:
        """Order of properties in the schema."""
        return cls.asdf_schema().property_order

    @classmethod
    def fill_docs(cls) -> None:
        super().fill_docs()

        # Add field docstrings
        for name, schema in cls.asdf_schema().fields.items():
            getattr(cls, name).__doc__ = schema.docstring

    def _field_generator(self, flush: FlushOptions = FlushOptions.NONE) -> Generator[str, None, None]:
        """
        Generator which yields the fields of this object.
            yields the field values in the following order:
                1. Fields in the order defined in the schema via the `propertyOrder` keyword.
                2. Required fields not already yielded in alphabetical order.
                3. Non-required fields not already yielded in alphabetical order.
                4. Extra fields not already yielded in alphabetical order.
                5. All other non-yielded data in _data in alphabetical order
        """
        required_fields = self.asdf_required()

        data_fields = set(self._data.keys())
        visited_fields = set()

        def handle_missing_field(field: str) -> Generator[str, None, None]:
            """
            Determine if we need to yield a missing field
            """
            match flush:
                case FlushOptions.REQUIRED:
                    if field in required_fields:
                        yield field
                case FlushOptions.ALL:
                    if field in self.schema_fields:
                        yield field
                case FlushOptions.EXTRA:
                    if field in self.fields:
                        yield field
                case _:
                    if flush is not FlushOptions.NONE:
                        raise ValueError(f"Invalid flush option: {flush}")

        def handle_field(field: str) -> Generator[str, None, None]:
            """
            Handle yielding the actual field
            """
            if field not in visited_fields:
                visited_fields.add(field)
                if field in data_fields:
                    data_fields.remove(field)

                    yield field
                else:
                    yield from handle_missing_field(field)
            else:
                raise ValueError(f"Field {field} has already been visited!")

        # 1) Return fields in the order defined by `propertyOrder`
        for field in self.asdf_property_order():
            yield from handle_field(field)

        # 2) Return required fields not already yielded in alphabetical order
        for field in sorted(required_fields - visited_fields):
            yield from handle_field(field)

        # 3) Return non-required fields not already yielded in alphabetical order
        for field in sorted(set(self.schema_fields) - visited_fields):
            yield from handle_field(field)

        # 4) Return extra fields not already yielded in alphabetical order
        for field in sorted(set(self.fields) - visited_fields):
            yield from handle_field(field)

        # 5) Return all other non-yielded data in _data in alphabetical order
        for field in sorted(data_fields):
            yield field

    def node_items(self, *, flush: FlushOptions = FlushOptions.NONE, warn: bool = False) -> Generator[tuple[str, _T], None, None]:
        """
        Generator which yields the fields and values of this object.
            yields the field values in the following order:
                1. Fields in the order defined in the schema via the `propertyOrder` keyword.
                2. Required fields not already yielded in alphabetical order.
                3. Non-required fields not already yielded in alphabetical order.
                4. Extra fields not already yielded in alphabetical order.
                5. All other non-yielded data in _data in alphabetical order
        """
        for field in self._field_generator(flush):
            if not self._has_node(field) and warn:
                warnings.warn(f"Filling in missing required field '{field}' with default value.", UserWarning, stacklevel=2)

            yield field, getattr(self, field)

    def flat_items(self, *, flush: FlushOptions = FlushOptions.NONE, warn: bool = False) -> Generator[tuple[str, _T], None, None]:
        """
        Generator which yields the fields and values of this object, flattened to be keys `foo.bar.baz`.
            yields the flattened field values, where it will yield until exhausting all the subfields
            following the same ordering

            field values in the following order at the same level:
                1. Fields in the order defined in the schema via the `propertyOrder` keyword.
                2. Required fields not already yielded in alphabetical order.
                3. Non-required fields not already yielded in alphabetical order.
                4. Extra fields not already yielded in alphabetical order.
                5. All other non-yielded data in _data in alphabetical order
        """

        def recurse(tree: Any, path: list[str | int] | None = None) -> Generator[tuple[str, _T], None, None]:
            """
            Recurse through the tree to flatten it
            """
            path = path or []

            if isinstance(tree, ObjectNode):
                for field, value in tree.node_items(flush=flush, warn=warn):
                    yield from recurse(value, [*path, field])
            elif isinstance(tree, DNode | dict | AsdfDictNode):
                for field, value in sorted(tree.items()):
                    yield from recurse(value, [*path, field])
            elif isinstance(tree, LNode | list | AsdfListNode):
                for idx, value in enumerate(tree):
                    yield from recurse(value, [*path, idx])
            else:
                yield ".".join(map(str, path)), tree.value if isinstance(tree, Enum) else tree

        yield from recurse(self)

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
        ## This makes use of the generator method developed for table writing above
        #  however, this causes slow downs in general use cases.
        # for _, field_value in self.node_items(flush=flush, warn=warn):
        #     if recurse and isinstance(field_value, ObjectNode):
        #         field_value.flush(flush=flush, warn=warn, recurse=recurse)

        match flush:
            case FlushOptions.NONE:
                return
            case FlushOptions.REQUIRED:
                fields = tuple(self.asdf_required())
            case FlushOptions.ALL:
                fields = get_node_fields(type(self))
            case FlushOptions.EXTRA:
                fields = get_node_fields(type(self)) + self._extra_fields()
            case _:
                raise ValueError(f"Invalid flush option: {flush}")

        for field in fields:
            if not self._has_node(field) and warn:
                warnings.warn(f"Filling in missing required field '{field}' with default value.", UserWarning, stacklevel=2)

            # access the field to trigger its default value
            field_value = getattr(self, field)
            if recurse and isinstance(field_value, ObjectNode):
                field_value.flush(flush=flush, warn=warn, recurse=recurse)

    def to_asdf_tree(self, ctx: AsdfFile, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> dict[str, Any]:
        # Flush out any required fields
        self.flush(flush, warn)
        return super().to_asdf_tree(ctx, flush=flush, warn=warn)

    def __asdf_traverse__(self) -> dict[str, _T]:
        return self.to_asdf_tree(ctx=get_config().asdf_ctx, flush=FlushOptions.REQUIRED, warn=False)


class ListNode(LNode[_T], RadNodeMixin[_T], ABC):
    """
    Base class for all list nodes
    """


class ScalarNode(RadNodeMixin[_T], ABC):
    """
    Base class for all scalars with descriptions in RAD
    -> this is for enums that are not tagged
    """

    def unwrap(self) -> Any:
        base = self.value if isinstance(self, Enum) else self

        return type(base).__bases__[0](base)

    def to_asdf_tree(self, ctx: AsdfFile, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> Any:
        return self.unwrap()

    def __asdf_traverse__(self) -> Any:
        return self.to_asdf_tree(ctx=get_config().asdf_ctx, flush=FlushOptions.REQUIRED, warn=False)


def field(function: Callable[[DNode[Any]], _T]) -> Callable[[ObjectNode[Any]], _T]:
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
    def wrapper(self: DNode[Any]) -> _T:
        """
        Wrap the function (which is defined on the node) to handle getting the value
        from the node and then falling back on evaluating the function itself to
        get, set, and then return the default value.
        """

        # Note the lambda is used to delay the evaluation of the default value all the way
        # until the default is actually needed. This is important for things like numpy arrays
        # which can be expensive to create (memory and time wise).
        #
        return cast(_T, self._get_node(function.__name__, lambda: type_checked(function)(self)))

    return wrapper


Node: TypeAlias = DNode[Any]
