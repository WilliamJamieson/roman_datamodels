from contextlib import nullcontext
from enum import Enum
from importlib import resources as importlib_resources
from inspect import signature
from typing import get_args

import numpy as np
import pytest
import yaml
from astropy import units as u
from astropy.table import Table
from astropy.time import Time
from gwcs import WCS
from rad import resources

from roman_datamodels.stnode import _registry, core, nodes, rad

_RESOURCES_PATH = importlib_resources.files(resources)
_MANIFEST_PATH = _RESOURCES_PATH / "manifests" / "datamodels-1.0.yaml"
_SCHEMAS_PATH = _RESOURCES_PATH / "schemas"


def _schema_files():
    """Generator to grab the RAD schema files directly"""
    for schema_file in _SCHEMAS_PATH.glob("**/**/*.yaml"):
        if schema_file.name == "rad_schema-1.0.0.yaml":
            continue

        yield yaml.safe_load(schema_file.read_bytes())


SCHEMA_FILES = list(_schema_files())


@pytest.mark.parametrize("schema_file", SCHEMA_FILES)
def test_node_exists_for_schema(schema_file):
    """
    Check that every schema file has a corresponding node class
        Note: This also checks that the asdf_schema_uri is correctly diduced
              from the tag uri for tagged nodes.
    """
    uri = schema_file["id"]

    # Check there is a node for this schema
    assert uri in _registry.RDM_NODE_REGISTRY.schema_registry

    # check the class's asdf_schema_uri matches the uri
    assert _registry.RDM_NODE_REGISTRY.schema_registry[uri].asdf_schema_uri() == uri

    # check the class name against the uri
    assert rad.class_name_from_uri(uri) == _registry.RDM_NODE_REGISTRY.schema_registry[uri].__name__


