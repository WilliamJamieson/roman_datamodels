from abc import ABC

from .._base import LNode
from ._mixins import SchemaMixin, TagMixin

__all__ = [
    "ListNode",
    "SchemaListNode",
    "TaggedListNode",
]


class ListNode(LNode, ABC): ...


class SchemaListNode(ListNode, SchemaMixin, ABC): ...


class TaggedListNode(SchemaListNode, TagMixin, ABC): ...
