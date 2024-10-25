"""
Module to generate the STNode class.
"""

from __future__ import annotations

import subprocess
import textwrap
from dataclasses import dataclass
from os import PathLike
from pathlib import Path

from ._annotation import Annotation, AnnotationInput, schema_annotation, schema_object
from ._property import create_property
from ._schemas import docstring_from_tag, load_schema_from_uri

_TAGGED_CLASS_TEMPLATE = """
class {name}({base}):
{docstring}

    _tag = "{tag_uri}"

"""

_CLASS_TEMPLATE = """
class {name}({base}):

"""

_HEADER_TEMPLATE = """
from roman_datamodels.stnode import _mixins, _tagged

{import_string}
"""

_MODULE_TEMPLATE = """\"\"\"
This module as been automatically generated, do not edit by hand.
\"\"\"

{code}
"""


class NodeRegister:
    def __init__(self):
        self._nodes: dict[str, Node] = {}

    def __contains__(self, node: Node) -> bool:
        return node.key in self._nodes

    def register(self, node: Node) -> bool:
        if node in self:
            return False

        self._nodes[node.key] = node
        return True

    def write(self, path: PathLike) -> None:
        print(f"Writing {len(self._nodes)} nodes to {path}")
        for key, node in self._nodes.items():
            print(f"   Writing node: {key}")

            node.write(path)


@dataclass
class Node:
    """
    Class to hold the information to generate code for an STNode class
    """

    path: PathLike
    class_name: str
    module_name: str

    body: str

    import_string: set[str] | None = None

    @property
    def key(self) -> str:
        return f"{self.module_name}.{self.class_name}"

    @property
    def header(self) -> str:
        import_string = ""
        if self.import_string is not None:
            import_string = "\n".join(self.import_string)

        return _HEADER_TEMPLATE.format(import_string=import_string)

    @property
    def code(self) -> str:
        return "\n".join([self.header, self.body])

    @property
    def module(self) -> str:
        return _MODULE_TEMPLATE.format(code=self.code)

    def write(self, path: PathLike) -> None:
        save_path = Path(path) / Path(self.path) / f"{self.module_name}.py"
        save_path.parent.mkdir(parents=True, exist_ok=True)

        if not save_path.exists():
            with save_path.open("w") as f:
                f.write(self.module)

            for _ in range(4):
                out = subprocess.run(["pre-commit", "run", "--files", str(save_path)])

                if out.returncode == 0:
                    break
            else:
                raise RuntimeError(f"Failed to format {save_path}\n\n{out.stdout}\n\n{out.stderr}")

    @classmethod
    def from_input_data(
        cls,
        data: AnnotationInput,
        body: str,
        import_string: set[str] | None = None,
    ) -> Node:
        return cls(
            data.path,
            data.class_name,
            data.module_name,
            body,
            import_string,
        )


def create_tagged_object_node(
    path: PathLike,
    register: NodeRegister,
    tag: dict[str, str],
    schema: dict[str, str] | None = None,
) -> NodeRegister:
    """
    Generate the STNode class from the schema

    Parameters
    ----------
    schema : dict
        The schema loaded from the

    Returns
    -------
    string representation of the class
    """
    if schema is None:
        schema = load_schema_from_uri(tag["schema_uri"])

    tag_uri = tag["tag_uri"]

    data = AnnotationInput.from_uri(path, tag_uri)
    docstring = textwrap.indent(docstring_from_tag(tag), " " * 4)

    body = _TAGGED_CLASS_TEMPLATE.format(
        name=data.class_name,
        base=data.tagged_object_base,
        docstring=docstring,
        tag_uri=tag_uri,
    )

    import_string = set()
    for property_name, annotation in schema_object(
        register,
        data,
        schema,
    ).items():
        final_annotation = annotation.final
        body += textwrap.indent(
            create_property(property_name, final_annotation.name),
            " " * 4,
        )
        if isinstance(annotation.import_string, str):
            import_string.add(annotation.import_string)
        else:
            import_string.update(annotation.import_string)

    if not register.register(Node.from_input_data(data, body, import_string)):
        raise RuntimeError(f"Node for tag: {tag_uri} already exists")

    return register


