from contextlib import nullcontext
from importlib import resources as importlib_resources
from inspect import signature
from pathlib import Path
from typing import get_args

import numpy as np
import pytest
import yaml
from astropy import units as u
from astropy.table import QTable, Table
from astropy.time import Time
from gwcs import WCS
from rad import resources

from roman_datamodels.stnode import _base, _core, nodes

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
    assert uri in nodes.SCHEMA_NODES

    # check the class's asdf_schema_uri matches the uri
    assert nodes.SCHEMA_NODES[uri].asdf_schema_uri() == uri

    # check the class name against the uri
    assert _core.class_name_from_uri(uri) == nodes.SCHEMA_NODES[uri].__name__


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
    assert tag_uri in nodes.TAGGED_NODES

    # check the class's asdf_tag matches the tag uri
    assert nodes.TAGGED_NODES[tag_uri].asdf_tag() == tag_uri

    # check the class's asdf_schema_uri matches the schema uri
    assert nodes.TAGGED_NODES[tag_uri].asdf_schema_uri() == schema_uri

    # check the class name against the tag uri
    assert _core.class_name_from_uri(tag_uri) == nodes.TAGGED_NODES[tag_uri].__name__


@pytest.mark.parametrize("node_cls", nodes.NODES.values())
def test_node_can_be_instantiated(node_cls):
    """
    Check that every node class can be instantiated
    """
    if issubclass(node_cls, Time):
        node_cls(Time.now())
    else:
        node_cls()


def get_orphan_nodes():
    """
    Get all the nodes that are implied by the schemas but do not have their own one
    """
    orphan = nodes.NODES.copy()
    for node_cls in nodes.SCHEMA_NODES.values():
        del orphan[node_cls.__name__]

    return orphan


ORPHAN_NODES = get_orphan_nodes()


def _camel_case_to_snake_case(value):
    """
    Courtesy of https://stackoverflow.com/a/1176023
    """
    import re

    return re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower()


def parse_orphan_name(name):
    split = name.split("_")
    assert len(split) > 1

    return "_".join(split[:-1]), _camel_case_to_snake_case(split[-1])


def get_containing_cls(containing_name):
    # Get the containing class
    assert containing_name in nodes.NODES, f"No node found for {containing_name}"
    return nodes.NODES[containing_name]


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
    if containing_cls in set(nodes.SCHEMA_NODES.values()):
        schema = SCHEMA_DICT[containing_cls.asdf_schema_uri()]
        return parse_schema(schema, property_name)

    new_containing_name, new_property_name = parse_orphan_name(containing_name)
    new_containing_cls = get_containing_cls(new_containing_name)

    return parse_schema(get_schema(new_containing_cls, new_containing_name, new_property_name), property_name)


SCHEMA_DICT = {schema["id"]: schema for schema in SCHEMA_FILES}


@pytest.mark.parametrize("node_cls", ORPHAN_NODES.values())
def test_orphan_node(node_cls):
    """
    Test that the orphan nodes follow a consistent naming pattern
        <ContainingNodeName>_<PropertyName>
    """
    assert issubclass(node_cls, _core.ImpliedNodeMixin)
    assert isinstance(node_cls.asdf_implied_property(), property)

    containing_name, property_name = parse_orphan_name(node_cls.__name__)

    containing_cls = get_containing_cls(containing_name)

    # Check that the property exists on the containing class
    assert hasattr(containing_cls, property_name), f"Property {property_name} not found on {containing_name}"
    cls_property = getattr(containing_cls, property_name)
    assert isinstance(cls_property, property), f"Property {property_name} is not a property"

    # Check that the property's return type matches the orphan node
    annotation = signature(cls_property.fget).return_annotation
    assert annotation is node_cls or annotation == _base.LNode[node_cls] or annotation == _base.DNode[str, node_cls]

    # Check that the orphan node's schema matches the schema of the property
    schema = get_schema(containing_cls, containing_name, property_name)

    if annotation is node_cls:
        assert "allOf" in schema or ("type" in schema and schema["type"] == "object")
        return

    if annotation == _base.LNode[node_cls]:
        assert "type" in schema and schema["type"] == "array"
        assert "items" in schema
        assert "allOf" in schema["items"] or ("type" in schema["items"] and schema["items"]["type"] == "object")
        return

    if annotation == _base.DNode[str, node_cls]:
        assert "type" in schema and schema["type"] == "object"
        assert "patternProperties" in schema
        pattern_schema = schema["patternProperties"][next(iter(schema["patternProperties"]))]
        assert "type" in pattern_schema and pattern_schema["type"] == "object"
        return

    raise ValueError(f"Annotation {annotation} not handled")


