Stnode Functionality
====================

As seen throughout :ref:`using-datamodels`, "node" objects are used to actually
handle and store the data for a datamodel. Indeed, if one opens an ASDF file
with a roman datamodel directly with `asdf.open` instead of
`roman_datamodels.datamodels.open`, the resulting object stored under the
``roman`` attribute will be a `~roman_datamodels.stnode.DNode` object or sublclass
there of rather than a `~roman_datamodels.datamodels.DataModel` object. Thus the
stnode, "node" objects form the data storage and manipulation backbone of the
roman datamodels.

Data Nodes
----------

The stnode, "node" objects are all directly implemented in code as as part of the
``roman_datamodels.nodes`` module. This module contains nodes corresponding to all
the schemas and sub-structure objects defined within ``rad``.

.. note::

    Originally, the node objects were dynamically generated from the schema files
    as subclasses of `~roman_datamodels.stnode.DNode` or `~roman_datamodels.stnode.LNode`.
    However, due to the necessity of being able to create and work with the nodes
    bespoke utility functions were necessary to (partially or completely) fill out
    the data within the node so that the node was valid enough to be read or written
    by ASDF.

    Ultimately, this became equivalent to writing the node objects explicitly with
    python code, but without the advantages of having a static reference to develop
    against.

As part of the testing suite for ``roman_datamodels``, the schema files and the
Python code are closely compared against each other to ensure that the Python code
matches the state of the schema files. This does mean that the explicit Python objects
only really match the latest manifest version of ``rad`` that ``roman_datamodels``
was "built" against. This however does not mean that the node objects cannot handle
data older versions of ``rad`` schema files, instead it just means that the node's
explicitly defined attributes will not necessary match those in the older schema files.
The struncture of the `~roman_datamodels.stnode.DNode` and `~roman_datamodels.stnode.LNode`
objects is sufficient to easily handle this (link to DNode discussion here), but any
completion engines, IDEs, or direct examination of the node object code many not give
a clear or accurate picture of the data therein. Thus in these cases it is important
to refer to the older versions of ``rad``.


Core Node Types
***************

There are two core container node types `~roman_datamodels.stnode.DNode` and
`~roman_datamodels.stnode.LNode` which correspond to "dictionary" and
"list"-like data structures, respectively. As we will see, all the specific
stnode objects construct from a schema file will be built off these two classes.
Hence, general functionality of an stnode object should be implemented in these
two classes so that all stnode objects can inherit from them.

DNode
#####

The `~roman_datamodels.stnode.DNode` is the primary building block of the nodes
in ``roman_datamodels``. This is because most of the schemas in ``rad`` are based
around the ``type: object``, meaning they follow the form of a dictionary with
a specific set of keys. Note that in general for the ``rad`` schemas, the
``additionalProperties: true`` modifier for the object type is used, meaning that
in the corrispondinging node object, we must be able to support any sort of string
key in addition to the keys defined in the schema.

To support this "dictionary-like" behavior, the `~roman_datamodels.stnode.DNode`
object follows the `collections.abc.MutableMapping` protocol. This means that for
the most part `~roman_datamodels.stnode.DNode` based objects can interacted with
as if they were a dictionary. That is ``node["keyword"]`` can be used to access
the information stored under the keyword ``"keyword"`` in the node object.

While this is great as an initial interface and allows for easy interaction with
the `~roman_datamodels.stnode.DNode` based object's stored data. It is not very
Pythonic in the cases that one wants to access and work with a single data entry
in the node object. To address this, the `~roman_datamodels.stnode.DNode` object
implements a modification of the ``__getattr__`` method to allow for direct "dot"
(``.``) access to the data stored in the node object. For example the data stored
under the keyword ``"keyword"`` can be accessed via ``node.keyword``. Similarly,
there is a matching modification of the ``__setattr__`` method to allow for for
the setting of the data stored in the node object via the ``.`` operator; that is
``node.keyword = value``.

.. note::

    For data fields that are not defined in the ``rad`` schema corresponding to
    the node object, they cannot be initially set via the ``.`` operator. Meaning
    that if ``keyword`` is not a defined keyword under the ``properties:`` section
    of the ``rad`` schema, then ``node.keyword = value`` will raise an error. In
    this case the data can still be set via the ``[]`` operator using
    ``node["keyword"] = value``. Once this has occurred, then the data can be accessed
    and set via the ``.`` operator unless the data is removed using ``del node["keyword"]``.

Data Fields
^^^^^^^^^^^

