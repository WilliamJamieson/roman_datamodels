from abc import ABC, abstractmethod

import asdf

from ._base import DNode


def get_schema_from_tag(ctx, tag):
    """
    Look up and load ASDF's schema corresponding to the tag_uri.

    Parameters
    ----------
    ctx :
        An ASDF file context.
    tag : str
        The tag_uri of the schema to load.
    """
    schema_uri = ctx.extension_manager.get_tag_definition(tag).schema_uris[0]

    return asdf.schema.load_schema(schema_uri, resolve_references=True)


class SchemaMixin(ABC):
    @property
    @abstractmethod
    def schema_uri(self):
        """URI of the schema that defines this node."""


class TagMixin(SchemaMixin, ABC):
    @property
    @abstractmethod
    def ctx(self):
        """The ASDF file context."""

    @property
    @abstractmethod
    def tag(self):
        """Tag of the node."""

    @property
    def schema_uri(self):
        return self.ctx.extension_manager.get_tag_definition(self.tag).schema_uris[0]


class SchemaObjectNode(DNode, SchemaMixin, ABC):
    @property
    @abstractmethod
    def required(self) -> tuple[str]:
        """List of required fields in this node."""


class TaggedObjectNode(SchemaObjectNode, TagMixin, ABC): ...


class SchemaScalarNode(SchemaMixin, ABC): ...


class TaggedScalarNode(SchemaScalarNode, TagMixin, ABC):
    """
    Base class for all tagged scalars defined by RAD
        There will be one of these for any tagged object defined by RAD, which has
        a scalar base type, or wraps a scalar base type.
        These will all be in the tagged_scalars directory.
    """

    _ctx = None

    # def __init_subclass__(cls, **kwargs) -> None:
    #     """
    #     Register any subclasses of this class in the SCALAR_NODE_CLASSES_BY_TAG
    #     and SCALAR_NODE_CLASSES_BY_KEY registry.
    #     """
    #     super().__init_subclass__(**kwargs)
    #     if cls.__name__ != "TaggedScalarNode":
    #         if cls._tag in SCALAR_NODE_CLASSES_BY_TAG:
    #             raise RuntimeError(f"TaggedScalarNode class for tag '{cls._tag}' has been defined twice")
    #         SCALAR_NODE_CLASSES_BY_TAG[cls._tag] = cls
    #         SCALAR_NODE_CLASSES_BY_KEY[name_from_tag_uri(cls._tag)] = cls

    @property
    def ctx(self):
        if self._ctx is None:
            TaggedScalarNode._ctx = asdf.AsdfFile()
        return self._ctx

    def __asdf_traverse__(self):
        return self

    # @property
    # def tag(self):
    #     return self._tag

    # @property
    # def key(self):
    #     return name_from_tag_uri(self._tag)

    # def get_schema(self):
    #     return get_schema_from_tag(self.ctx, self._tag)

    # def copy(self):
    #     return copy.copy(self)
