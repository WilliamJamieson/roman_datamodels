from __future__ import annotations

from roman_datamodels.stnode import rad

__all__ = ["TvacTelescope", "TvacTelescopeMixin"]


class TvacTelescopeMixin(str, rad.TaggedScalarNode, rad.EnumNodeMixin):
    @classmethod
    def _asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/telescope-1.0.0",)

    @classmethod
    def _asdf_tag_uris(cls) -> dict[str, str]:
        return {
            "asdf://stsci.edu/datamodels/roman/tags/tvac/telescope-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/telescope-1.0.0"
        }


class TvacTelescope(TvacTelescopeMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    ROMAN = "ROMAN"

    @classmethod
    def default(cls) -> TvacTelescope:
        return cls.ROMAN
