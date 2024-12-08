from abc import ABC

from ..core import LNode
from ._mixins import SchemaMixin, TagMixin

__all__ = [
    "ListNode",
    "SchemaListNode",
    "TaggedListNode",
]


class ListNode(LNode, ABC):
    """
    Base class for all list nodes
    """


class SchemaListNode(ListNode, SchemaMixin, ABC):
    """
    Base class for all list nodes described by their own schema in RAD.
    """


class TaggedListNode(SchemaListNode, TagMixin, ABC):
    """
    Base class for all tagged list nodes defined by RAD
        There will be one of these for any tagged object defined by RAD, which has
        a list base type, or wraps a list base type.
        These will all be in the tagged_lists directory.
    """
