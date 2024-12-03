from astropy import units as u

from roman_datamodels.stnode import _core

from ..meta import OPTICAL_ELEMENTS
from .ref import RefCommonRef

__all__ = ["WfiImgPhotomRef"]


class WfiImgPhotomRefMeta(RefCommonRef):
    @property
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "PHOTOM")


class WfiImgPhotomRefPhotTableEntry(_core.ObjectNode):
    @classmethod
    def no_phot(cls) -> "WfiImgPhotomRefPhotTableEntry":
        return cls(
            {
                "photmjsr": None,
                "uncertainty": None,
            }
        )

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "photmjsr",
            "uncertainty",
            "pixelareasr",
        )

    @property
    def photmjsr(self) -> u.Quantity | None:
        return self._get_node("photmjsr", lambda: 1.0e-15 * u.megajansky / u.steradian)

    @property
    def uncertainty(self) -> u.Quantity | None:
        return self._get_node("uncertainty", lambda: 1.0e-16 * u.megajansky / u.steradian)

    @property
    def pixelareasr(self) -> u.Quantity | None:
        return self._get_node("pixelareasr", lambda: 1.0e-13 * u.steradia)


class WfiImgPhotomRef(_core.DataModelNode):
    """
    WFI imaging photometric flux conversion data model
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/wfi_img_photom-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "meta",
            "phot_table",
        )

    @property
    def array_data(self) -> tuple[int]:
        raise NotImplementedError("array_data is not implemented")

    @property
    def meta(self) -> WfiImgPhotomRefMeta:
        return self._get_node("meta", WfiImgPhotomRefMeta)

    @property
    def phot_table(self) -> dict[str, WfiImgPhotomRefPhotTableEntry]:
        def _default():
            table = {}
            for element in OPTICAL_ELEMENTS:
                if element in ("GRISM", "PRISM", "DARK"):
                    table[element] = WfiImgPhotomRefPhotTableEntry.no_phot()
                else:
                    table[element] = WfiImgPhotomRefPhotTableEntry()
            return table

        return self._get_node("phot_table", _default)
