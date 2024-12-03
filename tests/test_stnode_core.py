import pytest

from roman_datamodels.stnode import _core


def test_abstract_SchemaScalarNode():
    # Test that SchemaScalarNode is an abstract class
    with pytest.raises(TypeError):
        _core.SchemaScalarNode()

    class ExampleSchemaScalarNode(_core.SchemaScalarNode):
        @classmethod
        def asdf_schema_uri(cls):
            return "test"

    # Show no type error when correct methods are implemented
    _ = ExampleSchemaScalarNode()


def test_abstract_TaggedScalarNode():
    # Test that TaggedScalarNode is an abstract class
    with pytest.raises(TypeError):
        _core.TaggedScalarNode()

    class ExampleTaggedScalarNode(_core.TaggedScalarNode):
        @classmethod
        def asdf_tag(cls):
            return "test"

    # Show no type error when correct methods are implemented
    _ = ExampleTaggedScalarNode()


def test_abstract_ObjectNode():
    # Test that ObjectNode is an abstract class
    with pytest.raises(TypeError):
        _core.ObjectNode()

    class ExampleObjectNode(_core.ObjectNode):
        @classmethod
        def asdf_required(cls):
            return ("test",)

    # Show no type error when correct methods are implemented
    _ = ExampleObjectNode()


def test_abstract_SchemaObjectNode():
    # Test that SchemaObjectNode is an abstract class
    with pytest.raises(TypeError):
        _core.SchemaObjectNode()

    class ExampleSchemaObjectNodeUri(_core.SchemaObjectNode):
        @classmethod
        def asdf_schema_uri(cls):
            return "test"

    # Test that SchemaObjectNode needs more than a URI
    with pytest.raises(TypeError):
        ExampleSchemaObjectNodeUri()

    class ExampleSchemaObjectNodeRequired(ExampleSchemaObjectNodeUri):
        @classmethod
        def asdf_required(cls):
            return ("test",)

    # Show no type error when correct methods are implemented
    _ = ExampleSchemaObjectNodeRequired()


def test_abstract_TaggedObjectNode():
    # Test that TaggedObjectNode is an abstract class
    with pytest.raises(TypeError):
        _core.TaggedObjectNode()

    class ExampleTaggedObjectNodeTag(_core.TaggedObjectNode):
        @classmethod
        def asdf_tag(cls):
            return "test"

    # Test that TaggedObjectNode needs more than a tag
    with pytest.raises(TypeError):
        ExampleTaggedObjectNodeTag()

    class ExampleTaggedObjectNodeRequired(ExampleTaggedObjectNodeTag):
        @classmethod
        def asdf_required(cls):
            return ("test",)

    # Show no type error when correct methods are implemented
    _ = ExampleTaggedObjectNodeRequired()
