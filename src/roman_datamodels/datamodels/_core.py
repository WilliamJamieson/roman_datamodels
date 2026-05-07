"""
This module provides the same interface as the datamodels for JWST, so that they can be
    used in a common pipeline structure. Unlike the JWST datamodels, these models are
    backed by an ASDF file and the schema structure is defined by the ASDF schema.

This provides the abstract base class ``Datamodel`` for all the specific datamodels
    used for Roman. This dataclass is intended to be subclassed to form all of the actual
    working datamodels.
"""

from __future__ import annotations

import copy
import datetime
import functools
import sys
from abc import ABC
from collections.abc import Mapping, MutableMapping
from pathlib import Path, PurePath
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, ClassVar, Self

import asdf
import numpy as np
from asdf.exceptions import ValidationError
from asdf.tags.core.ndarray import NDArrayType
from asdf.util import uri_match
from astropy.table.meta import get_yaml_from_table
from astropy.time import Time

from roman_datamodels._stnode import DNode, TaggedObjectNode, get_default_tag, get_schema_uri

from ._utils import temporary_update_filedate, temporary_update_filename

if TYPE_CHECKING:
    from pyarrow import DataType

__all__ = ("DataModel", "ParquetSupport", "PipelineStep")


def _set_default_asdf(func):
    """
    Decorator which ensures that a DataModel has an asdf file available for use
    if required
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self._asdf is None:
            af = asdf.AsdfFile()
            af["roman"] = self._instance
            self._asdf = af

        return func(self, *args, **kwargs)

    return wrapper


class DataModel(ABC):
    """Base class for all top level datamodels"""

    crds_observatory: ClassVar[str] = "roman"
    tag_pattern: ClassVar[str]

    @classmethod
    def default_tag(cls) -> str:
        """Get the default tag for this class"""

        if (tag := get_default_tag(cls.tag_pattern)) is None:
            raise RuntimeError(f"No default tag found for pattern '{cls.tag_pattern}'")

        return tag

    def __new__(cls, init=None, **kwargs):
        """
        Handle the case where one passes in an already instantiated version
        of the model. In this case the constructor should just directly return
        the model.
        """
        if init.__class__.__name__ == cls.__name__:
            return init

        return super().__new__(cls)

    @classmethod
    def create_minimal(cls, defaults: Mapping[str, Any] | None = None, *, tag: str | None = None) -> Self:
        """
        Class method that constructs an "minimal" model.

        The "minimal" model will contain schema-required attributes
        where a default value can be determined:

            * node class defining a default value
            * defined in the schema (for example single item enums)
            * empty container classes (for example a "meta" dict)
            * required items with a corresponding provided default

        Parameters
        ----------
        defaults : None or dict
            If provided, defaults will be used in place of schema
            defined values for required attributes.

        tag: str or None
            If provided, specifically create a model using this tag not the
            default one.

        Returns
        -------
        DataModel
            "Empty" model with optional defaults. This will often
            be incomplete (invalid) as not all required attributes
            can be guessed.
        """
        return cls(
            TaggedObjectNode.create_minimal(
                tag=(tag or cls.default_tag()),
                defaults=defaults,
            )
        )

    @classmethod
    def create_fake_data(
        cls, defaults: Mapping[str, Any] | None = None, shape: tuple[int, ...] | None = None, *, tag: str | None = None
    ) -> Self:
        """
        Class method that constructs a model filled with fake data.

        Similar to `DataModel.create_minimal` this only creates
        required attributes.

        Fake arrays will have a number of dimensions matching
        the schema requirements. If shape is provided only the
        dimensions matching the schema requirements will be used.
        For example if a 3 dimensional shape is provided but a fake
        array only requires 2 dimensions only the first 2 values
        from shape will be used.

        Parameters
        ----------
        defaults : None or dict
            If provided, defaults will be used in place of schema
            defined or fake values for required attributes.

        shape : None or tuple of int
            When provided use this shape to determine the
            shape used to construct fake arrays.

        tag: str or None
            If provided, specifically create a model using this tag not the
            default one.

        Returns
        -------
        DataModel
            A valid model with fake data.
        """
        return cls(
            TaggedObjectNode.create_fake_data(
                tag=(tag or cls.default_tag()),
                defaults=defaults,
                shape=shape,
            )
        )

    __slots__ = ("_asdf", "_files_to_close", "_instance", "_iscopy", "_shape")

    @classmethod
    def create_from_model(cls, model: DataModel | DNode, *, tag: str | None = None) -> Self:
        """
        Create a new DataModel from an existing model.
        """
        return cls(
            TaggedObjectNode.create_from_node(
                tag=(tag or cls.default_tag()),
                node=(model._instance if isinstance(model, DataModel) else model),
            )
        )

    def migrate_tag(self, tag: str | None = None) -> Self:
        """
        Return a new version of this model with the tag updated.

        .. note::

            This may not fully update your model to the new tag, it only moves
            the information into the new tree. So it maybe missing information
            or have information of the wrong type. If you want a more complete
            migration to the new tag, use

                ``romancal.datamodels.migration.update_model_version``

            instead. This function begins with the result of this function and
            then apply migration steps that require the full pipeline to determine.

        Parameters
        ----------
        tag: str or None
            If provided, specifically update to this tag not the default (latest) one.

        Returns
        -------
        DataModel
            A new version of this model with the tag updated.
        """
        # If no tag is provided, then update to the default tag.
        tag = tag or self.default_tag()

        if self.tag == tag:
            return self

        return type(self).create_from_model(self, tag=tag)

    def __init__(self, init=None, **kwargs):
        if isinstance(init, self.__class__):
            # Due to __new__ above, this is already initialized.
            return

        self._iscopy = False
        self._shape = None
        self._instance = None
        self._asdf = None
        self._files_to_close = None

        if isinstance(init, TaggedObjectNode):
            if not uri_match(self.tag_pattern, init.tag):
                raise ValidationError(
                    f"The provided TaggedObjectNode's tag '{init.tag}' does not match the expected pattern '{self.tag_pattern}' for this model! "
                )

            self._instance = init
            af = asdf.AsdfFile()
            af["roman"] = self._instance
            self._asdf = af
            return

        if init is None:
            self._instance = TaggedObjectNode(read_tag=self.default_tag())

        elif isinstance(init, str | bytes | PurePath):
            if isinstance(init, PurePath):
                init = str(init)
            if isinstance(init, bytes):
                init = init.decode(sys.getfilesystemencoding())

            self._asdf = self.open_asdf(init, **kwargs)
            if not self.check_type(self._asdf):
                raise ValueError(f"ASDF file is not of the type expected. Expected {self.__class__.__name__}")

            self._instance = self._asdf.tree["roman"]
        elif isinstance(init, asdf.AsdfFile):
            self._asdf = init

            self._instance = self._asdf.tree["roman"]
        else:
            raise OSError("Argument does not appear to be an ASDF file or TaggedObjectNode.")

    def check_type(self, asdf_file):
        """
        Subclass is expected to check for proper type of node
        """
        from roman_datamodels import Manager

        if "roman" not in asdf_file.tree:
            raise ValueError('ASDF file does not have expected "roman" attribute')

        roman_branch = asdf_file.tree["roman"]
        if isinstance(roman_branch, TaggedObjectNode):
            return Manager().get_data_model(roman_branch.tag) is type(self)

    @property
    def schema_uri(self):
        return get_schema_uri(self._instance.tag)

    def close(self):
        if not (self._iscopy or self._asdf is None):
            self._asdf.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        """Ensure closure of resources when deleted."""
        self.close()

    def copy(self, deepcopy=True, memo=None):
        result = self.__class__(init=None)
        self.clone(result, self, deepcopy=deepcopy, memo=memo)
        return result

    __copy__ = copy

    def __deepcopy__(self, memo=None):
        return self.copy(deepcopy=True, memo=memo)

    @staticmethod
    def clone(target, source, deepcopy=False, memo=None):
        if deepcopy:
            target._asdf = source._asdf.copy()
            target._instance = copy.deepcopy(source._instance, memo=memo)
        else:
            target._asdf = source._asdf
            target._instance = source._instance

        target._iscopy = True
        target._files_to_close = []
        target._shape = source._shape

    def save(self, path, dir_path=None, *args, all_array_compression="lz4", all_array_storage="internal", **kwargs):
        path = Path(path(self.meta.filename) if callable(path) else path)
        output_path = Path(dir_path) / path.name if dir_path else path
        ext = path.suffix.decode(sys.getfilesystemencoding()) if isinstance(path.suffix, bytes) else path.suffix

        # TODO: Support gzip-compressed fits
        if ext == ".asdf":
            self.to_asdf(
                output_path, *args, all_array_compression=all_array_compression, all_array_storage=all_array_storage, **kwargs
            )
        elif ext == ".parquet" and hasattr(self, "to_parquet"):
            self.to_parquet(output_path)
        else:
            raise ValueError(f"unknown filetype {ext}")

        return output_path

    def open_asdf(self, init=None, **kwargs):
        from ._utils import _open_asdf

        if isinstance(init, str):
            return _open_asdf(init, **kwargs)

        return asdf.AsdfFile(init, **kwargs)

    def to_asdf(self, init, *args, all_array_compression="lz4", all_array_storage="internal", **kwargs):
        from ._utils import temporary_update_filedate, temporary_update_filename

        with (
            temporary_update_filename(self, Path(init).name),
            temporary_update_filedate(self, Time.now()),
        ):
            asdf_file = self.open_asdf(**kwargs)
            asdf_file["roman"] = self._instance
            asdf_file.write_to(
                init, *args, all_array_compression=all_array_compression, all_array_storage=all_array_storage, **kwargs
            )

    def get_primary_array_name(self):
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        return "data" if hasattr(self, "data") else ""

    @property
    def override_handle(self):
        """override_handle identifies in-memory models where a filepath
        would normally be used.
        """
        # Arbitrary choice to look something like crds://
        return f"override://{self.__class__.__name__}"

    @property
    def shape(self):
        if self._shape is None:
            primary_array_name = self.get_primary_array_name()
            if primary_array_name and hasattr(self, primary_array_name):
                primary_array = getattr(self, primary_array_name)
                self._shape = primary_array.shape
        return self._shape

    def __setattr__(self, attr, value):
        if attr.startswith("_") and attr in DataModel.__slots__:
            DataModel.__dict__[attr].__set__(self, value)
        else:
            setattr(self._instance, attr, value)

    def __getattr__(self, attr):
        return getattr(self._instance, attr)

    def __delattr__(self, attr):
        if attr.startswith("_") and attr in DataModel.__slots__:
            super().__delattr__(attr)
        else:
            delattr(self._instance, attr)

    def __setitem__(self, key, value):
        if key.startswith("_"):
            raise ValueError("May not specify attributes/keys that start with _")
        self._instance[key] = value

    def __getitem__(self, key):
        return self._instance[key]

    def __dir__(self):
        return set(super().__dir__()) | set(dir(self._instance))

    def __iter__(self):
        return iter(self._instance)

    def to_flat_dict(self, include_arrays=True):
        """
        Returns a dictionary of all of the model items as a flat dictionary.

        Each dictionary key is a dot-separated name.  For example, the
        model element ``meta.observation.date`` will end up in the
        dictionary as::

            { "meta.observation.date": "2012-04-22T03:22:05.432" }

        This differs from the JWST data model in that the schema is not
        directly used
        """

        def convert_val(val):
            if isinstance(val, datetime.datetime):
                return val.isoformat()
            elif isinstance(val, Time):
                return str(val)
            return val

        return {
            f"roman.{key}": convert_val(val)
            for (key, val) in self.items()
            if include_arrays or not isinstance(val, np.ndarray | NDArrayType)
        }

    def items(self):
        """
        Iterates over all of the model items in a flat way.

        Each element is a pair (``key``, ``value``).  Each ``key`` is a
        dot-separated name.  For example, the schema element
        ``meta.observation.date`` will end up in the result as::

            ("meta.observation.date": "2012-04-22T03:22:05.432")

        Unlike the JWST DataModel implementation, this does not use
        schemas directly.
        """

        yield from self._instance._recursive_items()

    def get_crds_parameters(self):
        """
        Get parameters used by CRDS to select references for this model.

        This will only return items under ``roman.meta``.

        Returns
        -------
        dict
        """
        return {
            f"roman.meta.{key}": val
            for key, val in self.meta.to_flat_dict(include_arrays=False, recursive=True).items()
            if isinstance(val, str | int | float | complex | bool)
        }

    @_set_default_asdf
    def validate(self):
        """
        Re-validate the model instance against the tags
        """
        self._asdf.validate()

    @_set_default_asdf
    def info(self, *args, **kwargs):
        return self._asdf.info(*args, **kwargs)

    @_set_default_asdf
    def search(self, *args, **kwargs):
        return self._asdf.search(*args, **kwargs)

    @_set_default_asdf
    def schema_info(self, *args, **kwargs):
        return self._asdf.schema_info(*args, **kwargs)


if TYPE_CHECKING:
    _DataModel = DataModel
else:
    _DataModel = object


class PipelineStep(_DataModel):
    """
    Mixin class for DataModels that are to be used as part of a pipeline step.

    Notes
    -----
        - Pipeline steps are all expected to have a ``model.meta.model_type``
            attribute which is set to the string name of the DataModel class in
            question. This class ensures this is set correctly as part of the
            __init__ for the DataModel.
        - Pipeline steps all have certain ``model.meta`` attributes which are
            expected to be set in certain ways, but it may not be clear from the
            schemas what the specific values for them are when creating a new
            model. These are set by ``_creator_defaults`` which is then used to
            update any defaults provided to the constructors. The defaults provided
            are:
                * calibration_software_name: "RomanCAL"
                * file_date: current time
                # TODO: Should we modify the origin schema in RAD to make this the first option?
                * origin: "STSCI/SOC"
    """

    __slots__ = ()

    def __init__(self, init=None, **kwargs):
        from roman_datamodels._stnode import TaggedStrNode

        super().__init__(init, **kwargs)

        if init is not None:
            current_model_type = self.get("meta", {}).get("model_type", None)
            # This is only necessary if we wish to support creating and writing
            #   RAD datamodels-1.4.0 and below
            match current_model_type:
                case TaggedStrNode():
                    self.meta.model_type = type(current_model_type).from_tag(
                        tag=current_model_type.tag,
                        node=type(self).__name__,
                    )

                case None:
                    self.meta.model_type = type(self).__name__

                case _:
                    self.meta.model_type = type(current_model_type)(type(self).__name__)

    @classmethod
    def _creator_defaults(
        cls, defaults: MutableMapping[str, Any] | None = None, *, time: Time | None = None
    ) -> MutableMapping[str, Any]:
        """
        The default values for the create constructors, `create_minimal` and `create_fake_data`.

        Parameters
        ----------
        defaults : None or dict
            If provided, defaults will be used in place of schema
        time: default time value


        Returns
        -------
        dict
            The default values to use when creating a new model. This will include
            some values that we want to always set to a specific value.
        """

        # TODO: Can this be simplified to using the | operator on dictionaries carefully?
        def merge_dicts(dict1: MutableMapping[str, Any], dict2: MutableMapping[str, Any]) -> MutableMapping[str, Any]:
            for key in dict2:
                if key in dict1:
                    dict1_is_mapping = isinstance(dict1[key], MutableMapping)
                    dict2_is_mapping = isinstance(dict2[key], MutableMapping)

                    if dict1_is_mapping and dict2_is_mapping:
                        dict1[key] = merge_dicts(dict1[key], dict2[key])

                    elif dict1_is_mapping ^ dict2_is_mapping:
                        raise ValueError("Cannot merge mapping with non-mapping")

                else:
                    dict1[key] = dict2[key]

            return dict1

        return merge_dicts(
            # deepcopy to avoid modifying input
            {} if defaults is None else copy.deepcopy(dict(defaults)),
            {
                "meta": {
                    "calibration_software_name": "RomanCAL",
                    "file_date": time or Time.now(),
                    "origin": "STSCI/SOC",
                }
            },
        )

    @classmethod
    def create_minimal(cls, defaults=None, *, tag=None):
        """
        Class method that constructs an "minimal" model.

        The "minimal" model will contain schema-required attributes
        where a default value can be determined:

            * node class defining a default value
            * defined in the schema (for example single item enums)
            * empty container classes (for example a "meta" dict)
            * required items with a corresponding provided default

        Parameters
        ----------
        defaults : None or dict
            If provided, defaults will be used in place of schema
            defined values for required attributes.

        Returns
        -------
        DataModel
            "Empty" model with optional defaults. This will often
            be incomplete (invalid) as not all required attributes
            can be guessed.
        """
        return super().create_minimal(defaults=cls._creator_defaults(defaults), tag=tag)

    @classmethod
    def create_fake_data(cls, defaults=None, shape=None, *, tag=None):
        """
        Class method that constructs a model filled with fake data.

        Similar to `DataModel.create_minimal` this only creates
        required attributes.

        Fake arrays will have a number of dimensions matching
        the schema requirements. If shape is provided only the
        dimensions matching the schema requirements will be used.
        For example if a 3 dimensional shape is provided but a fake
        array only requires 2 dimensions only the first 2 values
        from shape will be used.

        Parameters
        ----------
        defaults : None or dict
            If provided, defaults will be used in place of schema
            defined or fake values for required attributes.

        shape : None or tuple of int
            When provided use this shape to determine the
            shape used to construct fake arrays.

        Returns
        -------
        DataModel
            A valid model with fake data.
        """
        return super().create_fake_data(
            defaults=cls._creator_defaults(
                defaults,
                time=Time("2020-01-01T00:00:00.0", format="isot", scale="utc"),
            ),
            shape=shape,
            tag=tag,
        )


class ParquetSupport(_DataModel):
    """
    Mixin class for DataModels to enable writing to parquet files

    .. note::
        Only models with a source_catalog attribute are intended to support parquet.
        This can be mixed in with those models to provide parquet support.
    """

    __slots__ = ()
    # Mapping from the string name of a numpy dtype to the corresponding pyarrow type
    _dtype_map: ClassVar[MappingProxyType[str, DataType]]

    @classmethod
    def dtype_map(cls) -> MappingProxyType[str, DataType]:
        """
        Defer the construction of the dtype_map until it is actually needed. This
            is an entirely static method so it does not matter if we are thread
            safe or not, as we will always end up with the same dtype_map, it
            only may result in this being calculated more than once in a
            multithreaded context if we hit a particularly bad race condition.
        """
        import pyarrow as pa

        if not hasattr(cls, "_dtype_map"):
            cls._dtype_map = MappingProxyType(
                {
                    "bool": pa.bool_(),
                    "uint8": pa.uint8(),
                    "uint16": pa.uint16(),
                    "uint32": pa.uint32(),
                    "uint64": pa.uint64(),
                    "int8": pa.int8(),
                    "int16": pa.int16(),
                    "int32": pa.int32(),
                    "int64": pa.int64(),
                    "float16": pa.float16(),
                    "float32": pa.float32(),
                    "float64": pa.float64(),
                }
            )

        return cls._dtype_map

    def to_parquet(self, filepath):
        """
        Save catalog in parquet format.

        Defers import of parquet to minimize import overhead for all other models.
        """
        import pyarrow as pa
        import pyarrow.parquet as pq

        # parquet does not provide validation so validate first with asdf
        self.validate()

        with temporary_update_filename(self, Path(filepath).name), temporary_update_filedate(self, Time.now()):
            # Construct flat metadata dict
            flat_meta = self.to_flat_dict()

        # select only meta items
        flat_meta = {k: str(v) for (k, v) in flat_meta.items() if k.startswith("roman.meta")}

        # Extract table metadata
        source_cat = self.source_catalog
        scmeta = source_cat.meta

        # Wrap it as a DNode so it can be flattened
        dn_scmeta = DNode(scmeta)
        flat_scmeta = dn_scmeta.to_flat_dict(recursive=True)

        # Add prefix to flattened keys to indicate table metadata
        flat_scmeta = {"source_catalog." + k: str(v) for (k, v) in flat_scmeta.items()}

        # merge the two meta dicts
        flat_meta.update(flat_scmeta)

        # Turn numpy structured array into list of arrays
        keys = list(source_cat.columns.keys())
        arrs = [np.array(source_cat[key]) for key in keys]
        units = [str(source_cat[key].unit) for key in keys]
        dtypes = [self.dtype_map()[np.array(source_cat[key]).dtype.name] for key in keys]
        fields = [
            pa.field(key, type=dtype, metadata={"unit": unit}) for (key, dtype, unit) in zip(keys, dtypes, units, strict=False)
        ]

        # Turn the source catalog metadata into a yaml string and then attach it
        #   to the metadata for the parquet file.
        extra_astropy_metadata = get_yaml_from_table(source_cat)
        flat_meta["table_meta_yaml"] = "\n".join(extra_astropy_metadata)

        # Write the table to parquet
        schema = pa.schema(fields, metadata=flat_meta)
        table = pa.Table.from_arrays(arrs, schema=schema)
        pq.write_table(table, filepath, compression=None)
