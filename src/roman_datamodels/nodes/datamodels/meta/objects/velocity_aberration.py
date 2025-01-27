from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["VelocityAberration"]


class VelocityAberration(rad.TaggedObjectNode[float]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/velocity_aberration-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/velocity_aberration-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/velocity_aberration-1.0.0"
            }
        )

    @rad.field
    def ra_reference(self) -> float:
        return rad.NONUM

    @rad.field
    def dec_reference(self) -> float:
        return rad.NONUM

    @rad.field
    def scale_factor(self) -> float:
        return 1.0
