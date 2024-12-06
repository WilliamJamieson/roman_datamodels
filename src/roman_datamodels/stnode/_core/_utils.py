from typing import Any, TypeVar, get_args

import asdf

from .._typing import type_checked

T = TypeVar("T")

__all__ = [
    "camel_case_to_snake_case",
    "class_name_from_uri",
    "get_all_fields",
    "get_node_fields",
    "get_nodes",
    "get_nodes",
    "get_schema_from_tag",
    "get_schema_nodes",
    "get_tagged_nodes",
    "rad_field",
    "wrap_into_node",
]


class rad_field_property(property):
    """
    Special subclass of property to mark schema fields out
    """


def rad_field(function):
    """
    Create a special property decorator for nodes that enables testing
    of the type annotations for the for a schema field's property
    """
    return rad_field_property(type_checked(function))


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


def camel_case_to_snake_case(value):
    """
    Courtesy of https://stackoverflow.com/a/1176023
    """
    import re

    return re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower()


def _add_nodes(node: type, nodes: dict[str, type], sub_nodes: dict[str, type], base_cls: type) -> None:
    """
    Add the sub-nodes to the nodes dictionary.

    Parameters
    ----------
    node : type
        The node the sub-nodes are from.
    nodes : dict[str, type]
        The nodes to add to.
    sub_nodes : dict[str, type]
        The sub-nodes to add.
    base_cls : type
        The base class to start from.
    """
    for name, sub_node in sub_nodes.items():
        if name in nodes and nodes[name] != sub_node:
            raise RuntimeError(f"{base_cls.__name__} class '{node.__name__}' has conflicting sub-node '{name}'")

        nodes[name] = sub_node


def get_nodes(cls: type, filter_types: tuple[type]) -> dict[str, type]:
    """
    Get all the nodes from the class. Starting from the base class.

    Parameters
    ----------
    cls : type
        The class to get the nodes from.
    filter_types : tuple[type]
        The types to filter out.

    Returns
    -------
    dict[str, type]
        class_name -> class mapping
    """

    def _get_nodes(cls: type, base_cls: type, filter_types: tuple[type]) -> dict[str, type]:
        nodes = {}
        for node in cls.__subclasses__():
            _add_nodes(node, nodes, _get_nodes(node, base_cls, filter_types), base_cls)

            if node not in filter_types:
                nodes[node.__name__] = node

        return nodes

    return _get_nodes(cls, cls, filter_types)


def get_schema_nodes(cls: type, no_subcls: bool) -> dict[str, type]:
    """
    Get all the schema nodes from the class. Starting from the base class.

    Parameters
    ----------
    cls : type
        The class to get the schema nodes from.
    no_subcls : bool
        If True, raise an error if the class is subclassed.

    Returns
    -------
    dict[str, type]
        schema_uri -> class mapping
    """

    def _get_schema_nodes(cls: type, base_cls: type, no_subcls: bool) -> dict[str, type]:
        nodes = {}
        for node in cls.__subclasses__():
            _add_nodes(node, nodes, _get_schema_nodes(node, base_cls, no_subcls), base_cls)

            try:
                uri = node.asdf_schema_uri()
            except KeyError:
                continue

            if node.__name__ == class_name_from_uri(uri):
                nodes[uri] = node
                continue

            if no_subcls:
                raise RuntimeError(f"{base_cls.__name__} class '{node.__name__}' should not be subclassed")

        return nodes

    return _get_schema_nodes(cls, cls, no_subcls)


def get_tagged_nodes(cls: type) -> dict[str, type]:
    """
    Get all the tagged nodes from the class. Starting from the base class.

    Parameters
    ----------
    cls : type
        The class to get the tagged nodes from.
    base_cls : type
        The base class to start from.

    Returns
    -------
    dict[str, type]
        tag_uri -> class mapping
    """

    def _get_tagged_nodes(cls: type, base_cls: type) -> dict[str, type]:
        nodes = {}
        for node in cls.__subclasses__():
            _add_nodes(node, nodes, _get_tagged_nodes(node, base_cls), base_cls)

            # Filter out the abstract classes
            if uri := node.asdf_tag():
                # tagged node names should match with the tag uri
                if node.__name__ != class_name_from_uri(uri):
                    raise RuntimeError(f"{base_cls.__name__} class '{node.__name__}' has incorrect tag '{uri}'")

                nodes[uri] = node

        return nodes

    return _get_tagged_nodes(cls, cls)


def get_all_fields(cls: type) -> set[str]:
    """
    Get all the fields from the class.

    Parameters
    ----------
    cls : type
        The class to get the fields from.

    Returns
    -------
    set[str]
        The fields of the class.
    """

    return {property_name for property_name in dir(cls) if isinstance(getattr(cls, property_name), property)}


def _get_mixin_fields(cls: type) -> set[str]:
    """
    Get all the mixin fields from the class.

    Parameters
    ----------
    cls : type
        The class to get the mixin fields from.

    Returns
    -------
    set[str]
        The mixin fields of the class.
    """
    from .._base import AdditionalNodeMixin

    mixin_fields = set()
    if issubclass(cls, AdditionalNodeMixin):
        for base in cls.__bases__:
            if issubclass(base, AdditionalNodeMixin):
                if base is AdditionalNodeMixin:
                    # This means that cls is the actual mixin class
                    new_fields = get_all_fields(cls)
                else:
                    # This means cls is a child of the class with the mixin
                    new_fields = _get_mixin_fields(base)
                mixin_fields.update(new_fields)
    return mixin_fields


def get_node_fields(cls: type) -> tuple[str]:
    """
    Get all the node fields from the class.
        This excludes the reserved fields and mixin fields.

    Parameters
    ----------
    cls : type
        The class to get the node fields from.

    Returns
    -------
    tuple[str]
        The node fields of the class.
    """
    from .._registry import RDM_NODE_REGISTRY

    return tuple(
        property_name
        for property_name in get_all_fields(cls)
        if (
            property_name not in (*RDM_NODE_REGISTRY.reserved_fields, *_get_mixin_fields(cls))
            and not property_name.startswith("_")
        )
    )


def wrap_into_node(value: Any, signature: T) -> T:
    """
    Wrap things into node containers if necessary.

    Parameters
    ----------
    value : Any
        The value to coerce.
    signature : T
        A type annotation

    Returns
    -------
    T
        Value wrapped into the node container if T describes a node container.
    """
    from .._base import DNode, LNode
    from ._scalar import SchemaScalarNode

    args = get_args(signature)

    # This is a true type
    # -> signature is the type
    if not args:
        # Only coerce nodes
        if issubclass(signature, DNode) or issubclass(signature, LNode) or issubclass(signature, SchemaScalarNode):
            # Skip if we are already the correct type
            if not isinstance(value, signature):
                return signature(value)

    # This is a annotated type
    if args:
        # These will always be a tuple (type, metadata)
        container, metadata = args

        # Handle DNodes
        if container is DNode:
            # Skip if we are already a DNode
            if not isinstance(value, DNode):
                # DNodes are hinted as dictionaries, so 2 metadata entries, (key, entry)
                _, entry = metadata

                # Coerce the dictionary entries if necessary
                return DNode({key: wrap_into_node(sub_val, entry) for key, sub_val in value.items()})

        # handle LNodes
        if container is LNode:
            if not isinstance(value, LNode):
                # LNodes are hinted as lists, so 1 metadata entry, entry
                # Coerce the list entries to the correct type
                return LNode([wrap_into_node(sub_val, metadata) for sub_val in value])

        return wrap_into_node(value, container)

    return value
