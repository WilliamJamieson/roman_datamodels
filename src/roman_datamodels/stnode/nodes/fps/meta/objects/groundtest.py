import numpy as np
from astropy import units as u
from astropy.time import Time

from roman_datamodels.stnode import rad

__all__ = ["FpsGroundtest"]


class FpsGroundtest(rad.TaggedObjectNode):
    """
    FPS Ground test description.
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/groundtest-1.0.0",)

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/fps/groundtest-1.0.0"

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