In general, writing a node to an ASDF file requires that the data within that node
being able pass the matching ``rad`` schema for that node. Moreover, the ``rad``
schemas are developed for the end products, meaning that all the data that is expected
in the final products is detailed and required by the schema. This can pose awkward
issues, when running ``romancal`` as often not all data is flushed out in the node
by the end of the step, but will be filled in by subsequent steps. This is because
we need to be able to write a given datamodel to disk after any step in the pipeline.
To address this issue, some mechanism needs to be in place to fill in these missing
fields with dummy data so that the node can be written to disk.

This leads to the concept of "data fields" (or "fields" to be short). These are
the keyword entries under the ``properties:`` section of the ``rad`` schema, and
is these pieces of data which we are trying to fill in. The
`~roman_datamodels.stnode.field` `descriptor <https://docs.python.org/3/howto/descriptor.html>`_
forms the solution to this issue. Effectively, the ``~roman_datamodels.stnode.field``
is acting like the builtin `property` descriptor except that it modifies the behavior
of the ``getter`` function that is typically passed to `property`.

For `~roman_datamodels.stnode.field`, the ``getter`` function is used as the default
value generator function for the field. This means that when accessed, the `~roman_datamodels.stnode.field`
descriptor will first try to find the data in the node object itself; however, if the
data is not found, the ``getter`` function will then be called to generate and set the
default value for the field in the node before returning the value. This allows the
node object to be lazy about the data it contains, only filling in data when accessed
or set by the user, not when the node instance is created. For example

.. code:: python

    from roman_datamodels.stnode import core, rad

    class DummyNode(core.DNode):

        @rad.field
        def my_field(self) -> int:
            return 42

Represents a node object that has been created with a single field ``my_field``,
which is an integer with a default value of 42.

.. note::

    The `~roman_datamodels.stnode.field` descriptor is a specialized subclass of
    the builtin `property` descriptor, so aside from the modification of how the
    value get is handled, the `~roman_datamodels.stnode.field` descriptor behaves
    just like a normal `property`.

.. note::

    The introduction of the `~roman_datamodels.stnode.field` accomplishes another
    distinct goal aside from providing a mechanism to fill in missing data. It
    also statically (in Python code) defines the data fields that one normally
    can expect to find in a given node object. Indeed, it has been carefully
    annotated so that IDE completion engines will be able to provide useful completions.
    For example if a field's data is that of another field, the engine will be able
    to recognize this fact and provide completions for what data fields the user
    expects to find in the node object.

    Moreover, when cupled to the rest of `~roman_datamodels.stnode` objects, the
    `~roman_datamodels.stnode.field` also performs some lazy documentation generation
    wherein it will find the ``title`` and ``description`` keywords for that field
    in the corresponding ``rad`` schema and add those into an documentation included
    in the node object. This will only occur if the documentation ``__doc__`` string
    is accessed. This means things like ``help(node_type.field_name)`` and related
    will provide useful information about the field when the user is working interactively
    with a node.

.. warning::

    The fields for given node object will only match those defined in the version
    of ``rad`` which the node object was created against. This means that the
    nodes can only perform their automatic data filling for writing ASDF files
    for that particular version of ``rad``. Moreover, the fields and documentation
    can only match the version ``rad`` that was built against. This means that
    opening earlier or later versions of datamodels may result in situations where
    the fields and documentation are unreliable or incorrect. Indeed, the node
    will issue a warning that the there is a version difference in these cases.

    The nodes themselves are designed to be able to handle, modify, and write
    ASDF files in this case, but they will not be able to assist the user in a
    meaniful way (such as filling in values). In these cases, the node will not
    even try to flush out data fields.

LNode
#####

`~roman_datamodels.stnode.LNode` is the list-like node object. This object is used
to provide an interface for the ``type: array`` schemas in ``rad``. This "type" in
JSON schema is defines something akin to a Python list. In our case we are interpreting
it as a list of objects, so a base node class is needed to wrap these. Moreover,
these provide a convenience wrapper around the Python list object to provide a uniform
interface among the different node objects.

Similar to the `~roman_datamodels.stnode.DNode` object, the `~roman_datamodels.stnode.LNode`
object follows the `collections.abc.MutableSequence` protocol, indeed it is a subclass
of `collections.UserList`. This means that all the common methods for a Python `list`
object are available for the `~roman_datamodels.stnode.LNode` object. In particular,
accessing data stored in `~roman_datamodels.stnode.LNode` object is done via the ``[]``
operator, e.g. ``node[0]``.

RAD Node Types
**************

