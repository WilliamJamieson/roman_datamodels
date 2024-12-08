from roman_datamodels.stnode import rad

__all__ = ["OutlierDetection"]


class OutlierDetection(rad.TaggedObjectNode):
    """
    Outlier Detection information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/outlier_detection-1.0.0"

    @rad.rad_field
    def good_bits(self) -> str:
        return self._get_node("good_bits", lambda: "NA")
