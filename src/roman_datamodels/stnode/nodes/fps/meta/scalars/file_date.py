from astropy.time import Time

from roman_datamodels.stnode import rad

__all__ = ["FpsFileDate"]


class FpsFileDate(Time, rad.TaggedScalarNode):
    """
    Date this file was created (UTC)
    """

    @classmethod
    def asdf_schema_uri(cls):
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/file_date-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/file_date-1.0.0"