In order to tightly integrate with both ASDF and the ``rad`` schemas, `~roman_datamodels.stnode`
provides some higher level node objects which are subclasses of `~roman_datamodels.stnode.DNode`
or `~roman_datamodels.stnode.LNode`. The nodes that form the base classes for ``roman_datamodels.nodes``
objects all subclass specialized versions of these classes, namely:

    1. `~roman_datamodels.stnode.ObjectNode`, which extends `~roman_datamodels.stnode.DNode` with
       additional that assist in handling the data in the node object and linking it with the ``rad``
       schemas in-particular the ASDF handling for the data.
    2. `~roman_datamodels.stnode.ListNode`, which simply subclasses `~roman_datamodels.stnode.LNode`
       in order to provide a uniform descriptive interface like the `~roman_datamodels.stnode.ObjectNode`;
       note that this class does not add additional functionality to the `~roman_datamodels.stnode.LNode`,
       but could be used to add additional functionality if needed.
    3. `~roman_datamodels.stnode.ScalarNode`, which integrates in the ASDF handling features for the
       scalar data types.

These classes are then mixed with

    1. `~roman_datamodels.stnode.SchemaMixin`
    2. `~roman_datamodels.stnode.TagMixin`

To provide the necessary functionality to define all the core objects described by the ``rad`` schemas.
There are also some additional mixins that can be used to add additional functionality or descriptions
to the node objects, which will be discussed in more detail below.

.. note::

    These are all abstract classes meaning that the node implementation must define the necessary methods
    in order to be used.

Schema Nodes
############

All schemas in ``rad`` have a corresponding "schema" node present in ``roman_datamodels.nodes``, which
fall into the object, list, or scalar categories. These categories correspond to the following node types:

    1. `~roman_datamodels.stnode.SchemaObjectNode`,
    2. `~roman_datamodels.stnode.SchemaListNode`,
    3. `~roman_datamodels.stnode.SchemaScalarNode`.

All of which are simply mixes of the `~roman_datamodels.stnode.SchemaMixin` with the appropriate base
node.

.. note::

    Technically, tagged schemas do not fall into this category, instead they will be handled with
    the `~roman_datamodels.stnode.TagMixin`; however, that inherits from the `~roman_datamodels.stnode.SchemaMixin`.
    It however, implements some of the interface required by `~roman_datamodels.stnode.SchemaMixin` through
    the tag mechanisms. So broadly speaking, the tagged schemas and the schema nodes have the same general interface.

    All of this is to say that the direct schema node subclasses in ``roman_datamodels.nodes`` represent all the
    ``type: object`` schemas in the ``rad`` schemas which are not tagged.

To create a new schema node one simply needs to define the ``_asdf_schema_uris`` method in your class and then add your
fields using the ``~roman_datamodels.stnode.field`` descriptor as a decorator. For example:

.. code:: python

    class MySchemaNode(core.SchemaObjectNode):

        @classmethod
        def _asdf_schema_uris(cls) -> tuple[str, ...]:
            return ("asdf://stsci.edu/datamodels/roman/schemas/path_to_my_schema_uri",)

        @rad.field
        def my_field(self) -> int:
            return 42

.. note::

    The ``_asdf_schema_uris`` is used by the ``.asdf_schema_uris`` "class-property". For some reason,
    the `~abc.abstractmethod` decorator causes very strange behavior when combined with
    the `~roman_datamodels.stnode.classproperty` descriptor. Thus, the hidden method is used in the
    code base to define the value, but it should not be used outside of the defining class. Use the
    ``.asdf_schema_uris`` class-property instead.

.. note::

    Notice that ``_asdf_schema_uris`` is returning a tuple of strings. This is so that in the future
    multiple schema versions (and their URIs) can be represented by this single node object, rather
    than having to have multiple node objects for each schema version.

.. warning::

    The last URI in the ``_asdf_schema_uris`` tuple is considered to be the default/current schema
    for a node unless it is otherwise indicated when creating an instance. This means that new
    schema versions should be added to the end of the tuple.

    The ``-*`` version suffix for the schema URIs is not supported. This is so that the URIs are
    totally explicit and can be used to search for the schema files in the ``rad`` schemas directly.
    Moreover, this makes sure that specialized classes for a given URI can be supported as needed.

Tag Nodes
#########

In a similar vein to the schema nodes, all "tagged" (with respect to having a defined tag in the ``rad``
schemas manifest) schemas in ``rad`` have a corresponding "tagged node" object in ``roman_datamodels.nodes``.
Similarly to the schema nodes, these are

    1. `~roman_datamodels.stnode.TaggedObjectNode`,
    2. `~roman_datamodels.stnode.TaggedListNode`,
    3. `~roman_datamodels.stnode.TaggedScalarNode`.

All of which are simply mixes of the `~roman_datamodels.stnode.TagMixin` with the appropriate base.

Currently, these two objects are implemented so that they follow the
dictionary or list interface; meaning that, they can be accessed via the ``[]``
operator (``node["keyword"]`` or ``node[0]``). However, for the case of the
`~roman_datamodels.stnode.DNode` objects, keys can also be used to directly
access the data attributes of the object via the Python ``.`` operator
(``node.keyword``). This is so that the `~roman_datamodels.stnode.DNode`
objects "look" like they are nice Python derived types.

