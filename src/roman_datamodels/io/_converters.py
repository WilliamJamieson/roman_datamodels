"""
The ASDF Converters to handle the serialization/deseialization of the STNode classes to ASDF.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from asdf.extension import Converter, ManifestExtension

from roman_datamodels.stnode.rad import RDM_NODE_REGISTRY

if TYPE_CHECKING:
    from roman_datamodels.stnode.rad import TagMixin

__all__ = ["NODE_EXTENSIONS"]


class _NodeConverter(Converter):
    """
    Converter for all node classes in the roman_datamodels package.
    """

    # Enable lazy-tree building for all converters.
    lazy = True

    @property
    def tags(self):
        return list(RDM_NODE_REGISTRY.tagged_registry.keys())

    @property
    def types(self):
        return list(RDM_NODE_REGISTRY.tagged_registry.values())

    def select_tag(self, obj: TagMixin, tags, ctx):
        return obj.asdf_tag()

    def to_yaml_tree(self, obj: TagMixin, tag, ctx):
        return obj.to_asdf_tree(ctx)

    def from_yaml_tree(self, node, tag, ctx):
        return RDM_NODE_REGISTRY.tagged_registry[tag](node)


# Create the ASDF extension for the STNode classes.
NODE_EXTENSIONS = [
    ManifestExtension.from_uri("asdf://stsci.edu/datamodels/roman/manifests/datamodels-1.0", converters=[_NodeConverter()]),
]
