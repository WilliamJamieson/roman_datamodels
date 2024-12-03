from astropy.time import Time

from roman_datamodels.stnode import _core

__all__ = ["TvacFileDate"]


class TvacFileDate(Time, _core.TaggedScalarNode):
    """
    Date this file was created (UTC)
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/file_date-1.0.0"