.. warning::

    Because the `~roman_datamodels.stnode.DNode` "attributes" are actually like
    Python dictionary keys, using the ``__getattr__`` to enable ``.``
    access, things like ``dir(node)``, IDE autocompletion, and some other Python
    introspection tools will not work as expected. In some cases this may result
    in spurious warnings about accessing undefined attributes. It also means
    that one should be referencing the schema files to understand what
    attributes are available for a given stnode object.

    This information can be found using the ``.info()`` method. This method will
    be a pass through to the `asdf.AsdfFile.info` method.


Dynamic Node Construction
*************************

A specialized "node" class, that is a node class with a specific name which maps
to a corresponding schema name, will be created and registered by
`~roman_datamodels.stnode` when the module is first imported. The schemas which
get this treatment are the "tagged" schemas defined within the ``datamodels-*``
manifest in the RAD package. Any "un-tagged" schemas in RAD will not have a
corresponding stnode object. Instead, the information they contain will be
stored in a `~roman_datamodels.stnode.DNode` or `~roman_datamodels.stnode.LNode`
object, depending on the schema in question.

.. note::

    The creation of stnode "node" types might occur when a user opens an ASDF
    file containing Roman data, as ASDF will load stnode as part of its
    de-serialization process. However, due to how Python imports work this
    should only happen once.

The specific stnode objects will be subclasses of the
`~roman_datamodels.stnode.TaggedObjectNode` or
`~roman_datamodels.stnode.TaggedListNode` classes. These classes are extensions
of the `~roman_datamodels.stnode.DNode` and `~roman_datamodels.stnode.LNode`
classes which have extensions to handle looking up the schema information.
In particular, they will track the ``tag`` information
contained within the manifest from RAD.

These "tagged-nodes" are then turned into specific stnode objects via the
factories in `roman_datamodels.stnode._factories`. The way these factories work
is they process the ``tag`` value and strip out the unique name for the schema,
which gets turned into a name for the type that the factory will create.

.. note::

    If special methods are needed for a specific stnode object, then one needs
    to add class to `roman_datamodels.stnode._mixins` with the appropriate
    methods/properties under the name ``<expected-class-name>Mixin``. The
    factories will automatically pick up these mixins and mix them into the
    stnode object correctly when it is created.

These factories are looped over and invoked by the
`roman_datamodels.stnode._stnode` module which will be imported whenever
`roman_datamodels.stnode` is imported which will generate the stnode objects and
register them during that import. Note that this module is imported as part of
the `roman_datamodels.datamodels` module.


Scalar Nodes
************

In addition to the objects described above, there are the "scalar node"
objects, which are created from multiple inheritance of
`~roman_datamodels.stnode.TaggedScalarNode` and a scalar type. These objects are
used to represent the schemas under the ``tagged_scalars`` directory in RAD.
Those schemas are used to decorate a few common scalar ``meta`` fields with
additional information for the archive and sdp. Due to how the ``meta`` keyword
is assembled (via multiple combiners), ASDF has a hard time traversing the
schemas to look for this information. Thus, these scalar nodes are tagged so that
ASDF has a hook to find them without trying a recursive search of the schema
files. If this issue is resolved in the future, or the metadata under ``meta``
is reorganized, then scalar node concept can be removed from the codebase.

.. note::
    The scalar nodes determine the type they mix together with
    `~roman_datamodels.stnode.TaggedScalarNode` via, the ``SCALAR_TYPE``
    constant dictionary defined in `roman_datamodels.stnode._factories`. This
    dictionary keys off the ``type`` keyword that all schemas have to define. If
    a new type needs to be added, then one needs to add a new entry to this
    dictionary.


ASDF
----

The stnode objects are designed to be serializable to and from ASDF files. As
noted above, the stnode objects wrapped by the
`~roman_datamodels.datamodels.DataModel` are the actual objects which are
serialized to ASDF not the `~roman_datamodels.datamodels.DataModel` object
itself.

``roman_datamodels`` provides a custom ASDF extension so that ASDF can handle
the stnode objects. This extension does not include the schemas used to build
the stnode objects, as the schemas are already included in extension provided by
the RAD package. The ASDF extension itself is defined in the
`roman_datamodels.stnode._converters` module. As part of this module, the
serialization and de-serialization logic is defined in the "converters" for each
of the three "tagged" object base classes. The extension is then integrated into
ASDF by the `roman_datamodels.stnode._integration` module, as this module allows
the ASDF extension to be registered with ASDF without having to always import
``roman_datamodels`` whether or not it is used for a particular case. This is
a recommendation from ASDF so that the extension will have minimal impact on the
general ASDF performance for a given user.
