import numpy as np
from astropy import units as u
from astropy.time import Time

from roman_datamodels.stnode import _core, _default

__all__ = ["TvacGroundtest"]


class TvacGroundtest(_core.TaggedObjectNode):
    """
    Tvac Ground test description.
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac/groundtest-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "test_name",
            "test_phase",
            "test_environment",
            "test_script",
            "product_date",
            "product_version",
            "conversion_date",
            "conversion_version",
            "filename_pnt5",
            "filepath_level_pnt5",
            "filename_l1a",
            "detector_id",
            "detector_temp",
            "frames_temp",
            "ota_temp",
            "rcs_on",
            "readout_col_num",
            "detector_pixel_size",
            "sensor_error",
        )

    @property
    def test_name(self) -> str:
        return self._get_node("test_name", lambda: _default.NOSTR)

    @property
    def test_phase(self) -> str:
        return self._get_node("test_phase", lambda: _default.NOSTR)

    @property
    def test_environment(self) -> str:
        return self._get_node("test_environment", lambda: _default.NOSTR)

    @property
    def test_script(self) -> str:
        return self._get_node("test_script", lambda: _default.NOSTR)

    @property
    def product_date(self) -> Time:
        return self._get_node("product_date", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @property
    def product_version(self) -> str:
        return self._get_node("product_version", lambda: _default.NOSTR)

    @property
    def conversion_date(self) -> Time:
        return self._get_node("conversion_date", lambda: Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

    @property
    def conversion_version(self) -> str:
        return self._get_node("conversion_version", lambda: _default.NOSTR)

    @property
    def filename_pnt5(self) -> str:
        return self._get_node("filename_pnt5", lambda: _default.NOSTR)

    @property
    def filepath_level_pnt5(self) -> str:
        return self._get_node("filepath_level_pnt5", lambda: _default.NOSTR)

    @property
    def filename_l1a(self) -> str:
        return self._get_node("filename_l1a", lambda: _default.NOSTR)

    @property
    def detector_id(self) -> str:
        return self._get_node("detector_id", lambda: _default.NOSTR)

    @property
    def detector_temp(self) -> float:
        return self._get_node("detector_temp", lambda: _default.NONUM)

    @property
    def frames_temp(self) -> np.ndarray:
        return self._get_node("frames_temp", lambda: np.zeros(6, dtype=np.float64))

    @property
    def ota_temp(self) -> float:
        return self._get_node("ota_temp", lambda: _default.NONUM)

    @property
    def rcs_on(self) -> bool:
        return self._get_node("rcs_on", lambda: False)

    @property
    def readout_col_num(self) -> int:
        return self._get_node("readout_col_num", lambda: _default.NONUM)

    @property
    def detector_pixel_size(self) -> u.Quantity:
        return self._get_node(
            "detector_pixel_size", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.cm, dtype=np.float64)
        )

    @property
    def sensor_error(self) -> np.ndarray:
        return self._get_node("sensor_error", lambda: np.zeros(6, dtype=np.float64))

    @property
    def activity_number(self) -> int:
        return self._get_node("activity_number", lambda: _default.NONUM)

    @property
    def led_bank1_band_number_on(self) -> list[int]:
        return self._get_node("led_bank1_band_number_on", lambda: [_default.NONUM])

    @property
    def led_bank2_bank1_number_on(self) -> list[int]:
        return self._get_node("led_bank2_bank1_number_on", lambda: [_default.NONUM])

    @property
    def led_bank1_approx_wlen(self) -> u.Quantity:
        return self._get_node(
            "led_bank1_approx_wlen", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.nm, dtype=np.float64)
        )

    @property
    def led_bank2_approx_wlen(self) -> u.Quantity:
        return self._get_node(
            "led_bank2_approx_wlen", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.nm, dtype=np.float64)
        )

    @property
    def srcs_pd_voltage(self) -> float:
        return self._get_node("srcs_pd_voltage", lambda: _default.NONUM)

    @property
    def srcs_led_flux(self) -> float:
        return self._get_node("srcs_led_flux", lambda: _default.NONUM)

    @property
    def wfi_mce_srcs_bank1_led_i(self) -> u.Quantity:
        return self._get_node(
            "wfi_mce_srcs_bank1_led_i", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.A, dtype=np.float64)
        )

    @property
    def wfi_mce_srcs_bank1_led_range(self) -> str:
        return self._get_node("wfi_mce_srcs_bank1_led_range", lambda: _default.NOSTR)

    @property
    def wfi_mce_srcs_bank2_led_i(self) -> u.Quantity:
        return self._get_node(
            "wfi_mce_srcs_bank2_led_i", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.A, dtype=np.float64)
        )

    @property
    def wfi_mce_srcs_bank2_led_range(self) -> str:
        return self._get_node("wfi_mce_srcs_bank2_led_range", lambda: _default.NOSTR)

    @property
    def srcs_led_current(self) -> float:
        return self._get_node("srcs_led_current", lambda: _default.NONUM)

    @property
    def wfi_opt_targettype(self) -> str:
        return self._get_node("wfi_opt_targettype", lambda: "FLAT-sRCS")

    @property
    def analysis_tag(self) -> str:
        return self._get_node("analysis_tag", lambda: _default.NOSTR)

    @property
    def gsorc_pose_mode(self) -> str:
        return self._get_node("gsorc_pose_mode", lambda: _default.NOSTR)

    @property
    def gsorc_pose_target(self) -> str:
        return self._get_node("gsorc_pose_target", lambda: _default.NOSTR)

    @property
    def gsorc_sds_active_atten(self) -> float:
        return self._get_node("gsorc_sds_active_atten", lambda: _default.NONUM)

    @property
    def gsorc_sds_lltfir_wave(self) -> float:
        return self._get_node("gsorc_sds_lltfir_wave", lambda: _default.NONUM)

    @property
    def gsorc_sds_sorc_on(self) -> bool:
        return self._get_node("gsorc_sds_sorc_on", lambda: False)

    @property
    def gsorc_sds_sorc_wlen(self) -> float:
        return self._get_node("gsorc_sds_sorc_wlen", lambda: _default.NONUM)

    @property
    def gsorc_sds_active_source(self) -> str:
        return self._get_node("gsorc_sds_active_source", lambda: _default.NOSTR)

    @property
    def gsorc_sds_dq_pulse(self) -> str:
        return self._get_node("gsorc_sds_dq_pulse", lambda: "pulse")

    @property
    def gsorc_sds_daq_pw(self) -> u.Quantity:
        return self._get_node("gsorc_sds_daq_pw", lambda: u.Quantity(_default.NONUM, u.ms))

    @property
    def gsorc_heater1_setpt(self) -> float:
        return self._get_node("gsorc_heater1_setpt", lambda: _default.NONUM)

    @property
    def wfi_otp_wfi_ewa(self) -> str:
        return self._get_node("wfi_otp_wfi_ewa", lambda: _default.NOSTR)

    @property
    def sca_temp(self) -> u.Quantity:
        return self._get_node("sca_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @property
    def mpa_temp(self) -> u.Quantity:
        return self._get_node("mpa_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @property
    def ewa_temp(self) -> u.Quantity:
        return self._get_node("ewa_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @property
    def ewta_outer_heater_temp(self) -> u.Quantity:
        return self._get_node("ewta_outer_heater_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @property
    def ewta_inner_heater_temp(self) -> u.Quantity:
        return self._get_node("ewta_inner_heater_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @property
    def coba_temp_near_ewta(self) -> u.Quantity:
        return self._get_node("coba_temp_near_ewta", lambda: u.Quantity(_default.NONUM, u.K))

    @property
    def scea_temp(self) -> u.Quantity:
        return self._get_node("scea_temp", lambda: u.Quantity(_default.NONUM, u.K))

    @property
    def wfi_sce_1_vbiasgate_v(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vbiasgate_v", lambda: u.Quantity(_default.NONUM, u.V))

    @property
    def wfi_sce_1_vbiaspwr_i(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vbiaspwr_i", lambda: u.Quantity(_default.NONUM, u.A))

    @property
    def wfi_sce_1_vbiaspwr_v(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vbiaspwr_v", lambda: u.Quantity(_default.NONUM, u.V))

    @property
    def wfi_sce_1_vreset_v(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vreset_v", lambda: u.Quantity(_default.NONUM, u.V))

    @property
    def wfi_sce_1_vreset_i(self) -> u.Quantity:
        return self._get_node("wfi_sce_1_vreset_i", lambda: u.Quantity(_default.NONUM, u.A))

    @property
    def wfi_mcu_a_offs_csense_fpssen(self) -> u.Quantity:
        return self._get_node("wfi_mcu_a_offs_csense_fpssen", lambda: u.Quantity(_default.NONUM, u.K))