def create_tagged_list_node(
    path: PathLike,
    register: NodeRegister,
    tag: dict[str, str],
) -> NodeRegister:
    tag_uri = tag["tag_uri"]

    data = AnnotationInput.from_uri(path, tag_uri)
    docstring = textwrap.indent(docstring_from_tag(tag), " " * 4)

    body = _TAGGED_CLASS_TEMPLATE.format(
        name=data.class_name,
        base=data.tagged_list_base,
        docstring=docstring,
        tag_uri=tag_uri,
    )

    if not register.register(Node.from_input_data(data, body)):
        raise RuntimeError(f"Node for tag: {tag_uri} already exists")

    return register


def create_tagged_scalar_node(
    path: PathLike,
    register: NodeRegister,
    tag: dict[str, str],
    schema: dict[str, str],
) -> NodeRegister:
    tag_uri = tag["tag_uri"]

    data = AnnotationInput.from_uri(path, tag_uri)
    annotation = schema_annotation(register, data, schema).final
    docstring = textwrap.indent(docstring_from_tag(tag), " " * 4)

    body = _TAGGED_CLASS_TEMPLATE.format(
        name=data.class_name,
        base=data.tagged_scalar_base(annotation.name),
        docstring=docstring,
        tag_uri=tag_uri,
    )

    if not register.register(
        Node.from_input_data(
            data,
            body,
            {annotation.import_string},
        )
    ):
        raise RuntimeError(f"Node for tag: {tag_uri} already exists")

    return register


def create_node(
    path: PathLike,
    register: NodeRegister,
    tag: dict[str, str],
) -> NodeRegister:
    print("Creating node: ", tag["tag_uri"])

    schema = load_schema_from_uri(tag["schema_uri"])

    if "tagged_scalar" in tag["schema_uri"]:
        return create_tagged_scalar_node(path, register, tag, schema)

    if "type" in schema:
        if schema["type"] == "object":
            return create_tagged_object_node(path, register, tag, schema)
        elif schema["type"] == "array":
            return create_tagged_list_node(path, register, tag)
        else:
            raise RuntimeError(f"Unknown schema type: {schema['type']}")
    elif "allOf" in schema:
        return create_tagged_object_node(path, register, tag, schema)

    raise RuntimeError(f"Unknown schema type for: {tag['schema_uri']}")


def create_ref_object_node(
    register: NodeRegister,
    data: AnnotationInput,
    schema_uri: str,
) -> NodeRegister:
    schema = load_schema_from_uri(schema_uri)

    node_data = AnnotationInput.from_uri(data.path, schema_uri)
    annotation = schema_annotation(
        register,
        node_data.property_input(data.property_name),
        schema,
    ).final
    annotation = node_data.ref_node_base(annotation).final

    body = _CLASS_TEMPLATE.format(
        name=node_data.class_name,
        base=annotation.name,
    )

    empty = True

    import_string = {annotation.import_string}
    for property_name, annotation in schema_object(
        register,
        node_data,
        schema,
    ).items():
        empty = False
        final_annotation = annotation.final
        body += textwrap.indent(
            create_property(property_name, final_annotation.name),
            " " * 4,
        )
        if isinstance(annotation.import_string, str):
            import_string.add(annotation.import_string)
        else:
            import_string.update(annotation.import_string)

    if empty:
        body += textwrap.indent("pass\n", " " * 4)

    register.register(Node.from_input_data(node_data, body, import_string))
    return register


def create_implied_object_node(
    register: NodeRegister,
    data: AnnotationInput,
    all_of: list[dict],
    bases: list[Annotation],
) -> NodeRegister:
    print(f"    Creating implied object node: {data.module_name}.{data.class_name}")

    base = ", ".join(list({base.name for base in bases}))
    body = _CLASS_TEMPLATE.format(name=data.class_name, base=base)
    empty = True

    import_string = set()
    for annotation in bases:
        if isinstance(annotation.import_string, str):
            import_string.add(annotation.import_string)
        else:
            import_string.update(annotation.import_string)

    for schema in all_of:
        if "properties" in schema:
            for property_name, annotation in schema_object(
                register,
                data,
                schema,
            ).items():
                empty = False
                final_annotation = annotation.final
                body += textwrap.indent(
                    create_property(property_name, final_annotation.name),
                    " " * 4,
                )
                if isinstance(annotation.import_string, str):
                    import_string.add(annotation.import_string)
                else:
                    import_string.update(annotation.import_string)

    if empty:
        body += textwrap.indent("pass\n", " " * 4)

    register.register(Node.from_input_data(data, body, import_string))
    return register
