from astropy import time

from roman_datamodels.stnode import _core

__all__ = ["FileDate"]


class FileDate(time.Time, _core.TaggedScalarNode):
    """
    Date this file was created (UTC)
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/file_date-1.0.0"
