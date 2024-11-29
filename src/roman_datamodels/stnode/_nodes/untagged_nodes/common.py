from .basic import Basic

__all__ = ["Common"]


class Common(Basic):
    @property
    def schema_uri(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/common-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            *super().required,
            "coordinates",
            "ephemeris",
            "exposure",
            "guide_star",
            "instrument",
            "observation",
            "pointing",
            "program",
            "ref_file",
            "rcs",
            "velocity_aberration",
            "visit",
            "wcsinfo",
        )
