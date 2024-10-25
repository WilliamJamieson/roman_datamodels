"""
This module contains the functions for deducing the type annotations for the
stnode classes based on their schemas
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum, auto
from os import PathLike

from ._schemas import RAD_TAG_URIS, class_name_from_uri, module_name_from_uri

__all__ = ["schema_properties"]


@dataclass
class Annotation:
    """
    A class to hold the type annotation for a property
    """

    name: str | set[str]
    import_string: str | set[str]

    def merge_with(self, other: Annotation) -> None:
        """
        Merge the annotations from another Annotation object
        """

        if isinstance(self.name, str):
            self.name = {self.name}

        if isinstance(self.import_string, str):
            self.import_string = {self.import_string}

        if isinstance(other.name, str):
            self.name.add(other.name)
        else:
            self.name.update(other.name)

        if isinstance(other.import_string, str):
            self.import_string.add(other.import_string)
        else:
            self.import_string.update(other.import_string)

    @property
    def final(self) -> Annotation:
        """
        Return the final annotation string
        """

        if isinstance(self.name, str):
            name = self.name
        else:
            name = " | ".join(self.name)

        if isinstance(self.import_string, str):
            import_string = self.import_string
        else:
            import_string = "\n".join(self.import_string)

        return Annotation(name, import_string)


class JsonSchemaType(StrEnum):
    string = auto()
    number = auto()
    integer = auto()
    boolean = auto()
    array = auto()
    object = auto()
    null = auto()

    @classmethod
    def get_annotation(cls, type_: str) -> Annotation:
        """
        Deduce the type annotation from a "type:" entry in a schema

        These should be all the basic types that can be indicated in a json schema
        """

        match type_:
            case cls.string:
                return Annotation("str", "")
            case cls.number:
                return Annotation("float", "")
            case cls.integer:
                return Annotation("int", "")
            case cls.boolean:
                return Annotation("bool", "")
            case cls.array:
                return Annotation("list", "")
            case cls.object:
                return Annotation("dict", "")
            case cls.null:
                return Annotation("None", "")
            case _:
                return Annotation("Any", "from typing import Any")


class AsdfTags(StrEnum):
    ndarray = "tag:stsci.edu:asdf/core/ndarray-1.*"
    unit = "tag:astropy.org:astropy/units/unit-1.*"
    time = "tag:stsci.edu:asdf/time/time-1.*"
    quantity = "tag:stsci.edu:asdf/unit/quantity-1.*"
    table = "tag:astropy.org:astropy/table/table-1.*"
    wcs = "tag:stsci.edu:gwcs/wcs-*"
    fps_time = "http://stsci.edu/schemas/asdf/time/time-1.1.0"

    @classmethod
    def get_annotation(cls, path: PathLike, tag: str) -> Annotation:
        """
        Deduce the type annotation from a "tag:" entry in a schema
        """

        match tag:
            case cls.ndarray:
                return Annotation("np.ndarray", "import numpy as np")
            case cls.unit:
                return Annotation("units.Unit", "from astropy import units")
            case cls.time | cls.fps_time:
                return Annotation("time.Time", "from astropy import time")
            case cls.quantity:
                return Annotation("units.Quantity", "from astropy import units")
            case cls.table:
                return Annotation("table.Table", "from astropy import table")
            case cls.wcs:
                return Annotation("wcs.WCS", "from gwcs import wcs")

        if tag in RAD_TAG_URIS:
            # This follows the same pattern as an ref uri
            return schema_ref(path, tag)

        raise ValueError(f"Unknown tag: {tag}")


def schema_ref(path: PathLike, ref: str) -> Annotation:
    """
    Deduce the type annotation from a "$ref:" entry in a schema
    """
    from ._node import create_ref_object_node

    if ref not in RAD_TAG_URIS and create_ref_object_node(path, ref).write(path):
        print(f"Creating ref object node for {ref}")

    return Annotation(class_name_from_uri(ref), f"from .{module_name_from_uri(ref)} import {class_name_from_uri(ref)}")


def schema_any_of(path: PathLike, name: str, any_of: list[dict]) -> Annotation:
    """
    Deduce the type annotation from an "anyOf:" entry in a schema
    """
    annotation = None

    for schema in any_of:
        new_annotation = JsonSchemaProperty.get_annotation(path, name, schema)

        if annotation is None:
            annotation = new_annotation
        else:
            annotation.merge_with(new_annotation)

    return annotation


def schema_all_of(path: PathLike, name: str, all_of: list[dict]) -> Annotation:
    """
    Deduce the type annotation from an "allOf:" entry in a schema
    """

    for schema in all_of:
        if JsonSchemaProperty.ref in schema and (ref := schema[JsonSchemaProperty.ref]) not in AsdfTags:
            schema_ref(path, ref)

    # This requires more thought
    #    It will generate a whole new class object
    return Annotation("Any", "from typing import Any")


class JsonSchemaProperty(StrEnum):
    """
    All the types of properties that can be in a json schema for RAD
    """

    type = "type"
    tag = "tag"
    ref = "$ref"
    anyOf = "anyOf"
    allOf = "allOf"

    @classmethod
    def get_annotation(cls, path: PathLike, name: str, schema: dict) -> Annotation:
        """
        Deduce the type annotation from a property in a schema
        """
        if cls.type in schema:
            return JsonSchemaType.get_annotation(schema[cls.type])

        if cls.tag in schema:
            return AsdfTags.get_annotation(path, schema[cls.tag])

        if cls.ref in schema:
            return schema_ref(path, schema[cls.ref])

        if cls.anyOf in schema:
            return schema_any_of(path, name, schema[cls.anyOf])

        if cls.allOf in schema:
            return schema_all_of(path, name, schema[cls.allOf])

        # Fall back on Any
        return Annotation("Any", "from typing import Any")


def schema_annotation(path: PathLike, name: str, schema: dict) -> Annotation:
    """
    Deduce the type annotation for a schema
    """

    return JsonSchemaProperty.get_annotation(path, name, schema)


def schema_properties(path: PathLike, name: str, schema: dict) -> dict[Annotation]:
    """
    Deduce the type annotations for the properties of a schema
    """

    annotations = {}

    if "properties" in schema:
        for property_name, property_schema in schema["properties"].items():
            annotations[property_name] = schema_annotation(path, name, property_schema)

    return annotations
