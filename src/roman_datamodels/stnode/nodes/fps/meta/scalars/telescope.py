from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["FpsTelescope"]


class FpsTelescopeMixin(str, rad.TaggedScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/telescope-1.0.0",)

    @classmethod
    def asdf_tag(cls):
        return "asdf://stsci.edu/datamodels/roman/tags/fps/telescope-1.0.0"


class FpsTelescope(FpsTelescopeMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Telescope used to acquire the data
    """

    ROMAN = "ROMAN"
