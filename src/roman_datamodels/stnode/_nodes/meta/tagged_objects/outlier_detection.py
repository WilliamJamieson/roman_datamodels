from roman_datamodels.stnode import _core

__all__ = ["OutlierDetection"]


class OutlierDetection(_core.TaggedObjectNode):
    """
    Outlier Detection information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/outlier_detection-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return ("good_bits",)

    @property
    def good_bits(self) -> str:
        return self._get_node("good_bits", lambda: "NA")
