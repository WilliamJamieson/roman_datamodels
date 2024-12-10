from abc import ABC, abstractmethod
from typing import Any

from asdf import AsdfFile
from astropy.time import Time

from ..core import FlushOptions
from ._schema import SchemaListNode, SchemaMixin, SchemaObjectNode, SchemaScalarNode

__all__ = [
    "TagMixin",
    "TaggedListNode",
    "TaggedObjectNode",
    "TaggedScalarNode",
]


class TagMixin(SchemaMixin, ABC):
    """Mixin for nodes to support linking to a tag."""

    @classmethod
    @abstractmethod
    def asdf_tag(cls) -> str:
        """Tag of the node."""


class TaggedObjectNode(SchemaObjectNode, TagMixin, ABC):
    """
    Base class for all objects that are tagged in RAD.
    """


class TaggedListNode(SchemaListNode, TagMixin, ABC):
    """
    Base class for all tagged list nodes defined by RAD
        There will be one of these for any tagged object defined by RAD, which has
        a list base type, or wraps a list base type.
        These will all be in the tagged_lists directory.
    """


class TaggedScalarNode(SchemaScalarNode, TagMixin, ABC):
    """
    Base class for all tagged scalars defined by RAD
        There will be one of these for any tagged object defined by RAD, which has
        a scalar base type, or wraps a scalar base type.
        These will all be in the tagged_scalars directory.
    """

    def to_asdf_tree(self, ctx: AsdfFile, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> Any:
        tree = super().to_asdf_tree(ctx, flush, warn)

        # Special handling for Time objects
        # -> others maybe needed in the future
        if isinstance(tree, Time):
            converter = ctx.extension_manager.get_converter_for_type(Time)
            return converter.to_yaml_tree(tree, self.asdf_tag(), ctx)

        return tree
