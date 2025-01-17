from types import MappingProxyType

from roman_datamodels.stnode import core, rad

from ..datamodels import OPTICAL_ELEMENTS
from .ref import RefCommonRef, RefTypeEntry

__all__ = ["WfiImgPhotomRef"]


class WfiImgPhotomRef_Meta(rad.ImpliedNodeMixin, RefCommonRef):
    @classmethod
    def asdf_implied_by(cls) -> type:
        return WfiImgPhotomRef

    @rad.field
    def reftype(self) -> RefTypeEntry:
        return RefTypeEntry.PHOTOM


class WfiImgPhotomRef_PhotTable(rad.ImpliedNodeMixin, rad.ObjectNode):
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

    @rad.field
    def photmjsr(self) -> float | None:
        return 1.0e-15

    @rad.field
    def uncertainty(self) -> float | None:
        return 1.0e-16

    @rad.field
    def pixelareasr(self) -> float | None:
        return 1.0e-13


class WfiImgPhotomRef_PhotTable_PatternNode(core.PatternDNode, rad.ImpliedNodeMixin):
    @classmethod
    def asdf_implied_by(cls):
        return WfiImgPhotomRef

    @classmethod
    def asdf_implied_property_name(cls) -> str:
        return "phot_table"

    @classmethod
    def asdf_key_pattern(cls):
        return "^(F062|F087|F106|F129|F146|F158|F184|F213|GRISM|PRISM|DARK)$"


class WfiImgPhotomRef(rad.TaggedObjectNode):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/reference_files/wfi_img_photom-1.0.0",)

    @classmethod
    def asdf_tag_uris(cls) -> MappingProxyType[str, str]:
        return MappingProxyType(
            {
                "asdf://stsci.edu/datamodels/roman/tags/reference_files/wfi_img_photom-1.0.0": "asdf://stsci.edu/datamodels/roman/schemas/reference_files/wfi_img_photom-1.0.0"
            }
        )

    @rad.field
    def meta(self) -> WfiImgPhotomRef_Meta:
        return WfiImgPhotomRef_Meta()

    # TODO: Add typeguard rule to fully handle this DNode annotation
    @rad.field
    def phot_table(self) -> WfiImgPhotomRef_PhotTable_PatternNode[str, WfiImgPhotomRef_PhotTable]:
        table = {}
        for element in OPTICAL_ELEMENTS:
            if element in ("GRISM", "PRISM", "DARK"):
                table[element] = WfiImgPhotomRef_PhotTable.no_phot()
            else:
                table[element] = WfiImgPhotomRef_PhotTable()
        return WfiImgPhotomRef_PhotTable_PatternNode(table)