def manifest_tags():
    """
    Generator that directly reads the manifest file in Rad and yields the tag_uri and schema_uri
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
    assert tag_uri in _registry.RDM_NODE_REGISTRY.tagged_registry

    # check the class's asdf_tag matches the tag uri
    assert _registry.RDM_NODE_REGISTRY.tagged_registry[tag_uri].asdf_tag() == tag_uri

    # check the class's asdf_schema_uri matches the schema uri
    assert _registry.RDM_NODE_REGISTRY.tagged_registry[tag_uri].asdf_schema_uri() == schema_uri

    # check the class name against the tag uri
    assert rad.class_name_from_uri(tag_uri) == _registry.RDM_NODE_REGISTRY.tagged_registry[tag_uri].__name__


def parse_orphan_name(name):
    split = name.split("_")
    assert len(split) > 1

    return "_".join(split[:-1]), rad.camel_case_to_snake_case(split[-1])


def get_containing_cls(containing_name):
    # Get the containing class
    assert containing_name in _registry.RDM_NODE_REGISTRY.all_nodes, f"No node found for {containing_name}"
    return _registry.RDM_NODE_REGISTRY.all_nodes[containing_name]


@pytest.mark.parametrize("node_cls", _registry.RDM_NODE_REGISTRY.implied_nodes.values())
def test_implied_node(node_cls):
    """
    Test that the implied nodes follow a consistent naming pattern
        <ContainingNodeName>_<PropertyName>
    """
    assert issubclass(node_cls, rad.ImpliedNodeMixin)
    containing_name, property_name = parse_orphan_name(node_cls.__name__)

    containing_cls = get_containing_cls(containing_name)
    assert node_cls.asdf_implied_by() is containing_cls
    assert node_cls.asdf_implied_property_name() == property_name

    # Check that the property exists on the containing class
    assert hasattr(containing_cls, property_name), f"Property {property_name} not found on {containing_name}"
    cls_property = getattr(containing_cls, property_name)
    assert node_cls.asdf_implied_property() is cls_property

    # Check that the property's return type matches the orphan node
    annotation = signature(cls_property.fget).return_annotation
    assert annotation is node_cls or annotation == core.LNode[node_cls] or annotation == core.DNode[str, node_cls]

    schema = node_cls.asdf_schema().schema

    # Check that the orphan node's schema matches the schema of the property
    if annotation is node_cls:
        assert "allOf" in schema or ("type" in schema and schema["type"] == "object")

    elif annotation == core.LNode[node_cls]:
        assert "type" in schema and schema["type"] == "array"
        assert "items" in schema
        assert "allOf" in schema["items"] or ("type" in schema["items"] and schema["items"]["type"] == "object")

    elif annotation == core.DNode[str, node_cls]:
        assert "type" in schema and schema["type"] == "object"
        assert "patternProperties" in schema
        pattern_schema = schema["patternProperties"][next(iter(schema["patternProperties"]))]
        assert "type" in pattern_schema and pattern_schema["type"] == "object"

    else:
        raise ValueError(f"Annotation {annotation} not handled")


SCHEMA_DICT = {schema["id"]: schema for schema in SCHEMA_FILES}


@pytest.mark.parametrize("node_cls", _registry.RDM_NODE_REGISTRY.object_nodes.values())
def test_node_requires_properties(node_cls):
    """
    Check that every property listed in `asdf_required` in the node class
    """

    for property_name in node_cls.asdf_required():
        property_name = "pass_" if property_name == "pass" else property_name

        assert hasattr(node_cls, property_name), f"Property {property_name} not found on {node_cls}"
        property_cls = getattr(node_cls, property_name)
        assert isinstance(property_cls, property), f"Property {property_name} is not a property"


def get_properties(schema):
    if "properties" in schema:
        properties = set(schema["properties"].keys())

        if "pass" in properties:
            properties.add("pass_")
            properties.remove("pass")
        return properties

    if "$ref" in schema:
        return get_properties(SCHEMA_DICT[schema["$ref"]])

    if "allOf" in schema:
        required = set()
        for sub_schema in schema["allOf"]:
            required.update(get_properties(sub_schema))

        return required

    if "type" in schema:
        if schema["type"] == "array":
            return get_properties(schema["items"])

        if schema["type"] == "object" and "patternProperties" in schema:
            sub_schema = schema["patternProperties"]
            return get_properties(sub_schema[next(iter(sub_schema))])

    return set()


_OBJECT_NODES = rad.get_nodes(rad.ObjectNode, (rad.ObjectNode, rad.SchemaObjectNode, rad.TaggedObjectNode, rad.DataModelNode))


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_fields_in_schema(node_cls):
    """
    Check that every property of the class in the schema
    """
    fields = set(node_cls.asdf_schema().fields)
    # RadSchema cannot properly traverse to nodes that are mixed classes of other
    # implied nodes, this is the only example in RAD, it cannot traverse into the second
    # object
    if node_cls is _registry.RDM_NODE_REGISTRY.all_nodes["DarkRef_Meta_Exposure"]:
        fields = fields | {"type", "p_exptype"}

    assert fields == set(rad.get_node_fields(node_cls))


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_fields(node_cls):
    """
    Check that the fields property returns the correct fields
    """

    properties = set(rad.get_node_fields(node_cls)) | set(node_cls._extra_fields())
    instance = node_cls()
    assert instance._fields is None
    assert properties == set(instance.fields)
    assert properties == set(instance._fields)

    for field in properties:
        assert hasattr(node_cls, field)
        assert isinstance(getattr(node_cls, field), rad.rad_field_property)


def find_property_schema(schema, property_name):
    property_name = "pass" if property_name == "pass_" else property_name
    if "properties" in schema:
        if property_name in schema["properties"]:
            return schema["properties"][property_name]

        raise ValueError(f"Property {property_name} not found in {schema['properties']}")

    if "$ref" in schema:
        return find_property_schema(SCHEMA_DICT[schema["$ref"]], property_name)

    if "allOf" in schema:
        for sub_schema in schema["allOf"]:
            try:
                return find_property_schema(sub_schema, property_name)
            except ValueError:
                continue

        raise ValueError(f"Property {property_name} not found in {schema['allOf']}")

    if "type" in schema:
        if schema["type"] == "array":
            return find_property_schema(schema["items"], property_name)

        if schema["type"] == "object" and "patternProperties" in schema:
            sub_schema = schema["patternProperties"]
            return find_property_schema(sub_schema[next(iter(sub_schema))], property_name)

    raise ValueError(f"Property {property_name} not found in {schema}")


_EXTERNAL_TAG_MAP = {
    "tag:stsci.edu:asdf/time/time-1.*": Time,
    "tag:stsci.edu:asdf/core/ndarray-1.*": np.ndarray,
    "tag:stsci.edu:asdf/unit/quantity-1.*": u.Quantity,
    "tag:stsci.edu:asdf/unit/unit-1.*": u.UnitBase,
    "tag:astropy.org:astropy/units/unit-1.*": u.UnitBase,
    "tag:astropy.org:astropy/table/table-1.*": Table,
    "tag:stsci.edu:gwcs/wcs-*": WCS,
}


def build_annotation_from_schema(schema, annotation):
    if "type" in schema:
        match schema["type"]:
            case "integer":
                return int
            case "number":
                return float
            case "string":
                return str
            case "boolean":
                return bool
            case "object":
                if annotation.__name__ in _registry.RDM_NODE_REGISTRY.implied_nodes:
                    # The orphan nodes are tested separately,
                    #     they are implied by the schema
                    return annotation

                if "patternProperties" in schema:
                    # check that the annotation is for string key dictionary
                    annotation_args = get_args(annotation)
                    assert len(annotation_args) == 2  # base_type, value_type
                    assert annotation_args[0] is core.DNode
                    assert len(annotation_args[1]) == 2  # key_type, value_type
                    assert annotation_args[1][0] is str  # string key

                    # The value should be an orphan node
                    assert annotation_args[1][1].__name__ in _registry.RDM_NODE_REGISTRY.implied_nodes

                    # The annotation is correct in this case
                    return annotation

                return core.DNode
            case "array":
                if "items" in schema:
                    annotation_args = get_args(annotation)
                    # The annotation should have 2 arguments, base and the arg
                    assert len(annotation_args) == 2
                    if len(get_args(annotation_args[0])) > 1:
                        annotation_args = get_args(annotation_args[0])
                    assert annotation_args[0] is core.LNode
                    base_annotation = build_annotation_from_schema(schema["items"], annotation_args[1])

                    return core.LNode[base_annotation]

                raise ValueError(f"Array schema {schema} does not have items")
            case "null" | None:
                return None
            case _:
                raise ValueError(f"Unknown type {schema['type']}")

    if "$ref" in schema:
        if schema["$ref"] in _registry.RDM_NODE_REGISTRY.schema_registry:
            return _registry.RDM_NODE_REGISTRY.schema_registry[schema["$ref"]]
        return build_annotation_from_schema(SCHEMA_DICT[schema["$ref"]], annotation)

    if "tag" in schema:
        if schema["tag"] in _EXTERNAL_TAG_MAP:
            return _EXTERNAL_TAG_MAP[schema["tag"]]

        if schema["tag"] in _registry.RDM_NODE_REGISTRY.tagged_registry:
            return _registry.RDM_NODE_REGISTRY.tagged_registry[schema["tag"]]

    if "anyOf" in schema:
        sub_schemas = schema["anyOf"].copy()
        schema_annotation = build_annotation_from_schema(sub_schemas.pop(0), annotation)
        for sub_schema in sub_schemas:
            schema_annotation = schema_annotation | build_annotation_from_schema(sub_schema, annotation)
        return schema_annotation

    if "allOf" in schema:
        # These result in an orphan node which is tested elsewhere
        assert annotation.__name__ in _registry.RDM_NODE_REGISTRY.implied_nodes
        return annotation

    return None


def get_value_for_coerce(default_value):
    # Handle all the object types AND dicts
    if isinstance(default_value, core.DNode):
        # Strip away the outer node
        value = default_value.__asdf_traverse__()
        assert type(value) is dict

    # Handle all the lists
    elif isinstance(default_value, core.LNode):
        # Strip away the outer node
        value = default_value.__asdf_traverse__()
        assert type(value) is list

    elif isinstance(default_value, rad.SchemaScalarNode):
        # Strip away the scalar node
        value = type(default_value).__bases__[0](default_value)
        assert type(value) is type(default_value).__bases__[0]

    # Handle concrete types
    # This will need to be extended as new types used

    elif isinstance(default_value, str):
        # Strip away the string
        value = 25  # Pick something that is not a string but can be
        assert type(value) is int

    elif isinstance(default_value, int | float):
        # Strip away the int
        value = "25"  # Pick something that can be an int
        assert type(value) is str

    elif isinstance(default_value, Time):
        # Strip away the time object
        value = default_value.to_string()
        assert type(value) is str

    elif isinstance(default_value, Table):
        # Strip away the table
        value = np.arange(1, 10).reshape((3, 3))
        assert type(value) is np.ndarray

    elif isinstance(default_value, u.UnitBase):
        # Strip away the unit
        value = default_value.to_string()
        assert type(value) is str

    elif isinstance(default_value, u.Quantity):
        value = default_value.value.copy()
        assert type(value) is np.ndarray or isinstance(value, np.number)

    elif isinstance(default_value, np.ndarray):
        # Strip away the ndarray
        value = default_value.tolist()
        assert type(value) is list
    else:
        raise ValueError(f"Cannot handle coerce type {type(default_value)}")

    return value


def get_testing_default_values(node_cls, property_name) -> tuple:
    """
    Get clean pair of default values for testing
    """
    array_shape = None
    if issubclass(node_cls, rad.DataModelNode):
        try:
            array_shape = node_cls().array_shape
        except NotImplementedError:
            array_shape = tuple()

        array_shape = len(array_shape) * (1,)

    settings = {"array_shape": array_shape}

    # Pull the default twice and throw away the base node
    # This is to ensure we have two different un-linked instances
    default_value = getattr(node_cls(settings.copy()), property_name)
    compare_value = getattr(node_cls(settings.copy()), property_name)

    # Create a testing instance and show it only contains the array_shape
    instance = node_cls(settings.copy())
    assert instance._data == settings

    return default_value, compare_value, instance


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_wrap_into_node_setting(node_cls):
    """
    Check that things get coerced to the right value during setting
    """

    properties = rad.get_node_fields(node_cls) + node_cls._extra_fields()

    for property_name in properties:
        stored_name = "pass" if property_name == "pass_" else property_name
        default_value, compare_value, instance = get_testing_default_values(node_cls, property_name)

        # These only ones we care about are the nodes
        if not isinstance(default_value, core.DNode | core.LNode | rad.SchemaScalarNode):
            continue

        value = default_value.unwrap()

        # Set the value and show it now exists in _data
        assert stored_name not in instance._data
        setattr(instance, property_name, value)
        assert stored_name in instance._data

        # Check the value is coerced into the correct type for storage
        # lookup coercion prevents checking via the methods on the node
        # instead we have to access the raw data storage directly to
        # check the type
        assert isinstance(instance._data[stored_name], type(compare_value))
        assert isinstance(compare_value, type(instance._data[stored_name]))

        # Double check that using the getattr method gets the right thing
        assert isinstance(getattr(instance, property_name), type(compare_value))
        assert isinstance(compare_value, type(getattr(instance, property_name)))


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_coerce_getting(node_cls):
    """
    Check that things get coerced to the right value when getting
    """

    properties = rad.get_node_fields(node_cls) + node_cls._extra_fields()

    for property_name in properties:
        stored_name = "pass" if property_name == "pass_" else property_name
        default_value, compare_value, _ = get_testing_default_values(node_cls, property_name)

        # These only ones we care about are the nodes
        if not isinstance(default_value, core.DNode | core.LNode | rad.SchemaScalarNode):
            continue
        value = default_value.unwrap()

        # Pass the value directly in so that it is lazy coerced
        instance = node_cls({stored_name: value})
        assert not isinstance(instance._data[stored_name], type(compare_value))

        # Access the value and show it is now coerced
        assert isinstance(getattr(instance, property_name), type(compare_value))

        # Check the value is coerced into the correct type for storage
        # lookup coercion prevents checking via the methods on the node
        # instead we have to access the raw data storage directly to
        # check the type
        assert isinstance(instance._data[stored_name], type(compare_value))
        assert isinstance(compare_value, type(instance._data[stored_name]))

        # Context is not needed as the stored value is updated to the coerced value
        assert isinstance(compare_value, type(getattr(instance, property_name)))


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_flush_none(node_cls):
    """
    Check that the `flush` method works with `FlushOptions.NONE`
    """

    instance = node_cls()
    assert instance._data == {}

    instance.flush(flush=core.FlushOptions.NONE, warn=True)
    assert instance._data == {}  # Nothing should have changed


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_flush_required(node_cls):
    """
    Check that the `flush` method works with `FlushOptions.REQUIRED`
    """

    instance = node_cls()
    assert instance._data == {}

    context = pytest.warns(UserWarning) if instance.required else nullcontext()

    # Check that the instance can be brought into a valid state
    with context:
        instance.flush(warn=True)  # REQUIRED is the default

    keys = set(instance._data.keys())
    if "pass" in keys:
        keys.add("pass_")
        keys.remove("pass")

    assert keys == set(instance.required)


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_flush_all(node_cls):
    """
    Check that the `flush` method works with `FlushOptions.ALL`
    """
    instance = node_cls()
    assert instance._data == {}

    # Check that the instance can be brought into a valid state
    with pytest.warns(UserWarning):
        instance.flush(flush=core.FlushOptions.ALL, warn=True)

    keys = set(instance._data.keys())
    if "pass" in keys:
        keys.add("pass_")
        keys.remove("pass")

    assert keys == set(rad.get_node_fields(node_cls))


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_flush_extra(node_cls):
    """
    Check that the `flush` method works with `FlushOptions.EXTRA`
    """
    instance = node_cls()
    assert instance._data == {}

    # Check that the instance can be brought into a valid state
    with pytest.warns(UserWarning):
        instance.flush(flush=core.FlushOptions.EXTRA, warn=True)

    keys = set(instance._data.keys())
    if "pass" in keys:
        keys.add("pass_")
        keys.remove("pass")

    assert keys == set(rad.get_node_fields(node_cls)) | set(node_cls._extra_fields())


def test_wfi_mode_mixin():
    """
    Test the the wfi mode mixin class works
    """

    # Test when element is a filter
    instance = nodes.WfiMode()
    # default is F158 -> a filter
    assert instance.optical_element == "F158"
    assert instance.filter == "F158"
    assert instance.grating is None

    # Test when element is a grating
    instance = nodes.WfiMode()
    instance.optical_element = "GRISM"
    assert instance.optical_element == "GRISM"
    assert instance.filter is None
    assert instance.grating == "GRISM"


def test_fps_common_mixin():
    """
    Test that the fps common mixin class works
    """
    # This mixes in statistics, which is present in constructors but not in the schema
    instance = nodes.FpsCommon()
    assert "statistics" not in instance._data
    assert instance.statistics is not None
    assert "statistics" in instance._data
    assert isinstance(instance.statistics, nodes.FpsStatistics)

    assert type(instance)._extra_fields() == ("statistics",)


def test_tvac_common_mixin():
    """
    Test that the tvac common mixin class works
    """
    # This mixes in statistics, which is present in constructors but not in the schema
    instance = nodes.TvacCommon()
    assert "statistics" not in instance._data
    assert instance.statistics is not None
    assert "statistics" in instance._data
    assert isinstance(instance.statistics, nodes.TvacStatistics)

    assert type(instance)._extra_fields() == ("statistics",)


def test_ref_common_ref_instrument_mixin():
    """
    Test that the ref common ref instrument mixin class works
    """
    # Not publicly exposed, but it can be found through the RefCommonRef class
    instance = nodes.RefCommonRef().instrument
    # This mixes in optical_element, which is present in constructors but not in the schema
    assert "optical_element" not in instance._data
    assert instance.optical_element is not None
    assert "optical_element" in instance._data
    assert isinstance(instance.optical_element, nodes.WfiOpticalElement)
    assert instance.optical_element == "F158"

    assert type(instance)._extra_fields() == ("optical_element",)


@pytest.mark.parametrize("node_cls", _registry.RDM_NODE_REGISTRY.all_nodes.values())
def test_to_asdf_tree(node_cls):
    """
    Smoke test that the to_asdf_tree method runs without error
    """
    if issubclass(node_cls, Time):
        instance = node_cls(Time.now())
    elif issubclass(node_cls, Enum):
        instance = next(iter(node_cls))
    else:
        instance = node_cls()
    instance.to_asdf_tree(flush=core.FlushOptions.EXTRA)


@pytest.mark.parametrize("node_cls", _registry.RDM_NODE_REGISTRY.all_nodes.values())
def test_asdf_schema(node_cls):
    """
    Smoke test that the asdf_schema method runs without error
    """
    if issubclass(node_cls, Time):
        instance = node_cls(Time.now())
    elif issubclass(node_cls, Enum):
        instance = next(iter(node_cls))
    else:
        instance = node_cls()

    schema = instance.asdf_schema()
    _ = schema.required
    _ = schema.fields
    _ = schema.archive_catalog
    _ = schema.sdf


@pytest.mark.parametrize("node_cls", _registry.RDM_NODE_REGISTRY.enum_nodes.values())
def test_enum_node(node_cls):
    """
    Test that the enum node class matches the schema section it is pointed at
    """
    assert issubclass(node_cls, Enum)
    assert issubclass(node_cls, rad.EnumNodeMixin)

    # Get the enums listed in the schema
    # These are the ones defined explicitly by their own schema file
    if issubclass(node_cls, rad.SchemaScalarNode):
        schema = node_cls.asdf_schema().schema
        assert "enum" in schema
        schema_enum_list = schema["enum"]

    # These are the ones defined by a field in some schema
    else:
        schema_enum_list = node_cls.asdf_schema().schema

    # Check that all the enums listed are in the class
    for entry_name in schema_enum_list:
        assert entry_name in node_cls, f"Enum entry: {entry_name} not listed in Enum: {node_cls}"

    # Check that all the enums in the class are listed in the schema
    if node_cls is _registry.RDM_NODE_REGISTRY.enum_nodes["RefTypeEntry"]:
        # These are a special case as the are implied by a collection of schemas
        return
    for entry in node_cls:
        assert entry.value in schema_enum_list, f"Enum class entry: {entry} not listed in schema for: {node_cls}"


def test_reftype_node():
    """
    Test that the reftype node has entries for each of the RefFiles
    """
    from roman_datamodels.stnode.nodes import reference_files
    from roman_datamodels.stnode.nodes.reference_files import ref

    # Get the entry types from the registry
    types = [value for key, value in _registry.RDM_NODE_REGISTRY.data_model_registry.items() if "reference_files" in key]
    assert len(types) == len(reference_files.__all__) - len(ref.__all__)

    # This is a fill in value for the `ref_common` which will
    # never be used outside testing
    enum_names = ["N/A"]
    for entry in types:
        entry_schema = entry.asdf_schema().fields["meta"].schema
        assert "allOf" in entry_schema
        entry_schema = entry_schema["allOf"]
        for schema in entry_schema:
            if "properties" in schema and "reftype" in schema["properties"]:
                enum_schema = schema["properties"]["reftype"]["enum"]
                print(enum_schema)
                break
        else:
            raise ValueError(f"Could not find reftype enum in {entry}")

        for enum_name in enum_schema:
            assert enum_name in nodes.RefTypeEntry
            enum_names.append(enum_name)

    for entry in nodes.RefTypeEntry:
        assert entry.value in enum_names, f"Extra ref_type entry: {entry}"


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_enum_exists(node_cls):
    """
    Test that properties that have an enum listed in the schema have an enum
    defined in their output annotation
    """
    # This is a special case that is difficult to abstractly search.
    # It should not have an enum in it which is directly exposed,
    # That will be checked by RefExposureTypeRef_Exposure
    if node_cls is _registry.RDM_NODE_REGISTRY.all_nodes["DarkRef_Meta_Exposure"]:
        return

    # Only check the actual fields
    fields = rad.get_node_fields(node_cls)
    for field in fields:
        # These are going to be removed shortly anyways, so I'm not going to
        # bother making enums for them
        if field in ("input_units", "output_units"):
            continue

        field_schema = node_cls.asdf_schema().fields[field].schema

        if "$ref" in field_schema:
            field_schema = node_cls.asdf_schema().get_schema(field_schema["$ref"])

        if "enum" in field_schema:
            field_cls = getattr(node_cls, field)
            annotation = signature(field_cls.fget).return_annotation
            assert issubclass(annotation, Enum), f"Annotation for {node_cls}.{field} should be an Enum"
