from types import MappingProxyType

from roman_datamodels.stnode import rad

__all__ = ["OutlierDetection"]


class OutlierDetection(rad.TaggedObjectNode):
    """
    Outlier Detection information
    """

    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/outlier_detection-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/outlier_detection-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/outlier_detection-1.0.0"
            }
        )

    @rad.field
    def good_bits(self) -> str:
        return "NA"
