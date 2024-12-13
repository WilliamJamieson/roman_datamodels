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
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/basic-1.0.0",)

    @rad.field
    def calibration_software_version(self) -> FpsCalibrationSoftwareVersion:
        return self._get_node("calibration_software_version", FpsCalibrationSoftwareVersion.default)

    @rad.field
    def filename(self) -> FpsFilename:
        return self._get_node("filename", FpsFilename.default)

    @rad.field
    def file_date(self) -> FpsFileDate:
        return self._get_node("file_date", FpsFileDate.default)

    @rad.field
    def model_type(self) -> FpsModelType:
        def _default():
            from roman_datamodels.stnode import RDM_NODE_REGISTRY

            if isinstance(self, rad.ImpliedNodeMixin):
                return FpsModelType(RDM_NODE_REGISTRY.node_datamodel_mapping[self.asdf_implied_by()].__name__)
            else:
                return FpsModelType.default()

        return self._get_node("model_type", _default)

    @rad.field
    def origin(self) -> FpsOrigin:
        return self._get_node("origin", FpsOrigin.default)

    @rad.field
    def prd_software_version(self) -> FpsPrdSoftwareVersion:
        return self._get_node("prd_software_version", FpsPrdSoftwareVersion.default)

    @rad.field
    def sdf_software_version(self) -> FpsSdfSoftwareVersion:
        return self._get_node("sdf_software_version", FpsSdfSoftwareVersion.default)

    @rad.field
    def telescope(self) -> FpsTelescope:
        return self._get_node("telescope", FpsTelescope.default)
