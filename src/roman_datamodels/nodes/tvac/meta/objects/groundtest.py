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


class TvacGroundtestGsorcSdsDqPulseEntry(TvacGroundtestGsorcSdsDqPulseEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
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


class TvacGroundtestWfiOptTargettypeEntry(TvacGroundtestWfiOptTargettypeEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
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
        return rad.NOSTR

    @rad.field
    def test_phase(self) -> str:
        return rad.NOSTR

    @rad.field
    def test_environment(self) -> str:
        return rad.NOSTR

    @rad.field
    def test_script(self) -> str:
        return rad.NOSTR

    @rad.field
    def product_date(self) -> Time:
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")

    @rad.field
    def product_version(self) -> str:
        return rad.NOSTR

    @rad.field
    def conversion_date(self) -> Time:
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")

    @rad.field
    def conversion_version(self) -> str:
        return rad.NOSTR

    @rad.field
    def filename_pnt5(self) -> str:
        return rad.NOSTR

    @rad.field
    def filepath_level_pnt5(self) -> str:
        return rad.NOSTR

    @rad.field
    def filename_l1a(self) -> str:
        return rad.NOSTR

    @rad.field
    def detector_id(self) -> str:
        return rad.NOSTR

    @rad.field
    def detector_temp(self) -> float:
        return rad.NONUM

    @rad.field
    def frames_temp(self) -> np.ndarray:
        return np.zeros(6, dtype=np.float64)

    @rad.field
    def ota_temp(self) -> float:
        return rad.NONUM

    @rad.field
    def rcs_on(self) -> bool:
        return False

    @rad.field
    def readout_col_num(self) -> int:
        return rad.NOINT

    @rad.field
    def detector_pixel_size(self) -> u.Quantity:
        return u.Quantity(np.zeros(6, dtype=np.float64), unit=u.cm, dtype=np.float64)

    @rad.field
    def sensor_error(self) -> np.ndarray:
        return np.zeros(6, dtype=np.float64)

    @rad.field
    def activity_number(self) -> int:
        return rad.NOINT

    @rad.field
    def led_bank1_band_number_on(self) -> core.LNode[int]:
        return core.LNode([rad.NOINT])

    @rad.field
    def led_bank2_bank1_number_on(self) -> core.LNode[int]:
        return core.LNode([rad.NOINT])

    @rad.field
    def led_bank1_approx_wlen(self) -> u.Quantity:
        return u.Quantity(np.zeros(6, dtype=np.float64), unit=u.nm, dtype=np.float64)

    @rad.field
    def led_bank2_approx_wlen(self) -> u.Quantity:
        return u.Quantity(np.zeros(6, dtype=np.float64), unit=u.nm, dtype=np.float64)

    @rad.field
    def srcs_pd_voltage(self) -> float:
        return rad.NONUM

    @rad.field
    def srcs_led_flux(self) -> float:
        return rad.NONUM

    @rad.field
    def wfi_mce_srcs_bank1_led_i(self) -> u.Quantity:
        return u.Quantity(np.zeros(6, dtype=np.float64), unit=u.A, dtype=np.float64)

    @rad.field
    def wfi_mce_srcs_bank1_led_range(self) -> str:
        return rad.NOSTR

    @rad.field
    def wfi_mce_srcs_bank2_led_i(self) -> u.Quantity:
        return u.Quantity(np.zeros(6, dtype=np.float64), unit=u.A, dtype=np.float64)

    @rad.field
    def wfi_mce_srcs_bank2_led_range(self) -> str:
        return rad.NOSTR

    @rad.field
    def srcs_led_current(self) -> float:
        return rad.NONUM

    @rad.field
    def wfi_opt_targettype(self) -> TvacGroundtestWfiOptTargettypeEntry:
        return TvacGroundtestWfiOptTargettypeEntry.FLAT_SRCS

    @rad.field
    def analysis_tag(self) -> str:
        return rad.NOSTR

    @rad.field
    def gsorc_pose_mode(self) -> str:
        return rad.NOSTR

    @rad.field
    def gsorc_pose_target(self) -> str:
        return rad.NOSTR

    @rad.field
    def gsorc_sds_active_atten(self) -> float:
        return rad.NONUM

    @rad.field
    def gsorc_sds_lltfir_wave(self) -> float:
        return rad.NONUM

    @rad.field
    def gsorc_sds_sorc_on(self) -> bool:
        return False

    @rad.field
    def gsorc_sds_sorc_wlen(self) -> float:
        return rad.NONUM

    @rad.field
    def gsorc_sds_active_source(self) -> str:
        return rad.NOSTR

    @rad.field
    def gsorc_sds_dq_pulse(self) -> TvacGroundtestGsorcSdsDqPulseEntry:
        return TvacGroundtestGsorcSdsDqPulseEntry.PULSE

    @rad.field
    def gsorc_sds_daq_pw(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.ms)

    @rad.field
    def gsorc_heater1_setpt(self) -> float:
        return rad.NONUM

    @rad.field
    def wfi_otp_wfi_ewa(self) -> str:
        return rad.NOSTR

    @rad.field
    def sca_temp(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.K)

    @rad.field
    def mpa_temp(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.K)

    @rad.field
    def ewa_temp(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.K)

    @rad.field
    def ewta_outer_heater_temp(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.K)

    @rad.field
    def ewta_inner_heater_temp(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.K)

    @rad.field
    def coba_temp_near_ewta(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.K)

    @rad.field
    def scea_temp(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.K)

    @rad.field
    def wfi_sce_1_vbiasgate_v(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.V)

    @rad.field
    def wfi_sce_1_vbiaspwr_i(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.A)

    @rad.field
    def wfi_sce_1_vbiaspwr_v(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.V)

    @rad.field
    def wfi_sce_1_vreset_v(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.V)

    @rad.field
    def wfi_sce_1_vreset_i(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.A)

    @rad.field
    def wfi_mcu_a_offs_csense_fpssen(self) -> u.Quantity:
        return u.Quantity(rad.NONUM, u.K)
