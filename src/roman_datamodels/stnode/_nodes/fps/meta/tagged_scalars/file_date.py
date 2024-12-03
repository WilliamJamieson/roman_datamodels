from astropy.time import Time

from roman_datamodels.stnode import _core

__all__ = ["FpsFileDate"]


class FpsFileDate(Time, _core.TaggedScalarNode):
    """
    Date this file was created (UTC)
    """

    @property
    def tag(self):
        return "asdf://stsci.edu/datamodels/roman/tags/fps/file_date-1.0.0"
