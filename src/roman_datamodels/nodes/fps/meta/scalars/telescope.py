from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["FpsTelescope", "FpsTelescopeMixin"]


class FpsTelescopeMixin(str, rad.TaggedScalarNode[str], rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/telescope-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/fps/telescope-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/fps/tagged_scalars/telescope-1.0.0"
            }
        )


class FpsTelescope(FpsTelescopeMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    ROMAN = "ROMAN"

    @classmethod
    def default(cls) -> FpsTelescope:
        return cls.ROMAN
