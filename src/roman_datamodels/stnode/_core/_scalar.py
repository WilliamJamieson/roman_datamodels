from abc import ABC
from typing import Any

from .._base import FlushOptions
from ._mixins import SchemaMixin, TagMixin

__all__ = [
    "SchemaScalarNode",
    "TaggedScalarNode",
]


class SchemaScalarNode(SchemaMixin, ABC):
    """
    Base class for all scalars that are described by their own schema in RAD.
    """

    def unwrap(self) -> Any:
        return type(self).__bases__[0](self)

    def to_asdf_tree(self, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> Any:
        if isinstance(self, TagMixin):
            return self

        return self.unwrap()

    def __asdf_traverse__(self):
        return self.unwrap()


class TaggedScalarNode(SchemaScalarNode, TagMixin, ABC):
    """
    Base class for all tagged scalars defined by RAD
        There will be one of these for any tagged object defined by RAD, which has
        a scalar base type, or wraps a scalar base type.
        These will all be in the tagged_scalars directory.
    """

    def __asdf_traverse__(self):
        return self