_SCHEMA_DICT = {schema["id"]: schema for schema in SCHEMA_FILES}


def get_required(schema):
    if "required" in schema:
        required = set(schema["required"])
        if "pass" in required:
            required.add("pass_")
            required.remove("pass")
        return required

    if "$ref" in schema:
        return get_required(_SCHEMA_DICT[schema["$ref"]])

    if "allOf" in schema:
        required = set()
        for sub_schema in schema["allOf"]:
            required.update(get_required(sub_schema))

        return required

    if "type" in schema:
        if schema["type"] == "array":
            return get_required(schema["items"])

        if schema["type"] == "object" and "patternProperties" in schema:
            sub_schema = schema["patternProperties"]
            return get_required(sub_schema[next(iter(sub_schema))])

    return set()


def find_schema_for_node(node_cls):
    if node_cls.__name__ not in ORPHAN_NODES:
        return _SCHEMA_DICT[node_cls.asdf_schema_uri()]

    containing_name, property_name = parse_orphan_name(node_cls.__name__)
    containing_cls = get_containing_cls(containing_name)

    return get_schema(containing_cls, containing_name, property_name)


@pytest.mark.parametrize("node_cls", nodes.NODES.values())
def test_node_requires(node_cls):
    """
    Check that every schema file with a `required` has a corresponding method
    listing those requirements.
    """

    if not issubclass(node_cls, _core.ObjectNode):
        return

    assert hasattr(node_cls, "asdf_required"), f"No `asdf_required` method found for {node_cls}"

    schema = find_schema_for_node(node_cls)
    assert get_required(schema) == set(node_cls.asdf_required())
    assert isinstance(node_cls.asdf_required(), set)


@pytest.mark.parametrize("node_cls", nodes.NODES.values())
def test_node_requires_properties(node_cls):
    """
    Check that every property listed in `asdf_required` in the node class
    """

    if not issubclass(node_cls, _core.ObjectNode):
        return

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
        return get_properties(_SCHEMA_DICT[schema["$ref"]])

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


_OBJECT_NODES = _core.get_nodes(
    _core.ObjectNode, (_core.ObjectNode, _core.SchemaObjectNode, _core.TaggedObjectNode, _core.DataModelNode)
)


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_properties_in_schema(node_cls):
    """
    Check that every property of the class in the schema
    """

    properties = set(_core.get_node_fields(node_cls))
    schema = find_schema_for_node(node_cls)
    assert get_properties(schema) == properties


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_fields(node_cls):
    """
    Check that the fields property returns the correct fields
    """

    properties = set(_core.get_node_fields(node_cls)) | set(node_cls._extra_fields())
    instance = node_cls()
    assert instance._fields is None
    assert properties == set(instance.fields)
    assert properties == set(instance._fields)


