from astropy.time import Time

from roman_datamodels.stnode import _core

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


class Basic(_core.SchemaNode):
    @property
    def schema_uri(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/basic-1.0.0"

    @property
    def required(self) -> tuple[str]:
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
        # add a default value if necessary
        if not self._has_node("calibration_software_name"):
            self.calibration_software_name = CalibrationSoftwareName("RomanCAL")

        return self._get_node("calibration_software_name")

    @property
    def calibration_software_version(self) -> CalibrationSoftwareVersion:
        if not self._has_node("calibration_software_version"):
            self.calibration_software_version = CalibrationSoftwareVersion("9.9.0")

        return self._get_node("calibration_software_version")

    @property
    def product_type(self) -> ProductType:
        if not self._has_node("product_type"):
            self.product_type = ProductType("l2")

        return self._get_node("product_type")

    @property
    def filename(self) -> Filename:
        if not self._has_node("filename"):
            self.filename = Filename(_core.NOFN)
        return self._get_node("filename")

    @property
    def file_date(self) -> FileDate:
        if not self._has_node("file_date"):
            self.file_date = FileDate(Time("2020-01-01T00:00:00.0", format="isot", scale="utc"))

        return self._get_node("file_date")

    @property
    def model_type(self) -> ModelType:
        if not self._has_node("model_type"):
            self.model_type = ModelType(_core.NOSTR)

        return self._get_node("model_type")

    @property
    def origin(self) -> Origin:
        if not self._has_node("origin"):
            self.origin = Origin.STSCI_SOC()

        return self._get_node("origin")

    @property
    def prd_version(self) -> PrdVersion:
        if not self._has_node("prd_version"):
            self.prd_version = PrdVersion("8.8.8")

        return self._get_node("prd_version")

    @property
    def sdf_software_version(self) -> SdfSoftwareVersion:
        if not self._has_node("sdf_software_version"):
            self.sdf_software_version = SdfSoftwareVersion("7.7.7")

        return self._get_node("sdf_software_version")

    @property
    def telescope(self) -> Telescope:
        if not self._has_node("telescope"):
            self.telescope = Telescope.ROMAN()

        return self._get_node("telescope")
