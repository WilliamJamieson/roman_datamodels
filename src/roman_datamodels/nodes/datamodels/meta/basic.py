from astropy.time import Time

from roman_datamodels.stnode import rad

from .scalars import (
    CalibrationSoftwareName,
    CalibrationSoftwareVersion,
    FileDate,
    Filename,
    ModelType,
    Origin,
    PrdVersion,
    ProductType,
    SdfSoftwareVersion,
    Telescope,
)

__all__ = ["Basic"]


class Basic(rad.SchemaObjectNode):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/basic-1.0.0",)

    @rad.field
    def calibration_software_name(self) -> CalibrationSoftwareName:
        return self._get_node("calibration_software_name", lambda: CalibrationSoftwareName("RomanCAL"))

    @rad.field
    def calibration_software_version(self) -> CalibrationSoftwareVersion:
        return self._get_node("calibration_software_version", lambda: CalibrationSoftwareVersion("9.9.0"))

    @rad.field
    def product_type(self) -> ProductType:
        return self._get_node("product_type", lambda: ProductType("l2"))

    @rad.field
    def filename(self) -> Filename:
        return self._get_node("filename", lambda: Filename(rad.NOFN))

    @rad.field
    def file_date(self) -> FileDate:
        return self._get_node("file_date", lambda: FileDate(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")))

    @rad.field
    def model_type(self) -> ModelType:
        return self._get_node("model_type", lambda: ModelType(rad.NOSTR))

    @rad.field
    def origin(self) -> Origin:
        return self._get_node("origin", lambda: Origin.STSCI_SOC)

    @rad.field
    def prd_version(self) -> PrdVersion:
        return self._get_node("prd_version", lambda: PrdVersion("8.8.8"))

    @rad.field
    def sdf_software_version(self) -> SdfSoftwareVersion:
        return self._get_node("sdf_software_version", lambda: SdfSoftwareVersion("7.7.7"))

    @rad.field
    def telescope(self) -> Telescope:
        return self._get_node("telescope", lambda: Telescope.ROMAN)
