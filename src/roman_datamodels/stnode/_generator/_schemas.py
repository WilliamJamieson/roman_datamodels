"""
Utilities for handling schemas
"""

import importlib.resources
from os import PathLike
from pathlib import Path

import yaml
from rad import resources

__all__ = [
    "RAD_TAG_URIS",
    "load_schema_from_uri",
    "module_name_from_uri",
    "class_name_from_uri",
    "docstring_from_tag",
]

# Load the manifest directly from the rad resources and not from ASDF.
#   This is because the ASDF extensions have to be created before they can be registered
#   and this module creates the classes used by the ASDF extension.
_RESOURCES = importlib.resources.files(resources)
_MANIFEST = _RESOURCES / "manifests" / "datamodels-1.0.yaml"
_SCHEMAS = _RESOURCES / "schemas"


def load_schema(file_path: PathLike) -> dict:
    """
    Load a schema from a file path
    """
    file_path = Path(file_path)
    return yaml.safe_load(file_path.read_bytes())


RAD_TAGS = load_schema(_MANIFEST)["tags"]
RAD_TAG_URIS = [tag["tag_uri"] for tag in RAD_TAGS]


def load_schema_from_uri(schema_uri) -> dict:
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
        schema_path = _SCHEMAS / "reference_files" / filename
    elif "/fps/tagged_scalars" in schema_uri:
        schema_path = _SCHEMAS / "fps/tagged_scalars" / filename
    elif "/fps/" in schema_uri:
        schema_path = _SCHEMAS / "fps" / filename
    elif "/tvac/tagged_scalars" in schema_uri:
        schema_path = _SCHEMAS / "tvac/tagged_scalars" / filename
    elif "/tvac/" in schema_uri:
        schema_path = _SCHEMAS / "tvac" / filename
    elif "tagged_scalars" in schema_uri:
        schema_path = _SCHEMAS / "tagged_scalars" / filename
    else:
        schema_path = _SCHEMAS / filename

    return load_schema(schema_path)


def module_name_from_uri(uri):
    """
    Compute the name of the schema from the utri

    Parameters
    ----------
    uri : str
        The uri to find the name from
    """
    name = uri.split("/")[-1].split("-")[0]

    # Handle tvac, fps, and reference files
    if "/tvac/" in uri and "tvac" not in name:
        name = f"tvac_{name}"
    elif "/fps/" in uri and "fps" not in name:
        name = f"fps_{name}"
    elif "/reference_files/" in uri:
        name = f"{name}_ref"

    return name


def class_name_from_uri(uri):
    """
    Construct the class name for the STNode class from the tag_uri

    Parameters
    ----------
    uri : str
        The uri in question

    Returns
    -------
    string name for the class
    """
    return "".join([p.capitalize() for p in module_name_from_uri(uri).split("_")])


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
    docstring += f"Class generated from tag '{tag['tag_uri']}'"

    return f'"""\n{docstring}\n"""'


def camel_case_to_snake_case(value):
    """
    Courtesy of https://stackoverflow.com/a/1176023
    """
    import re

    return re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower()
