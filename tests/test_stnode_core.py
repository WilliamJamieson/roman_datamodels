import pytest

from roman_datamodels.stnode import rad


def test_abstract_SchemaScalarNode():
    # Test that SchemaScalarNode is an abstract class
    with pytest.raises(TypeError):
        rad.SchemaScalarNode()

    class ExampleSchemaScalarNode(rad.SchemaScalarNode):
        @classmethod
        def asdf_schema_uris(cls):
            return "test"

    # Show no type error when correct methods are implemented
    _ = ExampleSchemaScalarNode()


def test_abstract_TaggedScalarNode():
    # Test that TaggedScalarNode is an abstract class
    with pytest.raises(TypeError):
        rad.TaggedScalarNode()

    class ExampleTaggedScalarNode(rad.TaggedScalarNode):
        @classmethod
        def asdf_tag_uris(cls):
            return "test"

    # Show no type error when correct methods are implemented
    _ = ExampleTaggedScalarNode()


def test_abstract_ObjectNode():
    # Test that ObjectNode is an abstract class
    with pytest.raises(TypeError):
        rad.ObjectNode()

    class ExampleObjectNode(rad.ObjectNode):
        @classmethod
        def asdf_required(cls):
            return ("test",)

    # Show no type error when correct methods are implemented
    _ = ExampleObjectNode()


def test_abstract_SchemaObjectNode():
    # Test that SchemaObjectNode is an abstract class
    with pytest.raises(TypeError):
        rad.SchemaObjectNode()

    class ExampleSchemaObjectNodeUri(rad.SchemaObjectNode):
        @classmethod
        def asdf_schema_uris(cls):
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
        rad.TaggedObjectNode()

    class ExampleTaggedObjectNodeTag(rad.TaggedObjectNode):
        @classmethod
        def asdf_tag_uris(cls):
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
