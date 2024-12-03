from astropy.time import Time

from roman_datamodels.stnode import _core, _default

from .tagged_scalars import (
    FpsCalibrationSoftwareVersion,
    FpsFileDate,
    FpsFilename,
    FpsModelType,
    FpsOrigin,
    FpsPrdSoftwareVersion,
    FpsSdfSoftwareVersion,
    FpsTelescope,
)

__all__ = ["FpsBasic"]


class FpsBasic(_core.SchemaObjectNode):
    @property
    def schema_uri(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/basic-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "calibration_software_version",
            "filename",
            "file_date",
            "model_type",
            "origin",
            "prd_software_version",
            "sdf_software_version",
            "telescope",
        )

    @property
    def calibration_software_version(self) -> FpsCalibrationSoftwareVersion:
        return self._get_node("calibration_software_version", lambda: FpsCalibrationSoftwareVersion("9.9.0"))

    @property
    def filename(self) -> FpsFilename:
        return self._get_node("filename", lambda: FpsFilename(_default.NOFN))

    @property
    def file_date(self) -> FpsFileDate:
        return self._get_node("file_date", lambda: FpsFileDate(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")))

    @property
    def model_type(self) -> FpsModelType:
        return self._get_node("model_type", lambda: FpsModelType(_default.NOSTR))

    @property
    def origin(self) -> FpsOrigin:
        return self._get_node("origin", FpsOrigin.STSCI)

    @property
    def prd_software_version(self) -> FpsPrdSoftwareVersion:
        return self._get_node("prd_version", lambda: FpsPrdSoftwareVersion("8.8.8"))

    @property
    def sdf_software_version(self) -> FpsSdfSoftwareVersion:
        return self._get_node("sdf_software_version", lambda: FpsSdfSoftwareVersion("7.7.7"))

    @property
    def telescope(self) -> FpsTelescope:
        return self._get_node("telescope", FpsTelescope.ROMAN)
