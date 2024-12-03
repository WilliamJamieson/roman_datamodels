from importlib import resources as importlib_resources
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
