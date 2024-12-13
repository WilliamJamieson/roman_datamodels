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

    class ExampleTaggedScalarNodeSchema(rad.TaggedScalarNode):
        @classmethod
        def asdf_schema_uris(cls):
            return ("test",)

    with pytest.raises(TypeError):
        ExampleTaggedScalarNodeSchema()

    class ExampleTaggedScalarNode(ExampleTaggedScalarNodeSchema):
        @classmethod
        def asdf_tag_uris(cls):
            return {"test": "test"}

    # Show no type error when correct methods are implemented
    _ = ExampleTaggedScalarNode()


def test_abstract_ObjectNode():
    # Test that ObjectNode is an abstract class
    with pytest.raises(TypeError):
        rad.ObjectNode()

    class ExampleObjectNode(rad.ObjectNode):
        @classmethod
        def asdf_schema(cls):
            return {"test": "test"}

    # Show no type error when correct methods are implemented
    _ = ExampleObjectNode()


def test_abstract_SchemaObjectNode():
    # Test that SchemaObjectNode is an abstract class
    with pytest.raises(TypeError):
        rad.SchemaObjectNode()

    class ExampleSchemaObjectNodeRequired(rad.SchemaObjectNode):
        @classmethod
        def asdf_schema_uris(cls):
            return ("test",)

    # Show no type error when correct methods are implemented
    _ = ExampleSchemaObjectNodeRequired()


def test_abstract_TaggedObjectNode():
    # Test that TaggedObjectNode is an abstract class
    with pytest.raises(TypeError):
        rad.TaggedObjectNode()

    class ExampleTaggedObjectNodeSchema(rad.TaggedObjectNode):
        @classmethod
        def asdf_schema_uris(cls):
            return ("test",)

    # Test that TaggedObjectNode needs more than a tag
    with pytest.raises(TypeError):
        ExampleTaggedObjectNodeSchema()

    class ExampleTaggedObjectNodeTag(ExampleTaggedObjectNodeSchema):
        @classmethod
        def asdf_tag_uris(cls):
            return {"test": "test"}

    # Show no type error when correct methods are implemented
    _ = ExampleTaggedObjectNodeTag()
