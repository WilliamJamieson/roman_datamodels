from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt
from astropy.time import Time
from astropy.units import A, K, Quantity, V, cm, ms, nm

from roman_datamodels.stnode import core, rad

__all__ = [
    "TvacGroundtest",
    "TvacGroundtestGsorcSdsDqPulseEntry",
    "TvacGroundtestWfiOptTargettypeEntry",
]


class TvacGroundtestGsorcSdsDqPulseEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return TvacGroundtest

    @classmethod
    def asdf_property_name(cls) -> str:
        return "gsorc_sds_dq_pulse"


class TvacGroundtestGsorcSdsDqPulseEntry(TvacGroundtestGsorcSdsDqPulseEntryMixin, rad.RadEnum, metaclass=rad.NodeEnumMeta):
    """
    Enum for the possible values of the GSORC SDS DQ Pulse
    """

    PULSE = "pulse"
    CW = "cw"


class TvacGroundtestWfiOptTargettypeEntryMixin(str, rad.EnumNodeMixin, rad.ScalarNode[str]):
    @classmethod
    def asdf_container(cls) -> type:
        return TvacGroundtest

    @classmethod
    def asdf_property_name(cls) -> str:
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


_TvacGroundtest: TypeAlias = (
    TvacGroundtestWfiOptTargettypeEntry
    | TvacGroundtestGsorcSdsDqPulseEntry
    | core.LNode[int]
    | npt.NDArray[np.float64]
    | Time
    | Quantity
    | str
    | bool
    | int
)


class TvacGroundtest(rad.TaggedObjectNode[_TvacGroundtest]):
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

    @property
    @rad.field
    def test_name(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def test_phase(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def test_environment(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def test_script(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def product_date(self: rad.Node) -> Time:
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")

    @property
    @rad.field
    def product_version(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def conversion_date(self: rad.Node) -> Time:
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")

    @property
    @rad.field
    def conversion_version(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def filename_pnt5(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def filepath_level_pnt5(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def filename_l1a(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def detector_id(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def detector_temp(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def frames_temp(self: rad.Node) -> npt.NDArray[np.float64]:
        return np.zeros(6, dtype=np.float64)

    @property
    @rad.field
    def ota_temp(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def rcs_on(self: rad.Node) -> bool:
        return False

    @property
    @rad.field
    def readout_col_num(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def detector_pixel_size(self: rad.Node) -> Quantity:
        return Quantity(np.zeros(6, dtype=np.float64), unit=cm, dtype=np.float64)

    @property
    @rad.field
    def sensor_error(self: rad.Node) -> npt.NDArray[np.float64]:
        return np.zeros(6, dtype=np.float64)

    @property
    @rad.field
    def activity_number(self: rad.Node) -> int:
        return rad.NOINT

    @property
    @rad.field
    def led_bank1_band_number_on(self: rad.Node) -> core.LNode[int]:
        return core.LNode([rad.NOINT])

    @property
    @rad.field
    def led_bank2_bank1_number_on(self: rad.Node) -> core.LNode[int]:
        return core.LNode([rad.NOINT])

    @property
    @rad.field
    def led_bank1_approx_wlen(self: rad.Node) -> Quantity:
        return Quantity(np.zeros(6, dtype=np.float64), unit=nm, dtype=np.float64)

    @property
    @rad.field
    def led_bank2_approx_wlen(self: rad.Node) -> Quantity:
        return Quantity(np.zeros(6, dtype=np.float64), unit=nm, dtype=np.float64)

    @property
    @rad.field
    def srcs_pd_voltage(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def srcs_led_flux(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def wfi_mce_srcs_bank1_led_i(self: rad.Node) -> Quantity:
        return Quantity(np.zeros(6, dtype=np.float64), unit=A, dtype=np.float64)

    @property
    @rad.field
    def wfi_mce_srcs_bank1_led_range(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def wfi_mce_srcs_bank2_led_i(self: rad.Node) -> Quantity:
        return Quantity(np.zeros(6, dtype=np.float64), unit=A, dtype=np.float64)

    @property
    @rad.field
    def wfi_mce_srcs_bank2_led_range(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def srcs_led_current(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def wfi_opt_targettype(self: rad.Node) -> TvacGroundtestWfiOptTargettypeEntry:
        return TvacGroundtestWfiOptTargettypeEntry.FLAT_SRCS

    @property
    @rad.field
    def analysis_tag(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def gsorc_pose_mode(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def gsorc_pose_target(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def gsorc_sds_active_atten(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def gsorc_sds_lltfir_wave(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def gsorc_sds_sorc_on(self: rad.Node) -> bool:
        return False

    @property
    @rad.field
    def gsorc_sds_sorc_wlen(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def gsorc_sds_active_source(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def gsorc_sds_dq_pulse(self: rad.Node) -> TvacGroundtestGsorcSdsDqPulseEntry:
        return TvacGroundtestGsorcSdsDqPulseEntry.PULSE

    @property
    @rad.field
    def gsorc_sds_daq_pw(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, ms)

    @property
    @rad.field
    def gsorc_heater1_setpt(self: rad.Node) -> float:
        return rad.NONUM

    @property
    @rad.field
    def wfi_otp_wfi_ewa(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def sca_temp(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, K)

    @property
    @rad.field
    def mpa_temp(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, K)

    @property
    @rad.field
    def ewa_temp(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, K)

    @property
    @rad.field
    def ewta_outer_heater_temp(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, K)

    @property
    @rad.field
    def ewta_inner_heater_temp(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, K)

    @property
    @rad.field
    def coba_temp_near_ewta(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, K)

    @property
    @rad.field
    def scea_temp(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, K)

    @property
    @rad.field
    def wfi_sce_1_vbiasgate_v(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, V)

    @property
    @rad.field
    def wfi_sce_1_vbiaspwr_i(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, A)

    @property
    @rad.field
    def wfi_sce_1_vbiaspwr_v(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, V)

    @property
    @rad.field
    def wfi_sce_1_vreset_v(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, V)

    @property
    @rad.field
    def wfi_sce_1_vreset_i(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, A)

    @property
    @rad.field
    def wfi_mcu_a_offs_csense_fpssen(self: rad.Node) -> Quantity:
        return Quantity(rad.NONUM, K)
