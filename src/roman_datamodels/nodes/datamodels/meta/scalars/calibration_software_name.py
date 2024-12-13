from __future__ import annotations

from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["CalibrationSoftwareName"]


class CalibrationSoftwareName(str, rad.TaggedScalarNode):
    """
    Name of the calibration software used
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/calibration_software_name-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/calibration_software_name-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tagged_scalars/calibration_software_name-1.0.0"
            }
        )

    @classmethod
    def default(cls) -> CalibrationSoftwareName:
        return cls("RomanCAL")
