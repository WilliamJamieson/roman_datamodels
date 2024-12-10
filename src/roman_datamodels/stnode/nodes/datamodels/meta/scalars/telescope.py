from enum import Enum
from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["Telescope"]


class TelescopeMixin(str, rad.TaggedScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/telescope-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/telescope-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/telescope-1.0.0"
            }
        )


class Telescope(TelescopeMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Telescope used to acquire the data
    """

    ROMAN = "ROMAN"
