"""
This module contains the functions for deducing the type annotations for the
stnode classes based on their schemas
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum, auto

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
            name = "|".join(self.name)

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

    @classmethod
    def get_annotation(cls, tag: str) -> Annotation:
        """
        Deduce the type annotation from a "tag:" entry in a schema
        """

        match tag:
            case cls.ndarray:
                return Annotation("np.ndarray", "import numpy as np")
            case cls.unit:
                return Annotation("units.Unit", "from astropy import units")
            case cls.time:
                return Annotation("time.Time", "from astropy import time")
            case cls.quantity:
                return Annotation("units.Quantity", "from astropy import units")
            case cls.table:
                return Annotation("table.Table", "from astropy import table")
            case cls.wcs:
                return Annotation("wcs.WCS", "from gwcs import wcs")

        if tag in RAD_TAG_URIS:
            # This follows the same pattern as an ref uri
            return schema_ref(tag)

        raise ValueError(f"Unknown tag: {tag}")


def schema_ref(ref: str) -> Annotation:
    """
    Deduce the type annotation from a "$ref:" entry in a schema
    """

    return Annotation(class_name_from_uri(ref), f"from .{module_name_from_uri(ref)} import {class_name_from_uri(ref)}")


def schema_any_of(any_of: list[dict]) -> Annotation:
    """
    Deduce the type annotation from an "anyOf:" entry in a schema
    """
    annotation = None

    for schema in any_of:
        new_annotation = JsonSchemaProperty.get_annotation(schema)

        if annotation is None:
            annotation = new_annotation
        else:
            annotation.merge_with(new_annotation)

    return annotation


def schema_all_of(all_of: list[dict]) -> Annotation:
    """
    Deduce the type annotation from an "allOf:" entry in a schema
    """

    # This requires more thought
    #    It will generate a whole new class object
    return Annotation("Any", "from typing import Any")


class JsonSchemaProperty(StrEnum):
    """
    All the types of properties that can be in a json schema for RAD
    """

    type = auto()
    tag = auto()
    ref = f"${auto()}"
    anyOf = auto()
    allOf = auto()

    @classmethod
    def get_annotation(cls, schema: dict) -> Annotation:
        """
        Deduce the type annotation from a property in a schema
        """

        if cls.type in schema:
            return JsonSchemaType.get_annotation(schema[cls.type])

        if cls.tag in schema:
            return AsdfTags.get_annotation(schema[cls.tag])

        if cls.ref in schema:
            return schema_ref(schema[cls.ref])

        if cls.anyOf in schema:
            return schema_any_of(schema[cls.anyOf])

        if cls.allOf in schema:
            return schema_all_of(schema[cls.allOf])

        # Fall back on Any
        return Annotation("Any", "from typing import Any")


def schema_properties(schema: dict) -> dict[Annotation]:
    """
    Deduce the type annotations for the properties of a schema
    """

    annotations = {}

    if "properties" in schema:
        for property_name, property_schema in schema["properties"].items():
            annotations[property_name] = JsonSchemaProperty.get_annotation(property_schema)

    return annotations
