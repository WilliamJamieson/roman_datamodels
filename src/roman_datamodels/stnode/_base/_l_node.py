from __future__ import annotations

from collections import UserList
from typing import Annotated, Generic, TypeVar

from asdf.lazy_nodes import AsdfListNode

__all__ = ["LNode"]

T = TypeVar("T")


# Once we are >3.11 -> LNode[T] can replace the Generic[T] in the class definition
class LNode(UserList, Generic[T]):
    """
    Base class describing all "array" (list-like) data nodes for STNode classes.
    """

    def __init__(self, node=None):
        if node is None:
            self.data = []
        elif isinstance(node, list | AsdfListNode):
            self.data = node
        elif isinstance(node, self.__class__):
            self.data = node.data
        else:
            raise ValueError("Initializer only accepts lists")

    def __class_getitem__(cls, item_type: type) -> type[LNode[T]]:
        """Enable type hinting for the class"""

        return Annotated[cls, item_type]

    def __getitem__(self, index):
        return self.data[index]

    def __asdf_traverse__(self):
        return list(self)
