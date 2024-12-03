from astropy.time import Time

from roman_datamodels.stnode import _core, _default

from .tagged_scalars import (
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


class Basic(_core.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/basic-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
        return (
            "calibration_software_name",
            "calibration_software_version",
            "filename",
            "file_date",
            "model_type",
            "origin",
            "prd_version",
            "sdf_software_version",
            "telescope",
        )

    @property
    def calibration_software_name(self) -> CalibrationSoftwareName:
        return self._get_node("calibration_software_name", lambda: CalibrationSoftwareName("RomanCAL"))

    @property
    def calibration_software_version(self) -> CalibrationSoftwareVersion:
        return self._get_node("calibration_software_version", lambda: CalibrationSoftwareVersion("9.9.0"))

    @property
    def product_type(self) -> ProductType:
        return self._get_node("product_type", lambda: ProductType("l2"))

    @property
    def filename(self) -> Filename:
        return self._get_node("filename", lambda: Filename(_default.NOFN))

    @property
    def file_date(self) -> FileDate:
        return self._get_node("file_date", lambda: FileDate(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")))

    @property
    def model_type(self) -> ModelType:
        return self._get_node("model_type", lambda: ModelType(_default.NOSTR))

    @property
    def origin(self) -> Origin:
        return self._get_node("origin", Origin.STSCI_SOC)

    @property
    def prd_version(self) -> PrdVersion:
        return self._get_node("prd_version", lambda: PrdVersion("8.8.8"))

    @property
    def sdf_software_version(self) -> SdfSoftwareVersion:
        return self._get_node("sdf_software_version", lambda: SdfSoftwareVersion("7.7.7"))

    @property
    def telescope(self) -> Telescope:
        return self._get_node("telescope", Telescope.ROMAN)
