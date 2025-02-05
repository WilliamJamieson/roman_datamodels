import inspect
from enum import Enum
from unittest import mock

import asdf
import gwcs
import pytest
from astropy import units as u
from astropy.time import Time

from roman_datamodels import _maker_utils, stnode
from roman_datamodels._maker_utils import _ref_files as ref_files
from roman_datamodels.testing import assert_node_equal


@pytest.mark.usefixtures("use_testing_shape")
@pytest.mark.parametrize("node_class", stnode.RDM_NODE_REGISTRY.tagged_registry.values())
def test_maker_utility_implemented(node_class):
    """
    Confirm that a subclass of TaggedObjectNode has a maker utility.

    (note: will be using full defaults for this one)
    """
    instance = _maker_utils.mk_node(node_class)
    assert isinstance(instance, node_class)


@pytest.mark.usefixtures("use_testing_shape")
@pytest.mark.parametrize("node_class", stnode.RDM_NODE_REGISTRY.tagged_registry.values())
def test_instance_valid(node_class):
    """
    Confirm that a class's maker utility creates an object that
    is valid against its schema.
    """
    with asdf.AsdfFile() as af:
        af["node"] = _maker_utils.mk_node(node_class)
        af.validate()


@pytest.mark.usefixtures("use_testing_shape")
@pytest.mark.parametrize(
    "node_class", [c for c in stnode.RDM_NODE_REGISTRY.tagged_registry.values() if issubclass(c, stnode.TaggedObjectNode)]
)
def test_no_extra_fields(node_class, manifest):
    instance = _maker_utils.mk_node(node_class)
    # Remove the keys used to store the default shapes for the maker utility
    instance_keys = set(instance.keys()) - {"_array_shape", "_n_groups", "_n_images"}

    schema_uri = next(t["schema_uri"] for t in manifest["tags"] if t["tag_uri"] == instance._tag)
    schema = asdf.schema.load_schema(schema_uri, resolve_references=True)

    schema_keys = set()
    subschemas = [schema]
    if "allOf" in schema:
        subschemas.extend(schema["allOf"])  # pragma: no cover
    for subschema in subschemas:
        schema_keys.update(subschema.get("properties", {}).keys())

    diff = instance_keys - schema_keys
    assert len(diff) == 0, "Dummy instance has extra keys: " + ", ".join(diff)


@pytest.mark.usefixtures("use_testing_shape")
@pytest.mark.parametrize(
    "name", [c.__name__ for c in stnode.RDM_NODE_REGISTRY.tagged_registry.values() if c.__name__.endswith("Ref")]
)
def test_ref_files_all(name):
    """
    Meta test to confirm that the __all__ in _ref_files.py has an entry for every ref file maker.
    """

    method_name = f"mk_{stnode.camel_case_to_snake_case(name)}"
    assert method_name[:-4] in ref_files.__all__


@pytest.mark.usefixtures("use_testing_shape")
@pytest.mark.parametrize("node_class", stnode.RDM_NODE_REGISTRY.node_datamodel_mapping.keys())
def test_make_datamodel_tests(node_class):
    """
    Meta test to confirm that correct tests exist for each datamodel maker utility.
    """

    from . import test_models as tests

    name = node_class.__name__
    name = _maker_utils.SPECIAL_MAKERS.get(name, stnode.camel_case_to_snake_case(name))
    if name.startswith("mk_"):
        name = name[3:]
    if name.endswith("_ref"):
        name = name[:-4]

    assert hasattr(tests, f"test_make_{name}"), name


@pytest.mark.usefixtures("use_testing_shape")
def test_deprecated():
    """
    mk_rampfitoutput has been deprecated because its name is inconsistent with the other
    maker utilities.  Confirm that it raises a DeprecationWarning.
    """

    with pytest.warns(DeprecationWarning):
        _maker_utils.mk_rampfitoutput()


