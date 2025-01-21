"""
This module contains the utility functions for the datamodels sub-package. Mainly
    the open/factory function for creating datamodels
"""

import warnings
from collections.abc import Mapping
from os import PathLike
from pathlib import Path
from typing import Any, TypeVar

import asdf

from roman_datamodels import validate

# from ._core import MODEL_REGISTRY, DataModel
from ._core import DataModel

__all__ = ["FilenameMismatchWarning", "rdm_open"]

_T = TypeVar("_T")


class FilenameMismatchWarning(UserWarning):
    """
    Warning when the filename in the meta attribute does not match the filename
    of the file being opened.
    """


def _open_path_like(init: PathLike[str] | str, lazy_tree: bool = True, **kwargs: Any) -> asdf.AsdfFile:
    """
    Attempt to open init as if it was a path-like object.

    Parameters
    ----------
    init
        Any path-like object that can be opened by asdf such as a valid string
    lazy_tree: bool
        If we should open the file with memmap
    **kwargs:
        Any additional arguments to pass to asdf.open
    """
    # asdf defaults to lazy_tree=False, this overwrites it to
    # lazy_tree=True for roman_datamodels
    kwargs["lazy_tree"] = lazy_tree
    init = Path(init)

    asdf_file: asdf.AsdfFile

    try:
        asdf_file = asdf.open(init, **kwargs)  # type: ignore[no-untyped-call]
    except ValueError as err:
        raise TypeError("Open requires a filepath, file-like object, or Roman datamodel") from err

    if (
        "roman" in asdf_file
        and isinstance(asdf_file["roman"], Mapping)  # Fix issue for Python 3.10
        and "meta" in asdf_file["roman"]
        and "filename" in asdf_file["roman"]["meta"]
        and asdf_file["roman"]["meta"]["filename"] != init.name
    ):
        warnings.warn(
            f"meta.filename: {asdf_file['roman']['meta']['filename']} does not match filename: {init.name}, updating the filename in memory!",
            FilenameMismatchWarning,
            stacklevel=2,
        )
        asdf_file["roman"]["meta"]["filename"] = init.name

    return asdf_file


def rdm_open(init: str | Path | DataModel[_T] | asdf.AsdfFile, memmap: bool = False, **kwargs: Any) -> DataModel[_T]:
    """
    Datamodel open/create function.
        This function opens a Roman datamodel from an asdf file or generates
        the datamodel from an existing one.

    Parameters
    ----------
    init
        May be any one of the following types:
            - `asdf.AsdfFile` instance
            - string indicating the path to an ASDF file
            - `DataModel` Roman data model instance
    memmap
        Open ASDF file binary data using memmap (default: False)

    Returns
    -------
    `DataModel`
    """
    from roman_datamodels.stnode import RDM_NODE_REGISTRY

    if isinstance(init, str | Path):
        if Path(init).suffix.lower() == ".json":
            try:
                from romancal.datamodels.library import ModelLibrary

                # Romancal is being totally skipped by MyPy
                return ModelLibrary(init)  # type: ignore[no-any-return]
            except ImportError as err:
                raise ImportError("Please install romancal to allow opening associations with roman_datamodels") from err
    with validate.nuke_validation():
        if isinstance(init, DataModel):
            # Copy the object so it knows not to close here
            return init.copy(deepcopy=False)

        # Temp fix to catch JWST args before being passed to asdf open
        if "asn_n_members" in kwargs:
            del kwargs["asn_n_members"]

        asdf_file = init if isinstance(init, asdf.AsdfFile) else _open_path_like(init, memmap=memmap, **kwargs)
        if (model_type := type(asdf_file.tree["roman"])) in RDM_NODE_REGISTRY.node_datamodel_mapping:
            # MyPy cannot statically determine that the return type will be a DataModel
            return RDM_NODE_REGISTRY.node_datamodel_mapping[model_type](asdf_file, **kwargs)  # type: ignore[no-any-return, index]

        # Check if the datamodel is a GDPS datamodel
        try:
            import roman_gdps  # noqa: F401
        except ImportError as err:
            # ASDF has not implemented type so MyPy will complain about this
            # until they do.
            asdf_file.close()  # type: ignore[no-untyped-call]
            raise ImportError("Please install roman-gdps to allow opening GDPS datamodels") from err

        # We assume at this point that an asdf file with `roman` key is a GDPS datamodel
        if "roman" in asdf_file.tree:
            # MyPy is not indexing into roman_gpds so it will complain about this being Any
            return asdf_file.tree["roman"]  # type: ignore[no-any-return]

        # ASDF has not implemented type so MyPy will complain about this
        # until they do.
        asdf_file.close()  # type: ignore[no-untyped-call]
        raise TypeError(f"Unknown datamodel type: {model_type}")
