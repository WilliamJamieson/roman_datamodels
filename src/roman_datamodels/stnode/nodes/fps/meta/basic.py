from astropy.time import Time

from roman_datamodels.stnode import rad

from .scalars import (
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


class FpsBasic(rad.SchemaObjectNode):
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/basic-1.0.0"

    @rad.field
    def calibration_software_version(self) -> FpsCalibrationSoftwareVersion:
        return self._get_node("calibration_software_version", lambda: FpsCalibrationSoftwareVersion("9.9.0"))

    @rad.field
    def filename(self) -> FpsFilename:
        return self._get_node("filename", lambda: FpsFilename(rad.NOFN))

    @rad.field
    def file_date(self) -> FpsFileDate:
        return self._get_node("file_date", lambda: FpsFileDate(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")))

    @rad.field
    def model_type(self) -> FpsModelType:
        return self._get_node("model_type", lambda: FpsModelType(rad.NOSTR))

    @rad.field
    def origin(self) -> FpsOrigin:
        return self._get_node("origin", lambda: FpsOrigin.STSCI)

    @rad.field
    def prd_software_version(self) -> FpsPrdSoftwareVersion:
        return self._get_node("prd_software_version", lambda: FpsPrdSoftwareVersion("8.8.8"))

    @rad.field
    def sdf_software_version(self) -> FpsSdfSoftwareVersion:
        return self._get_node("sdf_software_version", lambda: FpsSdfSoftwareVersion("7.7.7"))

    @rad.field
    def telescope(self) -> FpsTelescope:
        return self._get_node("telescope", lambda: FpsTelescope.ROMAN)
