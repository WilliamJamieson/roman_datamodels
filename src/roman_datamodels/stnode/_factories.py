"""
Factories for creating Tagged STNode classes from tag_uris.
    These are used to dynamically create classes from the RAD manifest.
"""

import importlib.resources
from typing import Any

import numpy as np
import yaml
from astropy.time import Time
from rad import resources

from . import _mixins, nodes
from ._node import property_factory
from ._registry import OBJECT_NODE_CLASSES_BY_TAG
from ._tagged import TaggedListNode, TaggedObjectNode, TaggedScalarNode, name_from_tag_uri

__all__ = ["stnode_factory"]

# Map of scalar types in the schemas to the python types
SCALAR_TYPE_MAP = {
    "string": str,
    "http://stsci.edu/schemas/asdf/time/time-1.1.0": Time,
}

BASE_SCHEMA_PATH = importlib.resources.files(resources) / "schemas"


def load_schema_from_uri(schema_uri):
    """
    Load the actual schema from the rad resources directly (outside ASDF)
        Outside ASDF because this has to occur before the ASDF extensions are
        registered.

    Parameters
    ----------
    schema_uri : str
        The schema_uri found in the RAD manifest

    Returns
    -------
    yaml library dictionary from the schema
    """
    filename = f"{schema_uri.split('/')[-1]}.yaml"

    if "reference_files" in schema_uri:
        schema_path = BASE_SCHEMA_PATH / "reference_files" / filename
    elif "/fps/tagged_scalars" in schema_uri:
        schema_path = BASE_SCHEMA_PATH / "fps/tagged_scalars" / filename
    elif "/fps/" in schema_uri:
        schema_path = BASE_SCHEMA_PATH / "fps" / filename
    elif "/tvac/tagged_scalars" in schema_uri:
        schema_path = BASE_SCHEMA_PATH / "tvac/tagged_scalars" / filename
    elif "/tvac/" in schema_uri:
        schema_path = BASE_SCHEMA_PATH / "tvac" / filename
    elif "tagged_scalars" in schema_uri:
        schema_path = BASE_SCHEMA_PATH / "tagged_scalars" / filename
    else:
        schema_path = BASE_SCHEMA_PATH / filename

    return yaml.safe_load(schema_path.read_bytes())


def class_name_from_tag_uri(tag_uri):
    """
    Construct the class name for the STNode class from the tag_uri

    Parameters
    ----------
    tag_uri : str
        The tag_uri found in the RAD manifest

    Returns
    -------
    string name for the class
    """
    tag_name = name_from_tag_uri(tag_uri)
    class_name = "".join([p.capitalize() for p in tag_name.split("_")])
    if tag_uri.startswith("asdf://stsci.edu/datamodels/roman/tags/reference_files/"):
        class_name += "Ref"

    return class_name


def docstring_from_tag(tag):
    """
    Read the docstring (if it exists) from the RAD manifest and generate a docstring
        for the dynamically generated class.

    Parameters
    ----------
    tag: dict
        A tag entry from the RAD manifest

    Returns
    -------
    A docstring for the class based on the tag
    """
    docstring = f"{tag['description']}\n\n" if "description" in tag else ""

    return docstring + f"Class generated from tag '{tag['tag_uri']}'"


def scalar_factory(tag):
    """
    Factory to create a TaggedScalarNode class from a tag

    Parameters
    ----------
    tag: dict
        A tag entry from the RAD manifest

    Returns
    -------
    A dynamically generated TaggedScalarNode subclass
    """
    class_name = class_name_from_tag_uri(tag["tag_uri"])
    schema = load_schema_from_uri(tag["schema_uri"])

    # TaggedScalarNode subclasses are really subclasses of the type of the scalar,
    #   with the TaggedScalarNode as a mixin.  This is because the TaggedScalarNode
    #   is supposed to be the scalar, but it needs to be serializable under a specific
    #   ASDF tag.
    # SCALAR_TYPE_MAP will need to be updated as new wrappers of scalar types are added
    #   to the RAD manifest.
    if "type" in schema:
        type_ = schema["type"]
    elif "allOf" in schema:
        type_ = schema["allOf"][0]["$ref"]
    else:
        raise RuntimeError(f"Unknown schema type: {schema}")

    return type(
        class_name,
        (SCALAR_TYPE_MAP[type_], TaggedScalarNode),
        {"_tag": tag["tag_uri"], "__module__": "roman_datamodels.stnode", "__doc__": docstring_from_tag(tag)},
    )


