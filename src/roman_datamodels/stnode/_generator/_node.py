"""
Module to generate the STNode class.
"""

import textwrap
from dataclasses import dataclass
from os import PathLike
from pathlib import Path

from ._annotation import schema_annotation, schema_properties
from ._property import create_property
from ._schemas import class_name_from_uri, docstring_from_tag, load_schema_from_uri, module_name_from_uri

_TAGGED_CLASS_TEMPLATE = """
class {name}({base}):
{docstring}

    _tag = "{tag_uri}"

"""

_SCHEMA_CLASS_TEMPLATE = """
class {name}({base}):

"""


@dataclass
class TaggedNode:
    """
    A class to hold the information for a tagged node
    """

    module: str
    node: str
    import_string: set[str] | None = None

    @property
    def header(self) -> str:
        header = "from roman_datamodels.stnode import _mixins, _tagged\n\n"

        if self.import_string is None:
            return header

        return f'{header}{"\n".join(self.import_string)}'

    @property
    def code(self) -> str:
        return "\n".join([self.header, self.node])

    def write(self, path: PathLike) -> bool:
        save_path = Path(path) / f"{self.module}.py"

        save_path.parent.mkdir(parents=True, exist_ok=True)

        if not save_path.exists():
            with save_path.open("w") as f:
                f.write(self.code)

            return True
        return False


def create_tagged_object_node(path: PathLike, tag: dict[str, str], schema: dict[str, str] | None = None) -> TaggedNode:
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

    name = class_name_from_uri(tag_uri)
    base = f"_mixins.{name}Mixin, _tagged.TaggedObjectNode"
    docstring = textwrap.indent(f'"""\n{docstring_from_tag(tag)}\n"""', " " * 4)

    class_ = _TAGGED_CLASS_TEMPLATE.format(name=name, base=base, docstring=docstring, tag_uri=tag_uri)

    import_string = set()
    for property_name, annotation in schema_properties(path, name, schema).items():
        final_annotation = annotation.final
        class_ += textwrap.indent(create_property(property_name, final_annotation.name), " " * 4)
        if isinstance(annotation.import_string, str):
            import_string.add(annotation.import_string)
        else:
            import_string.update(annotation.import_string)

    return TaggedNode(module_name_from_uri(tag_uri), class_, import_string)


def create_tagged_list_node(tag: dict[str, str]) -> TaggedNode:
    tag_uri = tag["tag_uri"]

    name = class_name_from_uri(tag_uri)
    base = f"_mixins.{name}Mixin, _tagged.TaggedListNode"
    docstring = textwrap.indent(f'"""\n{docstring_from_tag(tag)}\n"""', " " * 4)

    return TaggedNode(
        module_name_from_uri(tag_uri),
        _TAGGED_CLASS_TEMPLATE.format(name=name, base=base, docstring=docstring, tag_uri=tag_uri),
    )


def create_tagged_scalar_node(path: PathLike, tag: dict[str, str], schema: dict[str, str]) -> TaggedNode:
    tag_uri = tag["tag_uri"]

    name = class_name_from_uri(tag_uri)
    annotation = schema_annotation(path, name, schema).final

    base = f"{annotation.name}, _tagged.TaggedScalarNode"
    docstring = textwrap.indent(f'"""\n{docstring_from_tag(tag)}\n"""', " " * 4)

    return TaggedNode(
        module_name_from_uri(tag_uri),
        _TAGGED_CLASS_TEMPLATE.format(name=name, base=base, docstring=docstring, tag_uri=tag_uri),
        {annotation.import_string},
    )


def create_node(path: PathLike, tag: dict[str, str]) -> TaggedNode:
    schema = load_schema_from_uri(tag["schema_uri"])

    if "tagged_scalar" in tag["schema_uri"]:
        return create_tagged_scalar_node(path, tag, schema)

    if "type" in schema:
        if schema["type"] == "object":
            return create_tagged_object_node(path, tag, schema)
        elif schema["type"] == "array":
            return create_tagged_list_node(tag)
        else:
            raise RuntimeError(f"Unknown schema type: {schema['type']}")
    elif "allOf" in schema:
        return create_tagged_object_node(path, tag, schema)

    raise RuntimeError(f"Unknown schema type for: {tag['schema_uri']}")


def create_ref_object_node(path: PathLike, schema_uri: str) -> TaggedNode:
    schema = load_schema_from_uri(schema_uri)

    name = class_name_from_uri(schema_uri)

    annotation = schema_annotation(path, name, schema).final
    base = "_core.DNode" if annotation.name == "Any" else annotation.name

    class_ = _SCHEMA_CLASS_TEMPLATE.format(name=name, base=base)

    import_string = {"from roman_datamodels.stnode import _core\n"}
    for property_name, annotation in schema_properties(path, name, schema).items():
        final_annotation = annotation.final
        class_ += textwrap.indent(create_property(property_name, final_annotation.name), " " * 4)
        if isinstance(annotation.import_string, str):
            import_string.add(annotation.import_string)
        else:
            import_string.update(annotation.import_string)

    return TaggedNode(module_name_from_uri(schema_uri), class_, import_string)
