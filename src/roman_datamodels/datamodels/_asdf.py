import sys
from collections.abc import Callable
from contextlib import contextmanager
from os import PathLike
from pathlib import Path

from asdf import AsdfFile

from roman_datamodels.validate import nuke_validation

__all__ = ["AsdfFileMixin"]


@contextmanager
def _temporary_update_filename(datamodel, filename):
    """
    Context manager to temporarily update the filename of a datamodel so that it
    can be saved with that new file name without changing the current model's filename
    """
    from roman_datamodels.nodes import Filename

    if "meta" in datamodel.fields and "filename" in datamodel.meta.fields:
        old_filename = datamodel.meta.filename
        datamodel.meta.filename = Filename(filename)

        yield
        datamodel.meta.filename = old_filename
        return

    yield
    return


class AsdfFileMixin:
    _is_copy: bool = False
    _asdf: AsdfFile | None = None

    @classmethod
    def node_type(cls) -> type:
        """
        Get the top-level node type for this model
        -> this is assumed to be the last class in the multiple inheritance
        """
        return cls.__bases__[-1]

    def _init_asdf_file(self) -> None:
        """
        Initialize the ASDF file
        """
        with nuke_validation():
            af = AsdfFile()
            af["roman"] = self.node_type()(self._data)
            af.validate()
            self._asdf = af

    @property
    def _asdf_file(self) -> AsdfFile:
        """Access the ASDF file"""
        if self._asdf is None:
            self._init_asdf_file()

        return self._asdf

    def _check_type(self, asdf_file: AsdfFile) -> bool:
        """
        Check that the asdf_file is the proper type of node for the datamodel
        """
        if "roman" not in asdf_file.tree:
            raise ValueError('ASDF file does not have expected "roman" attribute')

        return type(asdf_file.tree["roman"]) is self.node_type()

    def close(self) -> None:
        """Close the associated ASDF file if it can be"""
        if not self._is_copy and self._asdf is not None:
            self._asdf.close()

    def open_asdf(self, init: PathLike | None = None, **kwargs) -> AsdfFile:
        """
        Attempt to open the ASDF path

        Parameters
        ----------
        init : PathLike
            Path to the ASDF file
        **kwargs:
            Arguments to asdf open

        Returns
        -------
        The opened ASDF file
        """
        from ._utils import _open_path_like

        with nuke_validation():
            if isinstance(init, str):
                return _open_path_like(init, **kwargs)

            return AsdfFile(init, **kwargs)

    def to_asdf(self, init: PathLike, *args, **kwargs) -> None:
        """
        Write to the ASDF File

        Parameters
        ----------
        init : PathLike
            Path to the ASDF file
        *args:
            Arguments to asdf write_to
        **kwargs:
            Keyword arguments to asdf open and asdf write_to
        """
        all_array_compression = kwargs.pop("all_array_compression", "lz4")

        with nuke_validation(), _temporary_update_filename(self, Path(init).name):
            asdf_file = self.open_asdf(**kwargs)
            asdf_file["roman"] = self.node_type()(self._data)
            asdf_file.write_to(init, *args, all_array_compression=all_array_compression, **kwargs)

    def save(self, path: PathLike | Callable[[PathLike], PathLike], dir_path: PathLike | None = None, *args, **kwargs) -> None:
        path = Path(path(self.meta.filename) if callable(path) else path)
        output_path = Path(dir_path) / path.name if dir_path else path
        ext = path.suffix.decode(sys.getfilesystemencoding()) if isinstance(path.suffix, bytes) else path.suffix

        # TODO: Support gzip-compressed fits
        if ext == ".asdf":
            self.to_asdf(output_path, *args, **kwargs)
        else:
            raise ValueError(f"unknown filetype {ext}")

        return output_path

    def validate(self):
        """Validate the ASDF file"""
        return self._asdf_file.validate()

    def info(self, *args, **kwargs):
        """Pass through to the AsdfFile info method"""
        return self._asdf_file.info(*args, **kwargs)

    def search(self, *args, **kwargs):
        """Pass through to the AsdfFile search method"""
        return self._asdf_file.search(*args, **kwargs)

    def schema_info(self, *args, **kwargs):
        """Pass through to the AsdfFile schema_info method"""
        return self._asdf_file.schema_info(*args, **kwargs)
