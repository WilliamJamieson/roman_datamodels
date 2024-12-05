import numpy as np
from astropy import units as u
from astropy.time import Time

from roman_datamodels.stnode import _core, _default

__all__ = ["FpsGroundtest"]


class FpsGroundtest(_core.TaggedObjectNode):
    """
    FPS Ground test description.
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/groundtest-1.0.0"

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
        return self._get_node("readout_col_num", lambda: _default.NOINT)

    @property
    def detector_pixel_size(self) -> u.Quantity:
        return self._get_node(
            "detector_pixel_size", lambda: u.Quantity(np.zeros(6, dtype=np.float64), unit=u.cm, dtype=np.float64)
        )

    @property
    def sensor_error(self) -> np.ndarray:
        return self._get_node("sensor_error", lambda: np.zeros(6, dtype=np.float64))
