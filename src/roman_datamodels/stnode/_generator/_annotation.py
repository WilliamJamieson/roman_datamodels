"""
This module contains the functions for deducing the type annotations for the
stnode classes based on their schemas
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum, auto
from os import PathLike
from typing import TYPE_CHECKING

from ._schemas import RAD_TAG_URIS, class_name_from_uri, module_name_from_uri

if TYPE_CHECKING:
    from ._node import NodeRegister

__all__ = ["schema_object"]


@dataclass(frozen=True)
class AnnotationInput:
    """
    Class to hold the the data to create an annotation
    """

    path: PathLike
    module_name: str
    class_name: str
    property_name: str | None = None

    @property
    def import_string(self) -> str:
        """
        Return the import string for the module
        """

        return f"from .{self.module_name} import {self.class_name}"

    @property
    def next_input(self) -> AnnotationInput:
        """
        Return input that can be derived from this one
        """

        class_name = f"{self.class_name}{self.property_name.capitalize()}"
        module_name = f"{self.module_name}_{self.property_name}"

        return AnnotationInput(self.path, module_name, class_name)

    def property_input(self, property_name: str) -> AnnotationInput:
        """
        Return input that can be derived from this one with a property name
        """

        if self.property_name is not None:
            raise ValueError("Cannot add a property name to an input that already has one")

        return AnnotationInput(self.path, self.module_name, self.class_name, property_name)

    @classmethod
    def from_uri(cls, path: PathLike, uri: str) -> AnnotationInput:
        """
        Create an AnnotationInput from a uri
        """

        module_name = module_name_from_uri(uri)
        class_name = class_name_from_uri(uri)

        return cls(path, module_name, class_name)

    @property
    def tagged_object_base(self) -> str:
        """
        Return base class string for tagged object
        """
        return f"_mixins.{self.class_name}Mixin, _tagged.TaggedObjectNode"

    @property
    def tagged_list_base(self) -> str:
        """
        Return base class string for tagged list
        """
        return f"_mixins.{self.class_name}Mixin, _tagged.TaggedListNode"

    def tagged_scalar_base(self, name: str) -> str:
        """
        Return base class string for tagged scalar
        """
        return f"{name}, _tagged.TaggedScalarNode"

    def ref_node_base(self, annotation: Annotation) -> Annotation:
        """
        Return base class string for a ref node
        """
        if annotation.name == "Any":
            return Annotation("_core.DNode", "from ._core import DNode")
        else:
            return annotation

    def implied_node_base(self, bases: list[Annotation]) -> str:
        """
        Return base class string for an implied node
        """
        return ", ".join(list({base.name for base in bases}))


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
    def get_annotation(cls, register: NodeRegister, data: AnnotationInput, type_: str) -> Annotation:
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
    asdf_unit = "tag:stsci.edu:asdf/unit/unit-1.*"
    time = "tag:stsci.edu:asdf/time/time-1.*"
    quantity = "tag:stsci.edu:asdf/unit/quantity-1.*"
    table = "tag:astropy.org:astropy/table/table-1.*"
    wcs = "tag:stsci.edu:gwcs/wcs-*"
    fps_time = "http://stsci.edu/schemas/asdf/time/time-1.1.0"

    @classmethod
    def get_annotation(cls, register: NodeRegister, data: AnnotationInput, tag: str) -> Annotation:
        """
        Deduce the type annotation from a "tag:" entry in a schema
        """

        match tag:
            case cls.ndarray:
                return Annotation("np.ndarray", "import numpy as np")
            case cls.unit | cls.asdf_unit:
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
            return schema_ref(register, data, tag)

        raise ValueError(f"Unknown tag: {tag}")


def schema_ref(register: NodeRegister, data: AnnotationInput, ref: str) -> Annotation:
    """
    Deduce the type annotation from a "$ref:" entry in a schema
    """
    from ._node import create_ref_object_node

    if ref in AsdfTags:
        return AsdfTags.get_annotation(register, data, ref)

    if ref not in RAD_TAG_URIS:
        create_ref_object_node(register, data, ref)

    return Annotation(class_name_from_uri(ref), f"from .{module_name_from_uri(ref)} import {class_name_from_uri(ref)}")


def schema_any_of(register: NodeRegister, data: AnnotationInput, any_of: list[dict]) -> Annotation:
    """
    Deduce the type annotation from an "anyOf:" entry in a schema
    """
    annotation = None

    for schema in any_of:
        new_annotation = JsonSchemaProperty.get_annotation(register, data, schema)

        if annotation is None:
            annotation = new_annotation
        else:
            annotation.merge_with(new_annotation)

    return annotation


def schema_all_of(register: NodeRegister, data: AnnotationInput, all_of: list[dict]) -> Annotation:
    """
    Deduce the type annotation from an "allOf:" entry in a schema
    """
    from ._node import create_implied_object_node

    if data.property_name is not None:
        bases: list[Annotation] = []
        for schema in all_of:
            if JsonSchemaProperty.ref in schema:
                ref = schema[JsonSchemaProperty.ref]
                if ref in AsdfTags:
                    bases.append(AsdfTags.get_annotation(register, data, ref))
                else:
                    bases.append(schema_ref(register, data, ref))

        new_data = data.next_input
        create_implied_object_node(register, new_data, all_of, bases)

        return Annotation(new_data.class_name, new_data.import_string)

    else:
        annotation = None
        for schema in all_of:
            new_annotation = JsonSchemaProperty.get_annotation(register, data, schema)

            if annotation is None:
                annotation = new_annotation
            else:
                annotation.merge_with(new_annotation)

        return annotation


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
    def get_annotation(cls, register: NodeRegister, data: AnnotationInput, schema: dict) -> Annotation:
        """
        Deduce the type annotation from a property in a schema
        """
        if cls.type in schema:
            return JsonSchemaType.get_annotation(register, data, schema[cls.type])

        if cls.tag in schema:
            return AsdfTags.get_annotation(register, data, schema[cls.tag])

        if cls.ref in schema:
            return schema_ref(register, data, schema[cls.ref])

        if cls.anyOf in schema:
            return schema_any_of(register, data, schema[cls.anyOf])

        if cls.allOf in schema:
            return schema_all_of(register, data, schema[cls.allOf])

        # Fall back on Any
        return Annotation("Any", "from typing import Any")


def schema_annotation(register: NodeRegister, data: AnnotationInput, schema: dict) -> Annotation:
    """
    Deduce the type annotation for a schema
    """

    return JsonSchemaProperty.get_annotation(register, data, schema)


def schema_object(register: NodeRegister, data: AnnotationInput, schema: dict) -> dict[str, Annotation]:
    """
    Deduce the type annotations for the properties of a schema
    """

    annotations = {}

    if "properties" in schema:
        for property_name, property_schema in schema["properties"].items():
            annotations[property_name] = schema_annotation(register, data.property_input(property_name), property_schema)

    return annotations