def find_property_schema(schema, property_name):
    property_name = "pass" if property_name == "pass_" else property_name
    if "properties" in schema:
        if property_name in schema["properties"]:
            return schema["properties"][property_name]

        raise ValueError(f"Property {property_name} not found in {schema['properties']}")

    if "$ref" in schema:
        return find_property_schema(_SCHEMA_DICT[schema["$ref"]], property_name)

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
                if annotation.__name__ in ORPHAN_NODES:
                    # The orphan nodes are tested separately,
                    #     they are implied by the schema
                    return annotation

                if "patternProperties" in schema:
                    # check that the annotation is for string key dictionary
                    annotation_args = get_args(annotation)
                    assert len(annotation_args) == 2  # base_type, value_type
                    assert annotation_args[0] is _base.DNode
                    assert len(annotation_args[1]) == 2  # key_type, value_type
                    assert annotation_args[1][0] is str  # string key

                    # The value should be an orphan node
                    assert annotation_args[1][1].__name__ in ORPHAN_NODES

                    # The annotation is correct in this case
                    return annotation

                return _base.DNode
            case "array":
                if "items" in schema:
                    annotation_args = get_args(annotation)
                    # The annotation should have 2 arguments, base and the arg
                    assert len(annotation_args) == 2
                    if len(get_args(annotation_args[0])) > 1:
                        annotation_args = get_args(annotation_args[0])
                    assert annotation_args[0] is _base.LNode
                    base_annotation = build_annotation_from_schema(schema["items"], annotation_args[1])

                    return _base.LNode[base_annotation]

                raise ValueError(f"Array schema {schema} does not have items")
            case "null" | None:
                return None
            case _:
                raise ValueError(f"Unknown type {schema['type']}")

    if "$ref" in schema:
        if schema["$ref"] in nodes.SCHEMA_NODES:
            return nodes.SCHEMA_NODES[schema["$ref"]]
        return build_annotation_from_schema(_SCHEMA_DICT[schema["$ref"]], annotation)

    if "tag" in schema:
        if schema["tag"] in _EXTERNAL_TAG_MAP:
            return _EXTERNAL_TAG_MAP[schema["tag"]]

        if schema["tag"] in nodes.TAGGED_NODES:
            return nodes.TAGGED_NODES[schema["tag"]]

    if "anyOf" in schema:
        sub_schemas = schema["anyOf"].copy()
        schema_annotation = build_annotation_from_schema(sub_schemas.pop(0), annotation)
        for sub_schema in sub_schemas:
            schema_annotation = schema_annotation | build_annotation_from_schema(sub_schema, annotation)
        return schema_annotation

    if "allOf" in schema:
        # These result in an orphan node which is tested elsewhere
        assert annotation.__name__ in ORPHAN_NODES
        return annotation

    return None


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_property_annotation(node_cls):
    """
    Check that the annotation for every property matches the schema
    """

    properties = set(_core.get_node_fields(node_cls))
    schema = find_schema_for_node(node_cls)

    for property_name in properties:
        property_cls = getattr(node_cls, property_name)
        annotation = signature(property_cls.fget).return_annotation
        schema_property = find_property_schema(schema, property_name)
        schema_annotation = build_annotation_from_schema(schema_property, annotation)
        # if schema_annotation is not None:
        # This is a special case because the schemas do not specify that it
        # is supposed to be an astropy Model
        if property_name == "coordinate_distortion_transform":
            assert schema_annotation is _base.DNode
        else:
            assert (
                annotation == schema_annotation
            ), f"Property {property_name} Annotation {annotation} does not match schema {schema_annotation}"


def check_type_fits_annotation(value, annotation):
    annotation_args = get_args(annotation)
    if annotation_args:
        check_type_fits_annotation(value, annotation_args[0])

        if annotation_args[0] is _base.LNode:
            assert len(annotation_args) == 2
            for item in value:
                check_type_fits_annotation(item, annotation_args[1])
    else:
        assert isinstance(value, annotation)


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_lazy_defaults(node_cls):
    """
    Check that every property can successfully be called into existence
    """

    properties = _core.get_node_fields(node_cls) + node_cls._extra_fields()

    for property_name in properties:
        # Generate a fresh instance of the class
        instance = node_cls()

        stored_name = "pass" if property_name == "pass_" else property_name

        if node_cls is nodes.RefCommonRef and stored_name == "reftype":
            continue  # This property is not implemented until the individual meta classes

        # Check the property is not in the instance
        assert stored_name not in instance
        assert stored_name not in instance._data

        # Access via the property
        assert property_name in dir(instance)
        getattr(instance, property_name)

        # Check the property is now in the instance
        assert stored_name in instance
        assert stored_name in instance._data

        # Check the property has the correct type
        property_cls = getattr(node_cls, property_name)
        annotation = signature(property_cls.fget).return_annotation
        check_type_fits_annotation(instance[stored_name], annotation)


def get_value_for_coerce(default_value):
    # Handle all the object types AND dicts
    if isinstance(default_value, _base.DNode):
        # Strip away the outer node
        value = default_value.__asdf_traverse__()
        assert type(value) is dict

    # Handle all the lists
    elif isinstance(default_value, _base.LNode):
        # Strip away the outer node
        value = default_value.__asdf_traverse__()
        assert type(value) is list

    elif isinstance(default_value, _core.SchemaScalarNode):
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
    if issubclass(node_cls, _core.DataModelNode):
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