def object_factory(class_name, tag, schema):
    """
    Factory to fill in the class definition for a TaggedObjectNode
    """
    cls = getattr(nodes, class_name)
    cls._tag = tag["tag_uri"]
    cls.__doc__ = docstring_from_tag(tag)
    properties = schema["properties"]

    if "__annotations__" not in cls.__dict__:
        cls.__annotations__ = {}

    for property_name, property_schema in properties.items():
        setattr(cls, property_name, property_factory(property_name))
        if "type" in property_schema:
            match property_schema["type"]:
                case "string":
                    cls.__annotations__[property_name] = str
                case "number":
                    cls.__annotations__[property_name] = float
                case "integer":
                    cls.__annotations__[property_name] = int
                case "boolean":
                    cls.__annotations__[property_name] = bool
                case "array":
                    cls.__annotations__[property_name] = list
                case "object":
                    cls.__annotations__[property_name] = dict
                case _:
                    cls.__annotations__[property_name] = Any
        elif "tag" in property_schema:
            if "ndarray" in property_schema["tag"]:
                cls.__annotations__[property_name] = np.ndarray
            else:
                property_class = class_name_from_tag_uri(property_schema["tag"])
                if hasattr(nodes, property_class):
                    cls.__annotations__[property_name] = getattr(nodes, property_class)
                else:
                    cls.__annotations__[property_name] = Any
        else:
            cls.__annotations__[property_name] = Any

    if cls._tag in OBJECT_NODE_CLASSES_BY_TAG:
        raise RuntimeError(f"TaggedObjectNode class for tag '{cls._tag}' has been defined twice")
    OBJECT_NODE_CLASSES_BY_TAG[cls._tag] = cls

    return cls


def node_factory(tag):
    """
    Factory to create a TaggedObjectNode or TaggedListNode class from a tag

    Parameters
    ----------
    tag: dict
        A tag entry from the RAD manifest

    Returns
    -------
    A dynamically generated TaggedObjectNode or TaggedListNode subclass
    """
    class_name = class_name_from_tag_uri(tag["tag_uri"])
    schema = load_schema_from_uri(tag["schema_uri"])

    if "type" in schema:
        # Determine if the class is a TaggedObjectNode or TaggedListNode based on the
        #   type defined in the schema:
        #   - TaggedObjectNode if type is "object"
        #   - TaggedListNode if type is "array" (array in jsonschema represents Python list)
        if schema["type"] == "object":
            class_type = TaggedObjectNode
        elif schema["type"] == "array":
            class_type = TaggedListNode
        else:
            raise RuntimeError(f"Unknown schema type: {schema['type']}")
    # Use of allOf in the schema indicates that the class is a TaggedObjectNode
    #    which is "extending" another class.
    elif "allOf" in schema:
        class_type = TaggedObjectNode
    else:
        raise RuntimeError(f"Unknown schema type for: {tag['schema_uri']}")

    if class_type == TaggedObjectNode:
        return object_factory(class_name, tag, schema)

    # In special cases one may need to add additional features to a tagged node class.
    #   This is done by creating a mixin class with the name <ClassName>Mixin in _mixins.py
    #   Here we mixin the mixin class if it exists.
    if hasattr(_mixins, mixin := f"{class_name}Mixin"):
        class_type = (class_type, getattr(_mixins, mixin))
    else:
        class_type = (class_type,)

    return type(
        class_name,
        class_type,
        {"_tag": tag["tag_uri"], "__module__": "roman_datamodels.stnode", "__doc__": docstring_from_tag(tag)},
    )


def stnode_factory(tag):
    """
    Construct a tagged STNode class from a tag

    Parameters
    ----------
    tag: dict
        A tag entry from the RAD manifest

    Returns
    -------
    A dynamically generated TaggedScalarNode, TaggedObjectNode, or TaggedListNode subclass
    """
    # TaggedScalarNodes are a special case because they are not a subclass of a
    #   _node class, but rather a subclass of the type of the scalar.
    if "tagged_scalar" in tag["schema_uri"]:
        return scalar_factory(tag)
    else:
        return node_factory(tag)
