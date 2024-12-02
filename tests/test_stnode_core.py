import pytest

from roman_datamodels.stnode import _core


def test_abstract_SchemaScalarNode():
    # Test that SchemaScalarNode is an abstract class
    with pytest.raises(TypeError):
        _core.SchemaScalarNode()

    class ExampleSchemaScalarNode(_core.SchemaScalarNode):
        @property
        def schema_uri(self):
            return "test"

    # Show no type error when correct methods are implemented
    _ = ExampleSchemaScalarNode()


def test_abstract_TaggedScalarNode():
    # Test that TaggedScalarNode is an abstract class
    with pytest.raises(TypeError):
        _core.TaggedScalarNode()

    class ExampleTaggedScalarNode(_core.TaggedScalarNode):
        @property
        def tag(self):
            return "test"

    # Show no type error when correct methods are implemented
    _ = ExampleTaggedScalarNode()


def test_abstract_ObjectNode():
    # Test that ObjectNode is an abstract class
    with pytest.raises(TypeError):
        _core.ObjectNode()

    class ExampleObjectNode(_core.ObjectNode):
        @property
        def required(self):
            return ("test",)

    # Show no type error when correct methods are implemented
    _ = ExampleObjectNode()


def test_abstract_SchemaObjectNode():
    # Test that SchemaObjectNode is an abstract class
    with pytest.raises(TypeError):
        _core.SchemaObjectNode()

    class ExampleSchemaObjectNodeUri(_core.SchemaObjectNode):
        @property
        def schema_uri(self):
            return "test"

    # Test that SchemaObjectNode needs more than a URI
    with pytest.raises(TypeError):
        ExampleSchemaObjectNodeUri()

    class ExampleSchemaObjectNodeRequired(ExampleSchemaObjectNodeUri):
        @property
        def required(self):
            return ("test",)

    # Show no type error when correct methods are implemented
    _ = ExampleSchemaObjectNodeRequired()


def test_abstract_TaggedObjectNode():
    # Test that TaggedObjectNode is an abstract class
    with pytest.raises(TypeError):
        _core.TaggedObjectNode()

    class ExampleTaggedObjectNodeTag(_core.TaggedObjectNode):
        @property
        def tag(self):
            return "test"

    # Test that TaggedObjectNode needs more than a tag
    with pytest.raises(TypeError):
        ExampleTaggedObjectNodeTag()

    class ExampleTaggedObjectNodeRequired(ExampleTaggedObjectNodeTag):
        @property
        def required(self):
            return ("test",)

    # Show no type error when correct methods are implemented
    _ = ExampleTaggedObjectNodeRequired()
