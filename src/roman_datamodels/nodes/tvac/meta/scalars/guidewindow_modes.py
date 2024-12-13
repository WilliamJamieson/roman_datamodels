from roman_datamodels.stnode import rad

__all__ = ["TvacGuidewindowModes"]


class TvacGuidewindowModesMixin(str, rad.SchemaScalarNode, rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/guidewindow_modes-1.0.0",)


class TvacGuidewindowModes(TvacGuidewindowModesMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Guidewindow modes
    """

    WIM_ACQ = "WIM-ACQ"
    WIM_TRACK = "WIM-TRACK"
    WSM_ACQ_1 = "WSM-ACQ-1"
    WSM_ACQ_2 = "WSM-ACQ-2"
    WSM_TRACK = "WSM-TRACK"
    DEFOCUSED_MODERATE = "DEFOCUSED-MODERATE"
    DEFOCUSED_LARGE = "DEFOCUSED-LARGE"
