from astropy.time import Time

from roman_datamodels.stnode import _core, _default

from .tagged_scalars import (
    TvacCalibrationSoftwareVersion,
    TvacFileDate,
    TvacFilename,
    TvacModelType,
    TvacOrigin,
    TvacPrdSoftwareVersion,
    TvacSdfSoftwareVersion,
    TvacTelescope,
)

__all__ = ["TvacBasic"]


class TvacBasic(_core.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/basic-1.0.0"

    @classmethod
    def asdf_required(cls) -> tuple[str]:
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
    def calibration_software_version(self) -> TvacCalibrationSoftwareVersion:
        return self._get_node("calibration_software_version", lambda: TvacCalibrationSoftwareVersion("9.9.0"))

    @property
    def filename(self) -> TvacFilename:
        return self._get_node("filename", lambda: TvacFilename(_default.NOSTR))

    @property
    def file_date(self) -> TvacFileDate:
        return self._get_node("file_date", lambda: TvacFileDate(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")))

    @property
    def model_type(self) -> TvacModelType:
        return self._get_node("model_type", lambda: TvacModelType(_default.NOSTR))

    @property
    def origin(self) -> TvacOrigin:
        return self._get_node("origin", TvacOrigin.STSCI)

    @property
    def prd_software_version(self) -> TvacPrdSoftwareVersion:
        return self._get_node("prd_version", lambda: TvacPrdSoftwareVersion("8.8.8"))

    @property
    def sdf_software_version(self) -> TvacSdfSoftwareVersion:
        return self._get_node("sdf_software_version", lambda: TvacSdfSoftwareVersion("7.7.7"))

    @property
    def telescope(self) -> TvacTelescope:
        return self._get_node("telescope", TvacTelescope.ROMAN)
