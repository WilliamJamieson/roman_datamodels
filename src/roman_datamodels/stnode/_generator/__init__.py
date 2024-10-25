from os import PathLike

from . import _node, _schemas


def generate(path: PathLike) -> None:
    print(f"Generating {len(_schemas.RAD_TAGS)} STNode classes at {path}")

    register = _node.NodeRegister()
    for tag in _schemas.RAD_TAGS:
        register = _node.create_node("", register, tag)

    register.write(path)
