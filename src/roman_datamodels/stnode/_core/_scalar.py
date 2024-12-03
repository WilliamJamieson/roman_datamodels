from abc import ABC

from ._mixins import SchemaMixin, TagMixin

__all__ = [
    "SchemaScalarNode",
    "TaggedScalarNode",
]


class SchemaScalarNode(SchemaMixin, ABC): ...


class TaggedScalarNode(SchemaScalarNode, TagMixin, ABC):
    """
    Base class for all tagged scalars defined by RAD
        There will be one of these for any tagged object defined by RAD, which has
        a scalar base type, or wraps a scalar base type.
        These will all be in the tagged_scalars directory.
    """

    def __asdf_traverse__(self):
        return self
