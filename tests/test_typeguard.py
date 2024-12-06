import asdf
import pytest
from astropy.time import Time

from roman_datamodels.stnode import _base, _core, _registry, _typing, nodes
from roman_datamodels.testing import assert_node_equal


@pytest.fixture
def enable_typeguard():
    """
    Fixture to enable typeguard for testing.
    """
    # Ensure typeguard is disabled (will catch issues that it is accidentally perminantly enabled)
    assert _typing._TYPEGUARD_ENABLED is False

    # Enable typeguard
    with _typing.enable_typeguard():
        assert _typing._TYPEGUARD_ENABLED is True

        yield

    # Ensure typeguard is disabled
    assert _typing._TYPEGUARD_ENABLED is False


class TypeguardExample:
    @_core.rad_field
    def good(self) -> int:
        """This should not raise an error"""
        return 1

    @_core.rad_field
    def bad(self) -> int:
        """This should raise an error"""
        return "1"


@pytest.mark.usefixtures("enable_typeguard")
def test_typeguard_is_functioning():
    """
    Test that the decorator has loaded up the typeguard module.
    -> This smokes out if typeguard is not getting picked up during testing.
    """
    from typeguard import TypeCheckError

    instance = TypeguardExample()
    assert instance.good == 1

    with pytest.raises(TypeCheckError):
        _ = instance.bad


def test_typeguard_decorator():
    """
    This checks that we don't get an error when typeguard is not enabled.
    -> This smokes out getting a typeguard error when it is not enabled.
    """
    assert _typing._TYPEGUARD_ENABLED is False

    instance = TypeguardExample()
    assert instance.good == 1  # always fine
    assert instance.bad == "1"  # should fail if typeguard is enabled


@pytest.mark.usefixtures("enable_typeguard")
@pytest.mark.parametrize("node_cls", _registry.RDM_NODE_REGISTRY.object_nodes.values())
def test_type_annotations(node_cls):
    """
    This will test all @rad_fields's in the given node class.
        -> flush(EXTRA) will cause all of the fields to have their default values set.
        -> test_check_defaults_against_schemas will check that the default values are valid relative
           to the RAD schemas
    """
    instance = node_cls()
    instance.flush(flush=_base.FlushOptions.EXTRA)


@pytest.mark.parametrize("node_cls", _registry.RDM_NODE_REGISTRY.tagged_registry.values())
def test_check_defaults_against_schemas(tmp_path, node_cls):
    """
    Test that the default values for all fields in a given node class are valid relative to the RAD schemas.
        -> with test_type_annoations this confirms that all the annotations are correct
    """

    if issubclass(node_cls, Time):
        instance = node_cls(Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))
    elif node_cls is nodes.Origin or node_cls is nodes.FpsOrigin or node_cls is nodes.TvacOrigin:
        instance = node_cls.STSCI()
    elif node_cls is nodes.Telescope or node_cls is nodes.FpsTelescope or node_cls is nodes.TvacTelescope:
        instance = node_cls.ROMAN()
    else:
        instance = node_cls()

    af = asdf.AsdfFile()
    af["roman"] = instance

    filepath = tmp_path / "test.asdf"
    af.write_to(filepath)

    with asdf.open(filepath) as af:
        assert_node_equal(instance, af["roman"])
