from os import PathLike

from . import _node, _schemas


def generate(path: PathLike) -> None:
    for node in _schemas.RAD_TAGS:
        _node.create_tagged_node(node).write(path)
