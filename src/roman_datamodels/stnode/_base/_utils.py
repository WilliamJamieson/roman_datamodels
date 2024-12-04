import re

__all__ = ["SchemaProperties", "get_schema_for_property"]


def get_schema_for_property(schema, attr):
    """
    Pull out the schema for a particular property.
    """
    # Check if attr is a property
    subschema = schema.get("properties", {}).get(attr, None)

    # Check if attr is a pattern property
    props = schema.get("patternProperties", {})
    for key, value in props.items():
        if re.match(key, attr):
            subschema = value
            break

    # Have found a schema for the attribute return it
    if subschema is not None:
        return subschema

    # Still have not found a schema for the attribute, so check for combiners
    # and search for the attribute through the entries in the combiners
    for combiner in ["allOf", "anyOf"]:
        for subschema in schema.get(combiner, []):
            subsubschema = get_schema_for_property(subschema, attr)
            if subsubschema != {}:
                return subsubschema

    # Still have not found a schema for the attribute, so return an empty one
    return {}


class SchemaProperties:
    """
    This class provides the capability for using the "contains" machinery
    so that an attribute can be tested against patternProperties as well
    as whether the attribute is explicitly a property of the schema.
    """

    def __init__(self, explicit_properties, patterns):
        self.explicit_properties = explicit_properties
        self.patterns = patterns

    def __contains__(self, attr):
        if attr in self.explicit_properties:
            return True
        else:
            for key in self.patterns.keys():
                if re.match(key, attr):
                    return True
        return False

    def extend(self, other):
        """
        Extend the current SchemaProperties with those from another instance.
        """
        self.explicit_properties = set(self.explicit_properties).union(other.explicit_properties)
        self.patterns.update(other.patterns)

    @classmethod
    def from_schema(cls, schema):
        """
        Create a SchemaProperties object from a schema.
        """

        # Handle the top-level properties
        explicit_properties = schema.get("properties", {}).keys()
        patterns = schema.get("patternProperties", {})
        schema_properties = cls(explicit_properties, patterns)

        # Handle the case where the schema is using an "allOf" combiner
        if "allOf" in schema:
            for subschema in schema["allOf"]:
                schema_properties.extend(cls.from_schema(subschema))

        return schema_properties
