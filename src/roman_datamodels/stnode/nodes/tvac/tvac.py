import numpy as np
from astropy import units as u

from roman_datamodels.stnode import rad

from .meta import (
    TvacCommon,
    TvacGroundtest,
)

__all__ = ["Tvac"]


class Tvac_Meta(rad.ImpliedNodeMixin, TvacCommon):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return Tvac

    @rad.field
    def groundtest(self) -> TvacGroundtest:
        return self._get_node("groundtest", TvacGroundtest)


class Tvac(rad.TaggedObjectNode, rad.ArrayFieldMixin):
    """
    Tvac test data
    """

    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac-1.0.0",)

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/tvac-1.0.0"

    @property
    def default_array_shape(self) -> tuple[int]:
        return (8, 4096, 4096)

    @property
    def testing_array_shape(self) -> tuple[int]:
        return (8, 8, 8)

    @rad.field
    def meta(self) -> Tvac_Meta:
        return self._get_node("meta", Tvac_Meta)

    @rad.field
    def data(self) -> u.Quantity:
        return self._get_node("data", lambda: u.Quantity(np.zeros(self.array_shape, dtype=np.uint16), unit=u.DN, dtype=np.uint16))

    @rad.field
    def amp33(self) -> u.Quantity:
        return self._get_node(
            "amp33",
            lambda: u.Quantity(
                np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16
            ),
        )

    @rad.field
    def amp33_reset_reads(self) -> u.Quantity:
        return self._get_node(
            "amp33_reset_reads",
            lambda: u.Quantity(
                np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16
            ),
        )

    @rad.field
    def amp33_reference_read(self) -> u.Quantity:
        return self._get_node(
            "amp33_reference_read",
            lambda: u.Quantity(
                np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16
            ),
        )

    @rad.field
    def guidewindow(self) -> u.Quantity:
        return self._get_node(
            "guidewindow",
            lambda: u.Quantity(
                np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16
            ),
        )

    @rad.field
    def reference_read(self) -> u.Quantity:
        return self._get_node(
            "reference_read",
            lambda: u.Quantity(
                np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16
            ),
        )

    @rad.field
    def reset_reads(self) -> u.Quantity:
        return self._get_node(
            "reset_reads",
            lambda: u.Quantity(
                np.zeros((self.array_shape[0], self.array_shape[1], 128), dtype=np.uint16), unit=u.DN, dtype=np.uint16
            ),
        )
