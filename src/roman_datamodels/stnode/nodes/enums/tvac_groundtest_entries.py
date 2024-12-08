from enum import Enum

from roman_datamodels.stnode import rad

__all__ = ["TvacGroundtestGsorcSdsDqPulseEntry", "TvacGroundtestWfiOptTargettypeEntry"]


class TvacGroundtestGsorcSdsDqPulseEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls):
        from ..tvac import TvacGroundtest

        return TvacGroundtest

    @classmethod
    def asdf_property_name(cls):
        return "gsorc_sds_dq_pulse"


class TvacGroundtestGsorcSdsDqPulseEntry(TvacGroundtestGsorcSdsDqPulseEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible values of the GSORC SDS DQ Pulse
    """

    PULSE = "pulse"
    CW = "cw"


class TvacGroundtestWfiOptTargettypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls):
        from ..tvac import TvacGroundtest

        return TvacGroundtest

    @classmethod
    def asdf_property_name(cls):
        return "wfi_opt_targettype"


class TvacGroundtestWfiOptTargettypeEntry(TvacGroundtestWfiOptTargettypeEntryMixin, Enum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible values of the WFI Optical Target Type
    """

    NONE = "NONE"
    FLAT_SRCS = "FLAT-sRCS"
    FLAT_SORC = "FLAT-SORC"
    POINT_SOURCE = "POINT SOURCE"
    SPECTRUM = "SPECTRUM"
    DARK = "DARK"
    DARK_DARKEL = "DARK-DARKEL"
    DARK_W146 = "DARK-W146"
    PHARET_GW = "PHARET-GW"
    PHARET_FF = "PHARET-FF"
    PHARET_FF_F158 = "PHARET-FF-F158"
    PHARET_FF_M3MM = "PHARET-FF-M3MM"
    PHARET_FF_M6MM = "PHARET-FF-M6MM"
    PHARET_FF_P3MM = "PHARET-FF-P3MM"
    PHARET_FF_P6MM = "PHARET-FF-P6MM"
    PHARET_FF_PRISM = "PHARET-FF-PRISM"
    PHARET_FF_W146 = "PHARET-FF-W146"
    POINT_SOURCE_GW = "POINT-SOURCE-GW"
    STRAY_LIGHT = "STRAY LIGHT"
