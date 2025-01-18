from __future__ import annotations

from types import MappingProxyType

from astropy.time import Time

from roman_datamodels.stnode import rad

__all__ = ["TvacFileDate"]


# Astropy does not have type hints/stubs for time so MyPy will complain about this class
class TvacFileDate(Time, rad.TaggedScalarNode[Time]):  # type: ignore[misc]
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/file_date-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/tvac/file_date-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/tagged_scalars/file_date-1.0.0"
            }
        )

    @classmethod
    def default(cls) -> TvacFileDate:
        return cls(Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))
