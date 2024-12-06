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
    @classmethod
    def asdf_schema_uri(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/schemas/fps/basic-1.0.0"

    @_core.rad_field
    def calibration_software_version(self) -> FpsCalibrationSoftwareVersion:
        return self._get_node("calibration_software_version", lambda: FpsCalibrationSoftwareVersion("9.9.0"))

    @_core.rad_field
    def filename(self) -> FpsFilename:
        return self._get_node("filename", lambda: FpsFilename(_default.NOFN))

    @_core.rad_field
    def file_date(self) -> FpsFileDate:
        return self._get_node("file_date", lambda: FpsFileDate(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")))

    @_core.rad_field
    def model_type(self) -> FpsModelType:
        return self._get_node("model_type", lambda: FpsModelType(_default.NOSTR))

    @_core.rad_field
    def origin(self) -> FpsOrigin:
        return self._get_node("origin", FpsOrigin.STSCI)

    @_core.rad_field
    def prd_software_version(self) -> FpsPrdSoftwareVersion:
        return self._get_node("prd_software_version", lambda: FpsPrdSoftwareVersion("8.8.8"))

    @_core.rad_field
    def sdf_software_version(self) -> FpsSdfSoftwareVersion:
        return self._get_node("sdf_software_version", lambda: FpsSdfSoftwareVersion("7.7.7"))

    @_core.rad_field
    def telescope(self) -> FpsTelescope:
        return self._get_node("telescope", FpsTelescope.ROMAN)
