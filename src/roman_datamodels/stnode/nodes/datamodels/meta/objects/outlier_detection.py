from roman_datamodels.stnode import rad

__all__ = ["OutlierDetection"]


class OutlierDetection(rad.TaggedObjectNode):
    """
    Outlier Detection information
    """

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/outlier_detection-1.0.0"

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/outlier_detection-1.0.0"

    @rad.field
    def good_bits(self) -> str:
        return self._get_node("good_bits", lambda: "NA")
