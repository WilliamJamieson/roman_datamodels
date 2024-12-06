from abc import ABC
from enum import Enum
from typing import Any

from astropy.time import Time

from .._base import FlushOptions
from ._mixins import RadNodeMixin, SchemaMixin, TagMixin

__all__ = [
    "ScalarNode",
    "SchemaScalarNode",
    "TaggedScalarNode",
]


class ScalarNode(RadNodeMixin, ABC):
    """
    Base class for all scalars with descriptions in RAD
    -> this is for enums that are not tagged
    """

    def unwrap(self) -> Any:
        base = self.value if isinstance(self, Enum) else self

        return type(base).__bases__[0](base)

    def to_asdf_tree(self, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> Any:
        return self.unwrap()

    def __asdf_traverse__(self):
        return self.unwrap()


class SchemaScalarNode(ScalarNode, SchemaMixin, ABC):
    """
    Base class for all scalars that are described by their own schema in RAD.
    """


class TaggedScalarNode(SchemaScalarNode, TagMixin, ABC):
    """
    Base class for all tagged scalars defined by RAD
        There will be one of these for any tagged object defined by RAD, which has
        a scalar base type, or wraps a scalar base type.
        These will all be in the tagged_scalars directory.
    """

    def to_asdf_tree(self, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> Any:
        tree = super().to_asdf_tree(flush, warn)

        if isinstance(tree, Time):
            converter = self.asdf_ctx().extension_manager.get_converter_for_type(Time)
            return converter.to_yaml_tree(tree, self.tag, self.asdf_ctx())

        return tree
