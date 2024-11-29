from roman_datamodels.stnode import _core

__all__ = ["Coordinates"]


class Coordinates(_core.TaggedNode):
    """
    Coordinate frame information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/coordinates-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return ("reference_frame",)

    @property
    def reference_frame(self) -> str:
        if not self._has_node("reference_frame"):
            self.reference_frame = "ICRS"

        return self._get_node("reference_frame")
