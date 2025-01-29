from roman_datamodels.stnode import rad

__all__ = ["FpsGuidewindowModes", "FpsGuidewindowModesMixin"]


class FpsGuidewindowModesMixin(str, rad.SchemaScalarNode[str], rad.EnumNodeMixin):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/guidewindow_modes-1.0.0",)


class FpsGuidewindowModes(FpsGuidewindowModesMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    WIM_ACQ = "WIM-ACQ"
    WIM_TRACK = "WIM-TRACK"
    WSM_ACQ_1 = "WSM-ACQ-1"
    WSM_ACQ_2 = "WSM-ACQ-2"
    WSM_TRACK = "WSM-TRACK"
    DEFOCUSED_MODERATE = "DEFOCUSED-MODERATE"
    DEFOCUSED_LARGE = "DEFOCUSED-LARGE"
