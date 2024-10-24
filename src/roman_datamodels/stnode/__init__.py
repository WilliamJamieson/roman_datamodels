"""
The STNode classes and supporting objects generated dynamically at import time
    from RAD's manifest.
"""

from . import _stnode
from ._converters import NODE_EXTENSIONS
from ._node import DNode, LNode
from ._stnode import NODE_CLASSES
from ._tagged import TaggedListNode, TaggedObjectNode, TaggedScalarNode

__all__ = [
    "DNode",
    "LNode",
    "TaggedListNode",
    "TaggedObjectNode",
    "TaggedScalarNode",
    "NODE_CLASSES",
    "NODE_EXTENSIONS",
]

for name in _stnode.__all__:
    __all__.append(name)
    globals()[name] = getattr(_stnode, name)
