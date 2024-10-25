"""
Module to generate the STNode class.
"""

import textwrap
from dataclasses import dataclass
from os import PathLike
from pathlib import Path

from ._annotation import schema_properties
from ._property import create_property
from ._schemas import class_name_from_uri, docstring_from_tag, load_schema_from_uri, module_name_from_uri

_TAGGED_CLASS_TEMPLATE = """
class {name}({base}):
{docstring}

    _tag = "{tag_uri}"

"""


@dataclass
class TaggedNode:
    """
    A class to hold the information for a tagged node
    """

    module: str
    node: str
    import_string: set[str]

    @property
    def header(self) -> str:
        header = "from roman_datamodels.stnode import _mixins, _tagged\n\n"
        return f'{header}{"\n".join(self.import_string)}'

    @property
    def code(self) -> str:
        return "\n".join([self.header, self.node])

    def write(self, path: PathLike) -> None:
        save_path = Path(path) / f"{self.module}.py"

        save_path.parent.mkdir(parents=True, exist_ok=True)

        with save_path.open("w") as f:
            f.write(self.code)


def create_tagged_node(tag: dict[str, str]) -> TaggedNode:
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

    tag_uri = tag["tag_uri"]
    schema = load_schema_from_uri(tag["schema_uri"])

    name = class_name_from_uri(tag_uri)
    base = f"_mixins.{name}Mixin, _tagged.TaggedObjectNode"
    docstring = textwrap.indent(f'"""\n{docstring_from_tag(tag)}\n"""', " " * 4)

    class_ = _TAGGED_CLASS_TEMPLATE.format(name=name, base=base, docstring=docstring, tag_uri=tag_uri)

    import_string = set()
    for property_name, annotation in schema_properties(schema).items():
        final_annotation = annotation.final
        class_ += textwrap.indent(create_property(property_name, final_annotation.name), " " * 4)
        if isinstance(annotation.import_string, str):
            import_string.add(annotation.import_string)
        else:
            import_string.update(annotation.import_string)

    return TaggedNode(module_name_from_uri(tag_uri), class_, import_string)