def coerce_property_skips(node_cls, property_name):
    """
    Check if a property should be skipped during coercion
    """
    from roman_datamodels.stnode.nodes.datamodels.wfi_image import WfiImage_Meta
    from roman_datamodels.stnode.nodes.datamodels.wfi_mosaic import WfiMosaic_Meta

    return (
        # coordinate_distortion_transform is a special case as it is an astropy
        # model so it cannot be coerced to
        (node_cls is nodes.DistortionRef and property_name == "coordinate_distortion_transform")
        # wcs is a special case again as it is a WCS object which cannot be easily coerced
        or ((node_cls is WfiImage_Meta or node_cls is WfiMosaic_Meta) and property_name == "wcs")
    )


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_coerce_setting(node_cls):
    """
    Check that things get coerced to the right value during setting
    """

    properties = _core.get_node_fields(node_cls) + node_cls._extra_fields()

    for property_name in properties:
        if coerce_property_skips(node_cls, property_name):
            continue

        stored_name = "pass" if property_name == "pass_" else property_name
        default_value, compare_value, instance = get_testing_default_values(node_cls, property_name)

        # Quantities are subclasses of np.ndarray so we only need to check for the ndarray
        context = pytest.warns(RuntimeWarning) if isinstance(default_value, np.ndarray) else nullcontext()

        value = get_value_for_coerce(default_value)

        # Set the value and show it now exists in _data
        assert stored_name not in instance._data
        with context:
            setattr(instance, property_name, value)
        assert stored_name in instance._data

        # Check the value is coerced into the correct type for storage
        # lookup coercion prevents checking via the methods on the node
        # instead we have to access the raw data storage directly to
        # check the type
        assert isinstance(instance._data[stored_name], Table if type(compare_value) is QTable else type(compare_value))
        assert isinstance(compare_value, type(instance._data[stored_name]))

        # Double check that using the getattr method gets the right thing
        assert isinstance(getattr(instance, property_name), Table if type(compare_value) is QTable else type(compare_value))
        assert isinstance(compare_value, type(getattr(instance, property_name)))


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_coerce_getting(node_cls):
    """
    Check that things get coerced to the right value when getting
    """

    properties = _core.get_node_fields(node_cls) + node_cls._extra_fields()

    for property_name in properties:
        if coerce_property_skips(node_cls, property_name):
            continue

        stored_name = "pass" if property_name == "pass_" else property_name
        default_value, compare_value, _ = get_testing_default_values(node_cls, property_name)

        # Quantities are subclasses of np.ndarray so we only need to check for the ndarray
        context = pytest.warns(RuntimeWarning) if isinstance(default_value, np.ndarray) else nullcontext()

        value = get_value_for_coerce(default_value)

        # Pass the value directly in so that it is lazy coerced
        instance = node_cls({stored_name: value})
        assert not isinstance(instance._data[stored_name], type(compare_value))

        # Access the value and show it is now coerced
        with context:
            this = getattr(instance, property_name)
            print(this)
            print(type(this))
            assert isinstance(getattr(instance, property_name), Table if type(compare_value) is QTable else type(compare_value))

        # Check the value is coerced into the correct type for storage
        # lookup coercion prevents checking via the methods on the node
        # instead we have to access the raw data storage directly to
        # check the type
        assert isinstance(instance._data[stored_name], Table if type(compare_value) is QTable else type(compare_value))
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

    instance.flush(flush=_base.FlushOptions.NONE, warn=True)
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
        instance.flush(flush=_base.FlushOptions.ALL, warn=True)

    keys = set(instance._data.keys())
    if "pass" in keys:
        keys.add("pass_")
        keys.remove("pass")

    assert keys == set(_core.get_node_fields(node_cls))


@pytest.mark.parametrize("node_cls", _OBJECT_NODES.values())
def test_flush_extra(node_cls):
    """
    Check that the `flush` method works with `FlushOptions.EXTRA`
    """
    instance = node_cls()
    assert instance._data == {}

    # Check that the instance can be brought into a valid state
    with pytest.warns(UserWarning):
        instance.flush(flush=_base.FlushOptions.EXTRA, warn=True)

    keys = set(instance._data.keys())
    if "pass" in keys:
        keys.add("pass_")
        keys.remove("pass")

    assert keys == set(_core.get_node_fields(node_cls)) | set(node_cls._extra_fields())


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


@pytest.mark.parametrize("node_cls", nodes.NODES.values())
def test_to_asdf_tree(node_cls):
    """
    Smoke test that the to_asdf_tree method runs without error
    """
    instance = node_cls(Time.now()) if issubclass(node_cls, Time) else node_cls()
    instance.to_asdf_tree()


@pytest.mark.parametrize("node_cls", nodes.NODES.values())
def test_asdf_schema(node_cls):
    """
    Smoke test that the asdf_schema method runs without error
    """
    instance = node_cls(Time.now()) if issubclass(node_cls, Time) else node_cls()
    schema = instance.asdf_schema()
    if issubclass(node_cls, _core.ObjectNode):
        assert schema.required == set(instance.required)
