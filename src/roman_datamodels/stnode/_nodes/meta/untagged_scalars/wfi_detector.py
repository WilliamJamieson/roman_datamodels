from __future__ import annotations

from roman_datamodels.stnode import _core

__all__ = ["WfiDetector"]


class WfiDetector(str, _core.SchemaScalarNode):
    """
    WFI Detector
    """

    @classmethod
    def WFI01(cls) -> WfiDetector:
        return cls("WFI01")

    @classmethod
    def WFI02(cls) -> WfiDetector:
        return cls("WFI02")

    @classmethod
    def WFI03(cls) -> WfiDetector:
        return cls("WFI03")

    @classmethod
    def WFI04(cls) -> WfiDetector:
        return cls("WFI04")

    @classmethod
    def WFI05(cls) -> WfiDetector:
        return cls("WFI05")

    @classmethod
    def WFI06(cls) -> WfiDetector:
        return cls("WFI06")

    @classmethod
    def WFI07(cls) -> WfiDetector:
        return cls("WFI07")

    @classmethod
    def WFI08(cls) -> WfiDetector:
        return cls("WFI08")

    @classmethod
    def WFI09(cls) -> WfiDetector:
        return cls("WFI09")

    @classmethod
    def WFI10(cls) -> WfiDetector:
        return cls("WFI10")

    @classmethod
    def WFI11(cls) -> WfiDetector:
        return cls("WFI11")

    @classmethod
    def WFI12(cls) -> WfiDetector:
        return cls("WFI12")

    @classmethod
    def WFI13(cls) -> WfiDetector:
        return cls("WFI13")

    @classmethod
    def WFI14(cls) -> WfiDetector:
        return cls("WFI14")

    @classmethod
    def WFI15(cls) -> WfiDetector:
        return cls("WFI15")

    @classmethod
    def WFI16(cls) -> WfiDetector:
        return cls("WFI16")

    @classmethod
    def WFI17(cls) -> WfiDetector:
        return cls("WFI17")

    @classmethod
    def WFI18(cls) -> WfiDetector:
        return cls("WFI18")

    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/wfi_detector-1.0.0"
