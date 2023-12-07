from typing import Callable

from pydantic.fields import FieldInfo

__all__ = ["URI_MODELS", "TAGGED_MODELS", "DATA_MODELS", "REF_MODELS", "URI_TYPES", "TAGGED_TYPES", "register_annotation"]

URI_MODELS = {}
TAGGED_MODELS = {}
DATA_MODELS = {}
REF_MODELS = {}

URI_TYPES = {}
TAGGED_TYPES = {}


def register_annotation(annotation: type) -> None:
    for meta in annotation.__metadata__:
        if isinstance(meta, FieldInfo):
            field_info = meta
            break
    else:
        raise ValueError(f"Annotation {annotation} has no FieldInfo")

    field_info = field_info.json_schema_extra
    if isinstance(field_info, Callable):
        _field_info = {}
        field_info(_field_info)
        field_info = _field_info

    if "id" in field_info:
        uri = field_info["id"]

        if uri in URI_TYPES:
            raise ValueError(f"URI {uri} already registered")

        URI_TYPES[uri] = annotation

    if "tag_id" in field_info:
        tag_uri = field_info["tag_id"]

        if tag_uri in TAGGED_TYPES:
            raise ValueError(f"Tag URI {tag_uri} already registered")

        TAGGED_TYPES[tag_uri] = annotation
