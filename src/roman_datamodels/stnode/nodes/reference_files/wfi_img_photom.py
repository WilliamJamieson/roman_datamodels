from astropy import units as u

from roman_datamodels.stnode import _base, _core

from ..meta import OPTICAL_ELEMENTS
from .ref import RefCommonRef

__all__ = ["WfiImgPhotomRef"]


class WfiImgPhotomRef_Meta(_core.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return WfiImgPhotomRef

    @_core.rad_field
    def reftype(self) -> str:
        return self._get_node("reftype", lambda: "PHOTOM")


class WfiImgPhotomRef_PhotTable(_core.ImpliedNodeMixin, _core.ObjectNode):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return WfiImgPhotomRef

    @classmethod
    def no_phot(cls) -> "WfiImgPhotomRef_PhotTable":
        return cls(
            {
                "photmjsr": None,
                "uncertainty": None,
            }
        )

    @_core.rad_field
    def photmjsr(self) -> u.Quantity | None:
        return self._get_node("photmjsr", lambda: 1.0e-15 * u.megajansky / u.steradian)

    @_core.rad_field
    def uncertainty(self) -> u.Quantity | None:
        return self._get_node("uncertainty", lambda: 1.0e-16 * u.megajansky / u.steradian)

    @_core.rad_field
    def pixelareasr(self) -> u.Quantity | None:
        return self._get_node("pixelareasr", lambda: 1.0e-13 * u.steradian)


class WfiImgPhotomRef(_core.DataModelNode):
    """
    WFI imaging photometric flux conversion data model
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/reference_files/wfi_img_photom-1.0.0"

    @property
    def array_shape(self) -> tuple[int]:
        raise NotImplementedError("array_data is not implemented")

    @_core.rad_field
    def meta(self) -> WfiImgPhotomRef_Meta:
        return self._get_node("meta", WfiImgPhotomRef_Meta)

    # TODO: Add typeguard rule to fully handle this DNode annotation
    @_core.rad_field
    def phot_table(self) -> _base.DNode[str, WfiImgPhotomRef_PhotTable]:
        def _default():
            table = {}
            for element in OPTICAL_ELEMENTS:
                if element in ("GRISM", "PRISM", "DARK"):
                    table[element] = WfiImgPhotomRef_PhotTable.no_phot()
                else:
                    table[element] = WfiImgPhotomRef_PhotTable()
            return _base.DNode(table)

        return self._get_node("phot_table", _default)
