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
        return self._get_node("calibration_software_name", CalibrationSoftwareName.default)

    @rad.field
    def calibration_software_version(self) -> CalibrationSoftwareVersion:
        return self._get_node("calibration_software_version", CalibrationSoftwareVersion.default)

    @rad.field
    def product_type(self) -> ProductType:
        return self._get_node("product_type", ProductType.default)

    @rad.field
    def filename(self) -> Filename:
        return self._get_node("filename", Filename.default)

    @rad.field
    def file_date(self) -> FileDate:
        return self._get_node("file_date", FileDate.default)

    @rad.field
    def model_type(self) -> ModelType:
        def _default():
            from roman_datamodels.stnode import RDM_NODE_REGISTRY

            if isinstance(self, rad.ImpliedNodeMixin):
                return ModelType(RDM_NODE_REGISTRY.node_datamodel_mapping[self.asdf_implied_by()].__name__)
            else:
                return ModelType.default()

        return self._get_node("model_type", _default)

    @rad.field
    def origin(self) -> Origin:
        return self._get_node("origin", Origin.default)

    @rad.field
    def prd_version(self) -> PrdVersion:
        return self._get_node("prd_version", PrdVersion.default)

    @rad.field
    def sdf_software_version(self) -> SdfSoftwareVersion:
        return self._get_node("sdf_software_version", SdfSoftwareVersion.default)

    @rad.field
    def telescope(self) -> Telescope:
        return self._get_node("telescope", Telescope.default)
