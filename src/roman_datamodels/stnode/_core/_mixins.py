from abc import ABC, abstractmethod

import asdf

__all__ = [
    "SchemaMixin",
    "TagMixin",
]


class SchemaMixin(ABC):
    @classmethod
    @abstractmethod
    def asdf_schema_uri(clas) -> str:
        """URI of the schema that defines this node."""

    @property
    def schema_uri(self):
        return self.asdf_schema_uri()


class TagMixin(SchemaMixin, ABC):
    _ctx = None

    @classmethod
    def asdf_ctx(cls):
        if cls._ctx is None:
            cls._ctx = asdf.AsdfFile()
        return cls._ctx

    @property
    def ctx(self):
        return self.asdf_ctx()

    @classmethod
    @abstractmethod
    def asdf_tag(cls) -> str:
        """Tag of the node."""

    @property
    def tag(self) -> str:
        return self.asdf_tag()

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return cls.asdf_ctx().extension_manager.get_tag_definition(cls.asdf_tag()).schema_uris[0]
