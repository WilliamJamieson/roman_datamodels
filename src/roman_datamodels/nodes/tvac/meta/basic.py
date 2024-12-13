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
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/basic-1.0.0",)

    @rad.field
    def calibration_software_version(self) -> TvacCalibrationSoftwareVersion:
        return self._get_node("calibration_software_version", TvacCalibrationSoftwareVersion.default)

    @rad.field
    def filename(self) -> TvacFilename:
        return self._get_node("filename", TvacFilename.default)

    @rad.field
    def file_date(self) -> TvacFileDate:
        return self._get_node("file_date", TvacFileDate.default)

    @rad.field
    def model_type(self) -> TvacModelType:
        def _default():
            from roman_datamodels.stnode import RDM_NODE_REGISTRY

            if isinstance(self, rad.ImpliedNodeMixin):
                return TvacModelType(RDM_NODE_REGISTRY.node_datamodel_mapping[self.asdf_implied_by()].__name__)
            else:
                return TvacModelType.default()

        return self._get_node("model_type", _default)

    @rad.field
    def origin(self) -> TvacOrigin:
        return self._get_node("origin", TvacOrigin.default)

    @rad.field
    def prd_software_version(self) -> TvacPrdSoftwareVersion:
        return self._get_node("prd_software_version", TvacPrdSoftwareVersion.default)

    @rad.field
    def sdf_software_version(self) -> TvacSdfSoftwareVersion:
        return self._get_node("sdf_software_version", TvacSdfSoftwareVersion.default)

    @rad.field
    def telescope(self) -> TvacTelescope:
        return self._get_node("telescope", TvacTelescope.default)
