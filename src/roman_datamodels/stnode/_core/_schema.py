from contextlib import suppress
from typing import Generic, TypeVar

from .._base import AsdfNodeMixin

S = TypeVar("S", bound=dict)

__all__ = ["MissingSchemaKeyError", "RadSchema"]


class MissingSchemaKeyError(KeyError):
    """
    Error for when a key is missing from a schema
    """

    pass


class RadSchema(Generic[S]):
    _required: set[str] | None = None
    _fields: set[str] | None = None

    def __init__(self, node: AsdfNodeMixin, schema: S | None = None):
        self._node = node
        self._schema = schema

    @property
    def node(self) -> type:
        return self._node

    @property
    def schema(self) -> S:
        from ._mixins import SchemaMixin

        if self._schema is None:
            if issubclass(self.node, SchemaMixin):
                self._schema = self.node.get_schema(self.node.asdf_schema_uri())
            else:
                raise TypeError("Can only automatically get the schema for classes that inherit from SchemaMixin")

        return self._schema

    @staticmethod
    def _to_schema_key(key: str) -> str:
        """
        Convert the key to a schema key.

        This is entirely to handle the case where the key is "pass".
            in the schema it is "pass"
            in the node it is "pass_"
        """
        return "pass" if key == "pass_" else key

    @staticmethod
    def _to_node_key(key: str) -> str:
        """
        Convert the key to a node key.

        This is entirely to handle the case where the key is "pass".
            in the schema it is "pass"
            in the node it is "pass_"
        """
        return "pass_" if key == "pass" else key

    def _get_field_schema(self, schema: S, field_name: str) -> S:
        """
        Get the sub-schema for the field
            -> Recursive search the schema for the field

        Parameters
        ----------
        schema : dict
            The schema to get the field sub-schema from from.
            -> public form of this method will pass self.schema in to initiate
               the recursive search
        field_name : str
            The name of the field (property) to get.

        Returns
        -------
        dict
            The raw sub-schema for the field.
        """
        field_name = self._to_schema_key(field_name)

        # Handle the case where the schema has a type listing
        #
        if "type" in schema:
            match schema["type"]:
                # The schema is an object, so we need to search through the properties
                # There are two possibilities we support currently:
                #   - "properties" listing of fields
                #   - "patternProperties" listing of fields
                case "object":
                    if "properties" in schema:
                        if field_name in schema["properties"]:
                            return schema["properties"][field_name]

                    if "patternProperties" in schema:
                        pattern_schema = schema["patternProperties"]

                        for sub_schema in pattern_schema.values():
                            # Search through the various sub-schema patterns
                            # the supppress will just let it wrap around the
                            # loop if that pattern doesn't have the field
                            with suppress(MissingSchemaKeyError):
                                return self._get_field_schema(sub_schema, field_name)

                # The object is an array so now we need to look at the items
                # schema.
                case "array":
                    if "items" in schema:
                        return self._get_field_schema(schema["items"], field_name)

        # If this is using an "allOf" combiner, then we need to search through that
        # list of schemas
        if "allOf" in schema:
            for sub_schema in schema["allOf"]:
                with suppress(MissingSchemaKeyError):
                    return self._get_field_schema(sub_schema, field_name)

        # If this has a $ref, then we need to search through that schema next
        if "$ref" in schema:
            return self._get_field_schema(self.node.get_schema(schema["$ref"]), field_name)

        # Fall back and raise an error if we can't find the field
        raise MissingSchemaKeyError(f"Property '{field_name}' not found in schema for {self.node}")

    def get_field_schema(self, field_name: str) -> S:
        """
        Search this schema to find the schema for the field.

        Parameters
        ----------
        field_name : str
            The name of the field to get the schema for.
        Returns
        -------
        dict
            The raw schema for the field.
        """
        return self._get_field_schema(self.schema, field_name)

    def _get_key(self, schema: S, key: str) -> set[str]:
        """
        Get the sub-schema for the field
            -> Recursive search the schema for the field

        Parameters
        ----------
        schema : dict
            The schema to get the field sub-schema from from.
            -> public form of this method will pass self.schema in to initiate
               the recursive search
        key : str
            Either "required" or "properties" to get the keys for.

        Returns
        -------
        dict
            The raw sub-schema for the field.
        """

        # Handle the case where the schema has a type listing
        #
        if "type" in schema:
            match schema["type"]:
                # The schema is an object, so we need to search through the properties
                # There are two possibilities we support currently:
                #   - "properties" listing of fields
                #   - "patternProperties" listing of fields
                case "object":
                    if key in schema:
                        return set(self._to_node_key(required) for required in schema[key])

                    if "patternProperties" in schema:
                        pattern_schema = schema["patternProperties"]

                        required = set()
                        for sub_schema in pattern_schema.values():
                            required.update(self._get_required(sub_schema))

                        return required

                # The object is an array so now we need to look at the items
                # schema.
                case "array":
                    if "items" in schema:
                        return self._get_required(schema["items"])

        # If this is using an "allOf" combiner, then we need to search through that
        # list of schemas
        if "allOf" in schema:
            required = set()
            for sub_schema in schema["allOf"]:
                required.update(self._get_required(sub_schema))

            return required

        # If this has a $ref, then we need to search through that schema next
        if "$ref" in schema:
            return self._get_required(self.node.get_schema(schema["$ref"]))

        # Fall back and raise an error if we can't find the field
        return set()

    @property
    def required(self) -> set[str]:
        if self._required is None:
            self._required = self._get_required(self.schema, "required")

        return self._required

    @property
    def fields(self) -> set[str]:
        if self._fields is None:
            self._fields = self._get_required(self.schema, "properties")
        return self._fields
