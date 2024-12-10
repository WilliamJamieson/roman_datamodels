from enum import Enum
from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["TvacTelescope"]


class TvacTelescopeMixin(str, rad.TaggedScalarNode, rad.EnumNodeMixin):
    """
    Telescope used to acquire the data
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/telescope-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/tvac/telescope-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/telescope-1.0.0"
            }
        )


class TvacTelescope(TvacTelescopeMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enumerate the telescopes
    """

    ROMAN = "ROMAN"
