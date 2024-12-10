from astropy.time import Time

from roman_datamodels.stnode import rad

from .scalars import (
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


class TvacBasic(rad.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/tvac/basic-1.0.0"

    @rad.field
    def calibration_software_version(self) -> TvacCalibrationSoftwareVersion:
        return self._get_node("calibration_software_version", lambda: TvacCalibrationSoftwareVersion("9.9.0"))

    @rad.field
    def filename(self) -> TvacFilename:
        return self._get_node("filename", lambda: TvacFilename(rad.NOSTR))

    @rad.field
    def file_date(self) -> TvacFileDate:
        return self._get_node("file_date", lambda: TvacFileDate(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")))

    @rad.field
    def model_type(self) -> TvacModelType:
        return self._get_node("model_type", lambda: TvacModelType(rad.NOSTR))

    @rad.field
    def origin(self) -> TvacOrigin:
        return self._get_node("origin", lambda: TvacOrigin.STSCI)

    @rad.field
    def prd_software_version(self) -> TvacPrdSoftwareVersion:
        return self._get_node("prd_software_version", lambda: TvacPrdSoftwareVersion("8.8.8"))

    @rad.field
    def sdf_software_version(self) -> TvacSdfSoftwareVersion:
        return self._get_node("sdf_software_version", lambda: TvacSdfSoftwareVersion("7.7.7"))

    @rad.field
    def telescope(self) -> TvacTelescope:
        return self._get_node("telescope", lambda: TvacTelescope.ROMAN)
