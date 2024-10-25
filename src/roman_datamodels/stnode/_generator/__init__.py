from os import PathLike

from . import _node, _schemas


def generate(path: PathLike) -> None:
    print(f"Generating {len(_schemas.RAD_TAGS)} STNode classes at {path}")
    for node in _schemas.RAD_TAGS:
        _node.create_node(path, node).write(path)
