from types import MappingProxyType

import numpy as np
from astropy import units as u
from astropy.time import Time

from roman_datamodels.stnode import rad

__all__ = ["FpsGroundtest"]


class FpsGroundtest(rad.TaggedObjectNode):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/groundtest-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/fps/groundtest-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/fps/groundtest-1.0.0"
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