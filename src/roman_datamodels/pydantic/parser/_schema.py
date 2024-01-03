from __future__ import annotations

from typing import Any

from datamodel_code_generator.parser.jsonschema import JsonSchemaObject

from ._utils import get_manifest_maps

__all__ = ["RadSchemaObject"]


class RadSchemaObject(JsonSchemaObject):
    """Modifications to the JsonSchemaObject to support reading Rad schemas"""

    items: list[RadSchemaObject] | RadSchemaObject | bool | None = None
    additionalProperties: RadSchemaObject | bool | None = None
    patternProperties: dict[str, RadSchemaObject] | None = None
    oneOf: list[RadSchemaObject] = []
    anyOf: list[RadSchemaObject] = []
    allOf: list[RadSchemaObject] = []
    properties: dict[str, RadSchemaObject | bool] | None = None
    id: str | None = None
    tag: str | None = None
    astropy_type: str | None = None
    tag_uri: str | None = None

    def model_post_init(self, __context: Any) -> None:
        """Custom post processing for RadSchemaObject"""

        manifest_maps = get_manifest_maps()

        # Turn tags into references
        if self.tag is not None:
            if self.tag in manifest_maps.tag_to_uri:
                if self.ref is not None:
                    raise ValueError("Cannot set both tag and ref")

                self.ref = manifest_maps.tag_to_uri[self.tag]

        # Handle external reference (this is a bit of a hack)
        if self.astropy_type is not None:
            self.custom_type_path = self.astropy_type
            self.allOf = []

        # Set the tag_uri if it has one
        if self.id is not None:
            if self.id in manifest_maps.uri_to_tag:
                self.tag_uri = manifest_maps.uri_to_tag[self.id]


RadSchemaObject.model_rebuild()
