from __future__ import annotations

from collections import UserList
from typing import Annotated, Generic, TypeVar

from asdf.lazy_nodes import AsdfListNode

from ._mixins import AsdfNodeMixin, FlushOptions

__all__ = ["LNode"]

T = TypeVar("T")


# Once we are >3.11 -> LNode[T] can replace the Generic[T] in the class definition
class LNode(AsdfNodeMixin, UserList, Generic[T]):
    """
    Base class describing all "array" (list-like) data nodes for STNode classes.
    """

    def __init__(self, node=None) -> None:
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

    def unwrap(self) -> list:
        return list(self)

    def to_asdf_tree(self, flush: FlushOptions = FlushOptions.REQUIRED, warn: bool = False) -> list:
        from ..rad import TagMixin

        tree = self.unwrap()
        for i, item in enumerate(tree):
            # Leave tagged objects alone, ASDF will take care of them
            if isinstance(item, TagMixin):
                continue

            # Recursively convert not-tagged nodes
            if isinstance(item, AsdfNodeMixin):
                tree[i] = item.to_asdf_tree(flush=flush, warn=warn)

            # Don't need to touch anything else

        return tree

    def __asdf_traverse__(self) -> list[T]:
        return self.unwrap()
