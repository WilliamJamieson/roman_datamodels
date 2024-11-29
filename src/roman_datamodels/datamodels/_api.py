# from abc import abstractmethod
import sys
from contextlib import contextmanager
from pathlib import Path

from roman_datamodels import validate

__all__ = ["StpipeAPIMixin"]


@contextmanager
def _temporary_update_filename(datamodel, filename):
    """
    Context manager to temporarily update the filename of a datamodel so that it
    can be saved with that new file name without changing the current model's filename
    """
    from roman_datamodels.stnode import Filename

    if "meta" in datamodel._instance and "filename" in datamodel._instance.meta:
        old_filename = datamodel._instance.meta.filename
        datamodel._instance.meta.filename = Filename(filename)

        yield
        datamodel._instance.meta.filename = old_filename
        return

    yield
    return


class StpipeAPIMixin:
    @property
    def crds_observatory(self) -> str:
        """The observatory for CRDS."""
        return "roman"

    # Should be enabled after refactoring to have properties
    # @property
    # @abstractmethod
    # def meta(self) -> dict:
    #     """The metadata for the model."""
    #     pass

    def get_crds_parameters(self) -> dict[str, str | int | float | complex | bool]:
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

    def to_asdf(self, init, *args, **kwargs):
        with validate.nuke_validation(), _temporary_update_filename(self, Path(init).name):
            asdf_file = self.open_asdf(**kwargs)
            asdf_file["roman"] = self._instance
            asdf_file.write_to(init, *args, **kwargs)

    def save(self, path, dir_path=None, *args, **kwargs):
        path = Path(path(self.meta.filename) if callable(path) else path)
        output_path = Path(dir_path) / path.name if dir_path else path
        ext = path.suffix.decode(sys.getfilesystemencoding()) if isinstance(path.suffix, bytes) else path.suffix

        # TODO: Support gzip-compressed fits
        if ext == ".asdf":
            self.to_asdf(output_path, *args, **kwargs)
        else:
            raise ValueError(f"unknown filetype {ext}")

        return output_path
