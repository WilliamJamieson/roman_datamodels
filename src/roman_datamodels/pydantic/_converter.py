from __future__ import annotations

from typing import ClassVar

from asdf.extension import Converter

from ._core import BaseRomanTaggedModel
from ._uri import asdf_tag_uri

_ASDF_CONVERTER: RomanDataModelConverter | None = None


class RomanDataModelConverter(Converter):
    _tag_to_model: ClassVar[dict[asdf_tag_uri, type[BaseRomanTaggedModel]] | None] = None

    def __init__(self) -> None:
        global _ASDF_CONVERTER

        if _ASDF_CONVERTER is not None:
            _ASDF_CONVERTER = self

        self = _ASDF_CONVERTER

    @classmethod
    def from_registry(cls, registry: dict[asdf_tag_uri, type[BaseRomanTaggedModel]]) -> RomanDataModelConverter:
        cls._tag_to_model = registry if cls._tag_to_model is None else {**cls._tag_to_model, **registry}
        return cls()

    @property
    def tags(self) -> tuple(str):
        return tuple(self._tag_to_model.keys())

    @property
    def types(self) -> tuple(type):
        return tuple(self._tag_to_model.values())

    def select_tag(self, obj: BaseRomanTaggedModel, tags, ctx) -> asdf_tag_uri:
        return obj._tag_uri

    def to_yaml_tree(self, obj: BaseRomanTaggedModel, tag, ctx) -> dict:
        return obj.to_asdf_tree()

    def from_yaml_tree(self, node, tag, ctx):
        return self._tag_to_model[tag](**node)
