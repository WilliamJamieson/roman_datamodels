from abc import ABC, abstractmethod

import asdf

from ._base import DNode, LNode

__all__ = [
    "DataModelNode",
    "ObjectNode",
    "SchemaObjectNode",
    "SchemaScalarNode",
    "TaggedListNode",
    "TaggedObjectNode",
    "TaggedScalarNode",
]


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


def class_name_from_uri(uri):
    """
    Compute the name of the schema from the uri.

    Parameters
    ----------
    uri : str
        The uri to find the name from
    """
    name = uri.split("/")[-1].split("-")[0]
    if "/tvac/" in uri and "tvac" not in name:
        name = "tvac_" + uri.split("/")[-1].split("-")[0]
    elif "/fps/" in uri and "fps" not in name:
        name = "fps_" + uri.split("/")[-1].split("-")[0]

    name = "".join([p.capitalize() for p in name.split("_")])

    if "reference_files" in uri:
        name += "Ref"

    return name


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


class ObjectNode(DNode, ABC):
    @classmethod
    def _object_nodes(cls):
        nodes = {}
        for node in cls.__subclasses__():
            sub_nodes = node._object_nodes()
            for name, sub_node in sub_nodes.items():
                if name in nodes and nodes[name] != sub_node:
                    raise RuntimeError(f"ObjectNode class '{node.__name__}' has conflicting sub-node '{name}'")

                nodes[name] = sub_node

            if node not in (ObjectNode, SchemaObjectNode, TaggedObjectNode, DataModelNode):
                nodes[node.__name__] = node

        return nodes

    @classmethod
    @abstractmethod
    def asdf_required(cls) -> tuple[str]:
        """List of required fields in this node."""

    @property
    def required(self) -> tuple[str]:
        return self.asdf_required()


class SchemaObjectNode(ObjectNode, SchemaMixin, ABC):
    @classmethod
    def _schema_object_nodes(cls):
        nodes = {}
        for node in cls.__subclasses__():
            sub_nodes = node._schema_object_nodes()
            for uri, sub_node in sub_nodes.items():
                if uri in nodes and nodes[uri] != sub_node:
                    raise RuntimeError(f"SchemaObjectNode class '{node.__name__}' has conflicting sub-node '{uri}'")
                nodes[uri] = sub_node

            try:
                uri = node.asdf_schema_uri()
            except KeyError:
                continue

            # Filter out the subclasses of schema nodes
            if node.__name__ == class_name_from_uri(uri):
                nodes[uri] = node

        return nodes


class TaggedObjectNode(SchemaObjectNode, TagMixin, ABC):
    @classmethod
    def _tagged_object_nodes(cls):
        nodes = {}
        for node in cls.__subclasses__():
            sub_nodes = node._tagged_object_nodes()
            for uri, sub_node in sub_nodes.items():
                if uri in nodes and nodes[uri] != sub_node:
                    raise RuntimeError(f"TaggedObjectNode class '{node.__name__}' has conflicting sub-node '{uri}'")
                nodes[uri] = sub_node

            # Filter out the abstract classes
            if uri := node.asdf_tag():
                # tagged node names should match with the tag uri
                if node.__name__ != class_name_from_uri(uri):
                    raise RuntimeError(f"TaggedObjectNode class '{node.__name__}' has incorrect tag '{uri}'")

                nodes[uri] = node

        return nodes


class DataModelNode(TaggedObjectNode, ABC):
    @classmethod
    def _data_model_nodes(cls):
        # Just start one level up so we don't capture the non-datamodels
        return cls._tagged_object_nodes()

    @property
    @abstractmethod
    def array_shape(self) -> tuple[int]:
        """Shape of the data array."""


class TaggedListNode(LNode, TagMixin, ABC):
    @classmethod
    def _tagged_list_nodes(cls):
        nodes = {}
        for node in cls.__subclasses__():
            sub_nodes = node._tagged_list_nodes()
            for uri, sub_node in sub_nodes.items():
                if uri in nodes and nodes[uri] != sub_node:
                    raise RuntimeError(f"TaggedObjectNode class '{node.__name__}' has conflicting sub-node '{uri}'")
                nodes[uri] = sub_node

            if uri := node.asdf_tag():
                # tagged node names should match with the tag uri
                if node.__name__ != class_name_from_uri(uri):
                    raise RuntimeError(f"TaggedObjectNode class '{node.__name__}' has incorrect tag '{uri}'")

                nodes[uri] = node

        return nodes


class SchemaScalarNode(SchemaMixin, ABC):
    @classmethod
    def _schema_scalar_nodes(cls):
        nodes = {}
        for node in cls.__subclasses__():
            sub_nodes = node._schema_scalar_nodes()
            for uri, sub_node in sub_nodes.items():
                if uri in nodes and nodes[uri] != sub_node:
                    raise RuntimeError(f"SchemaObjectNode class '{node.__name__}' has conflicting sub-node '{uri}'")
                nodes[uri] = sub_node

            try:
                uri = node.asdf_schema_uri()
            except KeyError:
                continue

            # These should not be subclassed
            if node.__name__ != class_name_from_uri(uri):
                raise RuntimeError(f"SchemaScalarNode class '{node.__name__}' should not be subclassed")

            nodes[uri] = node

        return nodes


class TaggedScalarNode(SchemaScalarNode, TagMixin, ABC):
    """
    Base class for all tagged scalars defined by RAD
        There will be one of these for any tagged object defined by RAD, which has
        a scalar base type, or wraps a scalar base type.
        These will all be in the tagged_scalars directory.
    """

    @classmethod
    def _tagged_scalar_nodes(cls):
        # Just start one level up so we don't capture the non-tagged scalars
        return cls._schema_scalar_nodes()

    def __asdf_traverse__(self):
        return self
