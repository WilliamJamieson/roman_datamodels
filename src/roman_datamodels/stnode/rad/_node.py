import warnings
from abc import ABC
from collections.abc import Generator
from enum import Enum
from typing import Any, TypeVar

from asdf import AsdfFile
from asdf.lazy_nodes import AsdfDictNode, AsdfListNode

from ..core import DNode, FlushOptions, LNode, get_config
from ._base import RadNodeMixin

__all__ = [
    "ListNode",
    "ObjectNode",
    "ScalarNode",
]

_T = TypeVar("_T")


class ObjectNode(DNode[_T], RadNodeMixin[_T], ABC):
    @classmethod
    def asdf_required(cls) -> set[str]:
        """List of required fields in this node."""
        return cls.asdf_schema().required

    @property
    def schema_required(self) -> set[str]:
        """List of required fields in the schema."""
        return self.schema.required

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
        required_fields = self.schema_required
        all_fields = self.schema_fields
        extra_fields = self.fields

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
                    if field in all_fields:
                        yield field
                case FlushOptions.EXTRA:
                    if field in extra_fields:
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
                fields = tuple(self.schema_required)
            case FlushOptions.ALL:
                fields = self.schema_fields
            case FlushOptions.EXTRA:
                fields = self.fields
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
