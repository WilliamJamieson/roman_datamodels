from __future__ import annotations

from contextlib import contextmanager
from inspect import isclass
from typing import Any, ClassVar, Union

from pydantic import BaseModel, ConfigDict
from pydantic.config import JsonDict

from ._archive import Archive
from ._uri import asdf_tag_uri, asdf_uri

__all__ = ["BaseDataModel", "BaseRomanRefModel", "BaseRomanDataModel", "Number"]

Number = Union[int, float]


def _asdf_schema_modify(json_schema: JsonDict, cls: BaseRomanModel) -> None:
    # Create the required fields entry
    optional = () if cls._optional_fields_ is None else cls._optional_fields_
    json_schema["required"] = [field for field in cls.model_fields if field not in optional]

    # Add the URI
    if issubclass(cls, BaseRomanURIModel):
        json_schema["id"] = cls._uri

    for field_name, field in cls.model_fields.items():
        # Turn Archive objects into their JSON schema
        field_name_ = field_name if field.alias is None else field.alias
        if isinstance(field.json_schema_extra, Archive):
            # archive = {key: value for key, value in field.json_schema_extra.model_dump().items() if value is not None}
            json_schema["properties"][field_name_] = {
                **json_schema["properties"][field_name_],
                **field.json_schema_extra.model_dump(exclude_none=True),
            }

        # Short circuit tagged models at their tags.
        if isclass(field.annotation) and issubclass(field.annotation, BaseRomanTaggedModel):
            json_schema["properties"][field_name] = {"tag": field.annotation._tag_uri}

    # Add property order
    if issubclass(cls, BaseRomanTaggedModel):
        json_schema["propertyOrder"] = list(cls.model_fields.keys())
        json_schema["flowStyle"] = "block"


class BaseDataModel(BaseModel):
    model_config = ConfigDict(
        # Allow enum values to be used in the model to define allowed values
        use_enum_values=True,
        # Validate values when they are set
        validate_assignment=True,
        revalidate_instances="always",
        extra="allow",
    )

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

    def __setitem__(self, key: str, value: Any) -> None:
        setattr(self, key, value)

    @contextmanager
    def pause_validation(self, revalidate_on_exit: bool = True) -> None:
        self.model_config["validate_assignment"] = False

        try:
            yield
        finally:
            self.model_config["validate_assignment"] = True

            if revalidate_on_exit:
                self.model_validate(self)


class BaseRomanModel(BaseDataModel):
    _optional_fields_: ClassVar[tuple[str] | None] = None
    _optional_fields: ClassVar[tuple[str] | None] = None

    def __init_subclass__(cls, **kwargs: Any):
        super().__init_subclass__(**kwargs)

        if cls._optional_fields is not None:
            if cls._optional_fields_ is None:
                cls._optional_fields_ = ()

            cls._optional_fields_ += cls._optional_fields

    model_config = ConfigDict(
        json_schema_extra=_asdf_schema_modify,
    )

    def to_asdf_tree(self) -> dict[str, Any]:
        tree = dict(self)

        for field_name, obj in tree.items():
            if isinstance(obj, BaseRomanModel) and not isinstance(obj, BaseRomanTaggedModel):
                tree[field_name] = obj.to_asdf_tree()

            if isinstance(obj, dict):
                for entry, dict_obj in obj.items():
                    if isinstance(dict_obj, BaseRomanModel) and not isinstance(dict_obj, BaseRomanTaggedModel):
                        obj[entry] = dict_obj.to_asdf_tree()

            if isinstance(obj, list):
                for idx, list_obj in enumerate(obj):
                    if isinstance(list_obj, BaseRomanModel) and not isinstance(list_obj, BaseRomanTaggedModel):
                        obj[idx] = list_obj.to_asdf_tree()

        return tree

    @classmethod
    def tagged_model_fields(cls) -> list[Any]:
        return [
            field
            for field in cls.model_fields.values()
            if isclass(field.annotation) and issubclass(field.annotation, BaseRomanTaggedModel)
        ]


class BaseRomanURIModel(BaseRomanModel):
    _uri: ClassVar[asdf_uri | None] = None


class BaseRomanTaggedModel(BaseRomanURIModel):
    _tag_uri: ClassVar[asdf_tag_uri | None] = None


class BaseRomanDataModel(BaseRomanTaggedModel):
    ...


class BaseRomanRefModel(BaseRomanTaggedModel):
    ...
