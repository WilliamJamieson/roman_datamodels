from collections import UserList

from asdf.lazy_nodes import AsdfDictNode, AsdfListNode

__all__ = ["LNode"]


class LNode(UserList):
    """
    Base class describing all "array" (list-like) data nodes for STNode classes.
    """

    _tag = None

    def __init__(self, node=None):
        if node is None:
            self.data = []
        elif isinstance(node, list | AsdfListNode):
            self.data = node
        elif isinstance(node, self.__class__):
            self.data = node.data
        else:
            raise ValueError("Initializer only accepts lists")

    def __getitem__(self, index):
        from ._d_node import DNode

        value = self.data[index]
        if isinstance(value, dict | AsdfDictNode):
            return DNode(value)
        elif isinstance(value, list | AsdfListNode):
            return LNode(value)
        else:
            return value

    def __asdf_traverse__(self):
        return list(self)