@pytest.mark.usefixtures("use_testing_shape")
@pytest.mark.parametrize("model_class", [mdl for mdl in _maker_utils.NODE_REGISTRY])
def test_datamodel_maker(model_class):
    """
    Test that the datamodel maker utility creates a valid datamodel.
    """

    model = _maker_utils.mk_datamodel(model_class)

    assert isinstance(model, model_class)
    model.validate()

    if "meta" in model and "model_type" in model.meta:
        assert model.meta.model_type == model_class.__name__


@pytest.mark.usefixtures("use_testing_shape")
@pytest.mark.parametrize("node_class", stnode.RDM_NODE_REGISTRY.node_datamodel_mapping.keys())
def test_override_data(node_class):
    """
    Test that we can override data in any maker, all makers are part included in some datamodel,
    so it is sufficient to work over just the datamodel node classes.

    Note:
        This test is a bit involved because we need to figure out all the possible overrides on the
        fly. The way we do this is to run the maker utility, then walk the resulting node object mutating
        everything along the way. We record the nested dictionary of mutated values and then pass that
        to the maker utility as the override data.

        Note that we use MagicMock objects to create mutated data, this is because they are very
        simple to generate new distinct instances that are easy to check. However, they will not
        pass validation. Because of the way all the maker utilities are implemented, they do not
        themselves validate the data as they make the object, so this is fine. The above tests
        explicitly validate all the maker utility outputs, so we don't need to worry about it here.
        The purpose here is just to inject unique non-default data into the maker utility to override
        its default values.
    """

    def mutate_value(value):
        """
        Generate a mutated value for a given value.
            Note:
                - Time is a special case because it's constructor is picky.
                - TaggedScalarNodes need their type preserved.
        """
        if isinstance(value, Time):
            return value + 1 * u.day

        if isinstance(value, gwcs.WCS):
            return gwcs.WCS(output_frame="fk5")

        if isinstance(value, stnode.TaggedScalarNode):
            return value.__class__(mutate_value(value.__class__.__bases__[0](value)))

        return mock.MagicMock()

    def mutate_node(node):
        """
        Walk the node object and mutate all its values, returning a dict of the mutated values.
        """
        if isinstance(node, stnode.DNode):
            dict_ = {}
            for key in node:
                if key.startswith("_"):
                    continue
                value = mutate_node(getattr(node, key))
                node[key] = value
                dict_[key] = value

            return node.__class__(dict_)

        elif isinstance(node, stnode.LNode):
            return node.__class__([mutate_node(value) for value in node])

        elif isinstance(node, Enum):
            return node
        else:
            return mutate_value(node)

    # Create a node then mutate it.
    node = _maker_utils.mk_node(node_class)

    kwargs = mutate_node(node)

    # Create a new node using the recorded mutation data. Then check it is equal to the mutated object.
    new_node = _maker_utils.mk_node(node_class, **kwargs)

    assert new_node is not node
    assert_node_equal(new_node, node)


@pytest.mark.usefixtures("use_testing_shape")
@pytest.mark.parametrize("node_class", stnode.RDM_NODE_REGISTRY.node_datamodel_mapping.keys())
def test_keyword_only(node_class):
    """
    Ensure all the maker utils at the top level are keyword only.
    """

    maker = _maker_utils._get_node_maker(node_class)
    sig = inspect.signature(maker)

    assert "kwargs" in sig.parameters

    for param in sig.parameters.values():
        if param.name == "kwargs":
            assert param.kind == inspect.Parameter.VAR_KEYWORD
        else:
            assert param.kind == inspect.Parameter.KEYWORD_ONLY


def test_mk_level2_image_shape():
    """
    Regression test for https://github.com/spacetelescope/roman_datamodels/issues/377
    where n_groups was incorrect when provided a 3d shape
    """
    n = _maker_utils.mk_level2_image(shape=(2, 3, 4))
    assert n.amp33.shape == (2, 3, 128)
    assert n.data.shape == (3, 4)
