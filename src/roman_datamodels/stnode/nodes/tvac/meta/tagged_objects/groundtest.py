import numpy as np
from astropy import units as u
from astropy.time import Time

from roman_datamodels.stnode import _base, _core, _default

from ....enums import TvacGroundtestGsorcSdsDqPulseEntry, TvacGroundtestWfiOptTargettypeEntry

__all__ = ["TvacGroundtest"]


class TvacGroundtest(_core.TaggedObjectNode):
    """
    Tvac Ground test description.
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/groundtest-1.0.0"

    @_core.rad_field
    def test_name(self) -> str:
        return self._get_node("test_name", lambda: _default.NOSTR)

    @_core.rad_field
    def test_phase(self) -> str:
        return self._get_node("test_phase", lambda: _default.NOSTR)

    @_core.rad_field
    def test_environment(self) -> str:
        return self._get_node("test_environment", lambda: _default.NOSTR)

    @_core.rad_field
    def test_script(self) -> str:
        return self._get_node("test_script", lambda: _default.NOSTR)

    @_core.rad_field
    def product_date(self) -> Time:
        return self._get_node("product_date", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @_core.rad_field
    def product_version(self) -> str:
        return self._get_node("product_version", lambda: _default.NOSTR)

    @_core.rad_field
    def conversion_date(self) -> Time:
        return self._get_node("conversion_date", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @_core.rad_field
    def conversion_version(self) -> str:
        return self._get_node("conversion_version", lambda: _default.NOSTR)

    @_core.rad_field
    def filename_pnt5(self) -> str:
        return self._get_node("filename_pnt5", lambda: _default.NOSTR)

    @_core.rad_field
    def filepath_level_pnt5(self) -> str:
        return self._get_node("filepath_level_pnt5", lambda: _default.NOSTR)

    @_core.rad_field
    def filename_l1a(self) -> str:
        return self._get_node("filename_l1a", lambda: _default.NOSTR)

    @_core.rad_field
    def detector_id(self) -> str:
        return self._get_node("detector_id", lambda: _default.NOSTR)

    @_core.rad_field
    def detector_temp(self) -> float:
        return self._get_node("detector_temp", lambda: _default.NONUM)

    @_core.rad_field
    def frames_temp(self) -> np.ndarray:
        return self._get_node("frames_temp", lambda: np.zeros(6, dtype=np.float64))

    @_core.rad_field
    def ota_temp(self) -> float:
        return self._get_node("ota_temp", lambda: _default.NONUM)

    @_core.rad_field
    def rcs_on(self) -> bool:
        return self._get_node("rcs_on", lambda: False)

    @_core.rad_field
    def readout_col_num(self) -> int:
        return self._get_node("readout_col_num", lambda: _default.NOINT)

    @_core.rad_field
    def detector_pixel_size(self) -> u.Quantity:
        return self._get_node(
            "detector_pixel_size", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.cm, dtype=np.float64)
        )

    @_core.rad_field
    def sensor_error(self) -> np.ndarray:
        return self._get_node("sensor_error", lambda: np.zeros(6, dtype=np.float64))

    @_core.rad_field
    def activity_number(self) -> int:
        return self._get_node("activity_number", lambda: _default.NOINT)

    @_core.rad_field
    def led_bank1_band_number_on(self) -> _base.LNode[int]:
        return self._get_node("led_bank1_band_number_on", lambda: _base.LNode([_default.NOINT]))

    @_core.rad_field
    def led_bank2_bank1_number_on(self) -> _base.LNode[int]:
        return self._get_node("led_bank2_bank1_number_on", lambda: _base.LNode([_default.NOINT]))

    @_core.rad_field
    def led_bank1_approx_wlen(self) -> u.Quantity:
        return self._get_node(
            "led_bank1_approx_wlen", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.nm, dtype=np.float64)
        )

    @_core.rad_field
    def led_bank2_approx_wlen(self) -> u.Quantity:
        return self._get_node(
            "led_bank2_approx_wlen", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.nm, dtype=np.float64)
        )

    @_core.rad_field
    def srcs_pd_voltage(self) -> float:
        return self._get_node("srcs_pd_voltage", lambda: _default.NONUM)

    @_core.rad_field
    def srcs_led_flux(self) -> float:
        return self._get_node("srcs_led_flux", lambda: _default.NONUM)

    @_core.rad_field
    def wfi_mce_srcs_bank1_led_i(self) -> u.Quantity:
        return self._get_node(
            "wfi_mce_srcs_bank1_led_i", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.A, dtype=np.float64)
        )

    @_core.rad_field
    def wfi_mce_srcs_bank1_led_range(self) -> str:
        return self._get_node("wfi_mce_srcs_bank1_led_range", lambda: _default.NOSTR)

    @_core.rad_field
    def wfi_mce_srcs_bank2_led_i(self) -> u.Quantity:
        return self._get_node(
            "wfi_mce_srcs_bank2_led_i", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.A, dtype=np.float64)
        )

    @_core.rad_field
    def wfi_mce_srcs_bank2_led_range(self) -> str:
        return self._get_node("wfi_mce_srcs_bank2_led_range", lambda: _default.NOSTR)

    @_core.rad_field
    def srcs_led_current(self) -> float:
        return self._get_node("srcs_led_current", lambda: _default.NONUM)

    @_core.rad_field
    def wfi_opt_targettype(self) -> TvacGroundtestWfiOptTargettypeEntry:
        return self._get_node("wfi_opt_targettype", lambda: TvacGroundtestWfiOptTargettypeEntry.FLAT_SRCS)

    @_core.rad_field
    def analysis_tag(self) -> str:
        return self._get_node("analysis_tag", lambda: _default.NOSTR)

    @_core.rad_field
    def gsorc_pose_mode(self) -> str:
        return self._get_node("gsorc_pose_mode", lambda: _default.NOSTR)

    @_core.rad_field
    def gsorc_pose_target(self) -> str:
        return self._get_node("gsorc_pose_target", lambda: _default.NOSTR)

    @_core.rad_field
    def gsorc_sds_active_atten(self) -> float:
        return self._get_node("gsorc_sds_active_atten", lambda: _default.NONUM)

    @_core.rad_field
    def gsorc_sds_lltfir_wave(self) -> float:
        return self._get_node("gsorc_sds_lltfir_wave", lambda: _default.NONUM)

    @_core.rad_field
    def gsorc_sds_sorc_on(self) -> bool:
        return self._get_node("gsorc_sds_sorc_on", lambda: False)

    @_core.rad_field
    def gsorc_sds_sorc_wlen(self) -> float:
        return self._get_node("gsorc_sds_sorc_wlen", lambda: _default.NONUM)

    @_core.rad_field
    def gsorc_sds_active_source(self) -> str:
        return self._get_node("gsorc_sds_active_source", lambda: _default.NOSTR)

    @_core.rad_field
    def gsorc_sds_dq_pulse(self) -> TvacGroundtestGsorcSdsDqPulseEntry:
        return self._get_node("gsorc_sds_dq_pulse", lambda: TvacGroundtestGsorcSdsDqPulseEntry.PULSE)

    @_core.rad_field
    def gsorc_sds_daq_pw(self) -> u.Quantity:
        return self._get_node("gsorc_sds_daq_pw", lambda: u.Quantity(_default.NONUM, u.ms))

    @_core.rad_field
    def gsorc_heater1_setpt(self) -> float:
        return self._get_node("gsorc_heater1_setpt", lambda: _default.NONUM)

    @_core.rad_field
    def wfi_otp_wfi_ewa(self) -> str:
        return self._get_node("wfi_otp_wfi_ewa", lambda: _default.NOSTR)

    @_core.rad_field
    def sca_temp(self) -> u.Quantity:
        return self._get_node("sca_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @_core.rad_field
    def mpa_temp(self) -> u.Quantity:
        return self._get_node("mpa_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @_core.rad_field
    def ewa_temp(self) -> u.Quantity:
        return self._get_node("ewa_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @_core.rad_field
    def ewta_outer_heater_temp(self) -> u.Quantity:
        return self._get_node("ewta_outer_heater_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @_core.rad_field
    def ewta_inner_heater_temp(self) -> u.Quantity:
        return self._get_node("ewta_inner_heater_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @_core.rad_field
    def coba_temp_near_ewta(self) -> u.Quantity:
        return self._get_node("coba_temp_near_ewta", lambda: u.Quantity(_default.NONUM, u.K))

    @_core.rad_field
    def scea_temp(self) -> u.Quantity:
        return self._get_node("scea_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @_core.rad_field
    def wfi_sce_1_vbiasgate_v(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vbiasgate_v", lambda: u.Quantity(_default.NONUM, u.V))

    @_core.rad_field
    def wfi_sce_1_vbiaspwr_i(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vbiaspwr_i", lambda: u.Quantity(_default.NONUM, u.A))

    @_core.rad_field
    def wfi_sce_1_vbiaspwr_v(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vbiaspwr_v", lambda: u.Quantity(_default.NONUM, u.V))

    @_core.rad_field
    def wfi_sce_1_vreset_v(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vreset_v", lambda: u.Quantity(_default.NONUM, u.V))

    @_core.rad_field
    def wfi_sce_1_vreset_i(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vreset_i", lambda: u.Quantity(_default.NONUM, u.A))

    @_core.rad_field
    def wfi_mcu_a_offs_csense_fpssen(self) -> u.Quantity:
        return self._get_node("wfi_mcu_a_offs_csense_fpssen", lambda: u.Quantity(_default.NONUM, u.K))
