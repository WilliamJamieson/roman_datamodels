from enum import Enum
from types import MappingProxyType

import numpy as np
from astropy import units as u
from astropy.time import Time

from roman_datamodels.stnode import core, rad

__all__ = [
    "TvacGroundtest",
    "TvacGroundtestGsorcSdsDqPulseEntry",
    "TvacGroundtestWfiOptTargettypeEntry",
]


class TvacGroundtestGsorcSdsDqPulseEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode):
    @classmethod
    def asdf_container(cls):
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


class TvacGroundtest(rad.TaggedObjectNode):
    """
    Tvac Ground test description.
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/groundtest-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/tvac/groundtest-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/tvac/groundtest-1.0.0"
            }
        )

    @rad.field
    def test_name(self) -> str:
        return self._get_node("test_name", lambda: rad.NOSTR)

    @rad.field
    def test_phase(self) -> str:
        return self._get_node("test_phase", lambda: rad.NOSTR)

    @rad.field
    def test_environment(self) -> str:
        return self._get_node("test_environment", lambda: rad.NOSTR)

    @rad.field
    def test_script(self) -> str:
        return self._get_node("test_script", lambda: rad.NOSTR)

    @rad.field
    def product_date(self) -> Time:
        return self._get_node("product_date", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def product_version(self) -> str:
        return self._get_node("product_version", lambda: rad.NOSTR)

    @rad.field
    def conversion_date(self) -> Time:
        return self._get_node("conversion_date", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @rad.field
    def conversion_version(self) -> str:
        return self._get_node("conversion_version", lambda: rad.NOSTR)

    @rad.field
    def filename_pnt5(self) -> str:
        return self._get_node("filename_pnt5", lambda: rad.NOSTR)

    @rad.field
    def filepath_level_pnt5(self) -> str:
        return self._get_node("filepath_level_pnt5", lambda: rad.NOSTR)

    @rad.field
    def filename_l1a(self) -> str:
        return self._get_node("filename_l1a", lambda: rad.NOSTR)

    @rad.field
    def detector_id(self) -> str:
        return self._get_node("detector_id", lambda: rad.NOSTR)

    @rad.field
    def detector_temp(self) -> float:
        return self._get_node("detector_temp", lambda: rad.NONUM)

    @rad.field
    def frames_temp(self) -> np.ndarray:
        return self._get_node("frames_temp", lambda: np.zeros(6, dtype=np.float64))

    @rad.field
    def ota_temp(self) -> float:
        return self._get_node("ota_temp", lambda: rad.NONUM)

    @rad.field
    def rcs_on(self) -> bool:
        return self._get_node("rcs_on", lambda: False)

    @rad.field
    def readout_col_num(self) -> int:
        return self._get_node("readout_col_num", lambda: rad.NOINT)

    @rad.field
    def detector_pixel_size(self) -> u.Quantity:
        return self._get_node(
            "detector_pixel_size", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.cm, dtype=np.float64)
        )

    @rad.field
    def sensor_error(self) -> np.ndarray:
        return self._get_node("sensor_error", lambda: np.zeros(6, dtype=np.float64))

    @rad.field
    def activity_number(self) -> int:
        return self._get_node("activity_number", lambda: rad.NOINT)

    @rad.field
    def led_bank1_band_number_on(self) -> core.LNode[int]:
        return self._get_node("led_bank1_band_number_on", lambda: core.LNode([rad.NOINT]))

    @rad.field
    def led_bank2_bank1_number_on(self) -> core.LNode[int]:
        return self._get_node("led_bank2_bank1_number_on", lambda: core.LNode([rad.NOINT]))

    @rad.field
    def led_bank1_approx_wlen(self) -> u.Quantity:
        return self._get_node(
            "led_bank1_approx_wlen", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.nm, dtype=np.float64)
        )

    @rad.field
    def led_bank2_approx_wlen(self) -> u.Quantity:
        return self._get_node(
            "led_bank2_approx_wlen", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.nm, dtype=np.float64)
        )

    @rad.field
    def srcs_pd_voltage(self) -> float:
        return self._get_node("srcs_pd_voltage", lambda: rad.NONUM)

    @rad.field
    def srcs_led_flux(self) -> float:
        return self._get_node("srcs_led_flux", lambda: rad.NONUM)

    @rad.field
    def wfi_mce_srcs_bank1_led_i(self) -> u.Quantity:
        return self._get_node(
            "wfi_mce_srcs_bank1_led_i", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.A, dtype=np.float64)
        )

    @rad.field
    def wfi_mce_srcs_bank1_led_range(self) -> str:
        return self._get_node("wfi_mce_srcs_bank1_led_range", lambda: rad.NOSTR)

    @rad.field
    def wfi_mce_srcs_bank2_led_i(self) -> u.Quantity:
        return self._get_node(
            "wfi_mce_srcs_bank2_led_i", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.A, dtype=np.float64)
        )

    @rad.field
    def wfi_mce_srcs_bank2_led_range(self) -> str:
        return self._get_node("wfi_mce_srcs_bank2_led_range", lambda: rad.NOSTR)

    @rad.field
    def srcs_led_current(self) -> float:
        return self._get_node("srcs_led_current", lambda: rad.NONUM)

    @rad.field
    def wfi_opt_targettype(self) -> TvacGroundtestWfiOptTargettypeEntry:
        return self._get_node("wfi_opt_targettype", lambda: TvacGroundtestWfiOptTargettypeEntry.FLAT_SRCS)

    @rad.field
    def analysis_tag(self) -> str:
        return self._get_node("analysis_tag", lambda: rad.NOSTR)

    @rad.field
    def gsorc_pose_mode(self) -> str:
        return self._get_node("gsorc_pose_mode", lambda: rad.NOSTR)

    @rad.field
    def gsorc_pose_target(self) -> str:
        return self._get_node("gsorc_pose_target", lambda: rad.NOSTR)

    @rad.field
    def gsorc_sds_active_atten(self) -> float:
        return self._get_node("gsorc_sds_active_atten", lambda: rad.NONUM)

    @rad.field
    def gsorc_sds_lltfir_wave(self) -> float:
        return self._get_node("gsorc_sds_lltfir_wave", lambda: rad.NONUM)

    @rad.field
    def gsorc_sds_sorc_on(self) -> bool:
        return self._get_node("gsorc_sds_sorc_on", lambda: False)

    @rad.field
    def gsorc_sds_sorc_wlen(self) -> float:
        return self._get_node("gsorc_sds_sorc_wlen", lambda: rad.NONUM)

    @rad.field
    def gsorc_sds_active_source(self) -> str:
        return self._get_node("gsorc_sds_active_source", lambda: rad.NOSTR)

    @rad.field
    def gsorc_sds_dq_pulse(self) -> TvacGroundtestGsorcSdsDqPulseEntry:
        return self._get_node("gsorc_sds_dq_pulse", lambda: TvacGroundtestGsorcSdsDqPulseEntry.PULSE)

    @rad.field
    def gsorc_sds_daq_pw(self) -> u.Quantity:
        return self._get_node("gsorc_sds_daq_pw", lambda: u.Quantity(rad.NONUM, u.ms))

    @rad.field
    def gsorc_heater1_setpt(self) -> float:
        return self._get_node("gsorc_heater1_setpt", lambda: rad.NONUM)

    @rad.field
    def wfi_otp_wfi_ewa(self) -> str:
        return self._get_node("wfi_otp_wfi_ewa", lambda: rad.NOSTR)

    @rad.field
    def sca_temp(self) -> u.Quantity:
        return self._get_node("sca_temp", lambda: u.Quantity(rad.NONUM, u.K))

    @rad.field
    def mpa_temp(self) -> u.Quantity:
        return self._get_node("mpa_temp", lambda: u.Quantity(rad.NONUM, u.K))

    @rad.field
    def ewa_temp(self) -> u.Quantity:
        return self._get_node("ewa_temp", lambda: u.Quantity(rad.NONUM, u.K))

    @rad.field
    def ewta_outer_heater_temp(self) -> u.Quantity:
        return self._get_node("ewta_outer_heater_temp", lambda: u.Quantity(rad.NONUM, u.K))

    @rad.field
    def ewta_inner_heater_temp(self) -> u.Quantity:
        return self._get_node("ewta_inner_heater_temp", lambda: u.Quantity(rad.NONUM, u.K))

    @rad.field
    def coba_temp_near_ewta(self) -> u.Quantity:
        return self._get_node("coba_temp_near_ewta", lambda: u.Quantity(rad.NONUM, u.K))

    @rad.field
    def scea_temp(self) -> u.Quantity:
        return self._get_node("scea_temp", lambda: u.Quantity(rad.NONUM, u.K))

    @rad.field
    def wfi_sce_1_vbiasgate_v(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vbiasgate_v", lambda: u.Quantity(rad.NONUM, u.V))

    @rad.field
    def wfi_sce_1_vbiaspwr_i(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vbiaspwr_i", lambda: u.Quantity(rad.NONUM, u.A))

    @rad.field
    def wfi_sce_1_vbiaspwr_v(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vbiaspwr_v", lambda: u.Quantity(rad.NONUM, u.V))

    @rad.field
    def wfi_sce_1_vreset_v(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vreset_v", lambda: u.Quantity(rad.NONUM, u.V))

    @rad.field
    def wfi_sce_1_vreset_i(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vreset_i", lambda: u.Quantity(rad.NONUM, u.A))

    @rad.field
    def wfi_mcu_a_offs_csense_fpssen(self) -> u.Quantity:
        return self._get_node("wfi_mcu_a_offs_csense_fpssen", lambda: u.Quantity(rad.NONUM, u.K))
