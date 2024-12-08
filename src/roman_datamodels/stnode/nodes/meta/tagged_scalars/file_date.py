from astropy.time import Time

from roman_datamodels.stnode import rad

__all__ = ["FileDate"]


class FileDate(Time, rad.TaggedScalarNode):
    """
    Date this file was created (UTC)
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/file_date-1.0.0"
