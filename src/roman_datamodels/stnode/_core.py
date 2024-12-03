from abc import ABC, abstractmethod

import asdf

from ._base import DNode, LNode


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
    @classmethod
    @abstractmethod
    def asdf_schema_uri(clas) -> str:
        """URI of the schema that defines this node."""

    @property
    def schema_uri(self):
        return self.asdf_schema_uri()


class TagMixin(SchemaMixin, ABC):
    @classmethod
    @abstractmethod
    def asdf_ctx(self):
        """The ASDF file context."""

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


class ObjectNode(DNode, ABC):
    @classmethod
    @abstractmethod
    def asdf_required(cls) -> tuple[str]:
        """List of required fields in this node."""

    @property
    def required(self) -> tuple[str]:
        return self.asdf_required()


class SchemaObjectNode(ObjectNode, SchemaMixin, ABC): ...


class TaggedObjectNode(SchemaObjectNode, TagMixin, ABC): ...


class DataModelNode(TaggedObjectNode, ABC):
    @property
    @abstractmethod
    def array_shape(self) -> tuple[int]:
        """Shape of the data array."""


class TaggedListNode(LNode, TagMixin, ABC): ...


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

    @classmethod
    def asdf_ctx(cls):
        if cls._ctx is None:
            cls._ctx = asdf.AsdfFile()
        return cls._ctx

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
