from types import MappingProxyType
from typing import TypeAlias

import numpy as np
import numpy.typing as npt
from astropy.time import Time
from astropy.units import Quantity, cm  # type: ignore[attr-defined]

from roman_datamodels.stnode import rad

__all__ = ["FpsGroundtest"]


_FpsGroundtest: TypeAlias = npt.NDArray[np.float64] | Quantity | Time | str | bool | int


class FpsGroundtest(rad.TaggedObjectNode[_FpsGroundtest]):
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
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

    @property
    @rad.field
    def product_version(self: rad.Node) -> str:
        return rad.NOSTR

    @property
    @rad.field
    def conversion_date(self: rad.Node) -> Time:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return Time("2020-01-01T00:00:00.0", format="isot", scale="utc")  # type: ignore[no-untyped-call]

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
