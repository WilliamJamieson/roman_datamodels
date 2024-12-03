from importlib import resources as importlib_resources
from inspect import signature
from pathlib import Path

import pytest
import yaml
from rad import resources

from roman_datamodels.stnode import _core, _nodes

_RESOURCES_PATH = importlib_resources.files(resources)
_MANIFEST_PATH = _RESOURCES_PATH / "manifests" / "datamodels-1.0.yaml"
_SCHEMAS_PATH = _RESOURCES_PATH / "schemas"


def load_schema(file_path) -> dict:
    """
    Load a schema from a file path
    """
    file_path = Path(file_path)
    return yaml.safe_load(file_path.read_bytes())


def schema_files():
    """
    Generator for schema files
    """
    for schema_file in _SCHEMAS_PATH.glob("**/**/*.yaml"):
        if schema_file.name == "rad_schema-1.0.0.yaml":
            continue

        yield load_schema(schema_file)


SCHEMA_FILES = list(schema_files())


@pytest.mark.parametrize("schema_file", SCHEMA_FILES)
def test_node_exists_for_schema(schema_file):
    """
    Check that every schema file has a corresponding node class

    Note this also checks that the `asdf_schema_uri` is correctly
    implemented.
    """
    uri = schema_file["id"]

    # Check there is a node for this schema
    assert uri in _nodes.SCHEMA_NODES

    # check the class's asdf_schema_uri matches the uri
    assert _nodes.SCHEMA_NODES[uri].asdf_schema_uri() == uri

    # check the class name against the uri
    assert _core.class_name_from_uri(uri) == _nodes.SCHEMA_NODES[uri].__name__


def manifest_tags():
    """
    Generator for manifest tags
    """

    manifest = yaml.safe_load(_MANIFEST_PATH.read_bytes())

    for tag_entry in manifest["tags"]:
        yield (tag_entry["tag_uri"], tag_entry["schema_uri"])


MANIFEST_TAGS = list(manifest_tags())


@pytest.mark.parametrize("tag_uri, schema_uri", MANIFEST_TAGS)
def test_node_exists_for_manifest_tag(tag_uri, schema_uri):
    """
    Check that every tag in the manifest has a corresponding node class
    """
    # Check that there is a node for this tag
    assert tag_uri in _nodes.TAGGED_NODES

    # check the class's asdf_tag matches the tag uri
    assert _nodes.TAGGED_NODES[tag_uri].asdf_tag() == tag_uri

    # check the class's asdf_schema_uri matches the schema uri
    assert _nodes.TAGGED_NODES[tag_uri].asdf_schema_uri() == schema_uri

    # check the class name against the tag uri
    assert _core.class_name_from_uri(tag_uri) == _nodes.TAGGED_NODES[tag_uri].__name__


@pytest.mark.parametrize("schema_file", SCHEMA_FILES)
def test_node_requires(schema_file):
    """
    Check that every schema file with a `required` has a corresponding method
    listing those requirements.
    """

    if "required" in schema_file:
        node_cls = _nodes.SCHEMA_NODES[schema_file["id"]]

        # Check that the class has a `requires` method
        assert issubclass(node_cls, _core.ObjectNode)
        assert node_cls is not _core.ObjectNode

        print(schema_file["id"])
        assert set(schema_file["required"]) == set(node_cls.asdf_required())


def get_orphan_nodes():
    """
    Get all the nodes that are implied by the schemas but do not have their own one
    """
    nodes = _nodes.NODES.copy()
    for node_cls in _nodes.SCHEMA_NODES.values():
        del nodes[node_cls.__name__]

    return nodes


ORPHAN_NODES = get_orphan_nodes()


def _camel_case_to_snake_case(value):
    """
    Courtesy of https://stackoverflow.com/a/1176023
    """
    import re

    return re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower()


SCHEMA_DICT = {schema["id"]: schema for schema in SCHEMA_FILES}


@pytest.mark.parametrize("node_cls", ORPHAN_NODES.values())
def test_orphan_node(node_cls):
    """
    Test that the orphan nodes follow a consistent naming pattern
        <ContainingNodeName>_<PropertyName>
    """

    def parse_orphan_name(name):
        split = name.split("_")
        assert len(split) > 1

        return "_".join(split[:-1]), _camel_case_to_snake_case(split[-1])

    containing_name, property_name = parse_orphan_name(node_cls.__name__)

    def get_containing_cls(containing_name):
        # Get the containing class
        assert containing_name in _nodes.NODES, f"No node found for {containing_name}"
        return _nodes.NODES[containing_name]

    containing_cls = get_containing_cls(containing_name)

    # Check that the property exists on the containing class
    assert hasattr(containing_cls, property_name), f"Property {property_name} not found on {containing_name}"
    cls_property = getattr(containing_cls, property_name)
    assert isinstance(cls_property, property), f"Property {property_name} is not a property"

    # Check that the property's return type matches the orphan node
    annotation = signature(cls_property.fget).return_annotation
    assert annotation is node_cls or annotation == list[node_cls] or annotation == dict[str, node_cls]

    def parse_schema(schema, property_name):
        if "type" in schema:
            if schema["type"] == "object":
                if "properties" in schema:
                    if property_name in schema["properties"]:
                        return schema["properties"][property_name]
                    return None
            elif schema["type"] == "array":
                return parse_schema(schema["items"], property_name)

        if "allOf" in schema:
            for sub_schema in schema["allOf"]:
                if all_of_schema := parse_schema(sub_schema, property_name):
                    return all_of_schema
            else:
                raise ValueError(f"Property {property_name} not found in {schema['allOf']}")

        return None

    def get_schema(containing_cls, containing_name, property_name):
        if containing_cls in set(_nodes.SCHEMA_NODES.values()):
            schema = SCHEMA_DICT[containing_cls.asdf_schema_uri()]
            return parse_schema(schema, property_name)

        new_containing_name, new_property_name = parse_orphan_name(containing_name)
        new_containing_cls = get_containing_cls(new_containing_name)

        s = get_schema(new_containing_cls, new_containing_name, new_property_name)
        return parse_schema(s, property_name)

    # Check that the orphan node's schema matches the schema of the property
    schema = get_schema(containing_cls, containing_name, property_name)

    if annotation is node_cls:
        assert "allOf" in schema or ("type" in schema and schema["type"] == "object")

    if annotation == list[node_cls]:
        assert "type" in schema and schema["type"] == "array"
        assert "items" in schema
        assert "allOf" in schema["items"] or ("type" in schema["items"] and schema["items"]["type"] == "object")

    if annotation == dict[str, node_cls]:
        assert "type" in schema and schema["type"] == "object"
        assert "patternProperties" in schema
        pattern_schema = schema["patternProperties"][next(iter(schema["patternProperties"]))]
        assert "type" in pattern_schema and pattern_schema["type"] == "object"
