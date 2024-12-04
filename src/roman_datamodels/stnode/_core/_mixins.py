from abc import ABC, abstractmethod

import asdf

__all__ = [
    "AsdfNodeMixin",
    "SchemaMixin",
    "TagMixin",
]


class AsdfNodeMixin:
    """Mixin so that Nodes can have an asdf context."""

    _ctx: asdf.AsdfFile | None = None

    @classmethod
    def asdf_ctx(cls) -> asdf.AsdfFile:
        """Get the asdf context for the class."""
        if cls._ctx is None:
            cls._ctx = asdf.AsdfFile()

        return cls._ctx

    @property
    def ctx(self) -> asdf.AsdfFile:
        """Get the asdf context for the instance."""
        return self.asdf_ctx()


class SchemaMixin(AsdfNodeMixin, ABC):
    """Mixin for nodes to support linking to a schema."""

    @classmethod
    @abstractmethod
    def asdf_schema_uri(clas) -> str:
        """URI of the schema that defines this node."""

    @property
    def schema_uri(self):
        """Get the URI for this instance"""
        return self.asdf_schema_uri()


class TagMixin(SchemaMixin, ABC):
    """Mixin for nodes to support linking to a tag."""

    @classmethod
    @abstractmethod
    def asdf_tag(cls) -> str:
        """Tag of the node."""

    @property
    def tag(self) -> str:
        """Get the tag for this instance."""
        return self.asdf_tag()

    @classmethod
    def asdf_schema_uri(cls) -> str:
        """Get the schema URI for the class using the asdf_tag"""
        return cls.asdf_ctx().extension_manager.get_tag_definition(cls.asdf_tag()).schema_uris[0]
