from typing import TypeAlias, TypeVar

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

# So that when we inherit from this we can include it's parts too
_T = TypeVar("_T")

_Basic: TypeAlias = (
    CalibrationSoftwareName
    | CalibrationSoftwareVersion
    | FileDate
    | Filename
    | ModelType
    | Origin
    | PrdVersion
    | ProductType
    | SdfSoftwareVersion
    | Telescope
)


class Basic(rad.SchemaObjectNode[_Basic | _T]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/basic-1.0.0",)

    @rad.field
    def calibration_software_name(self) -> CalibrationSoftwareName:
        return CalibrationSoftwareName.default()

    @rad.field
    def calibration_software_version(self) -> CalibrationSoftwareVersion:
        return CalibrationSoftwareVersion.default()

    @rad.field
    def product_type(self) -> ProductType:
        return ProductType.default()

    @rad.field
    def filename(self) -> Filename:
        return Filename.default()

    @rad.field
    def file_date(self) -> FileDate:
        return FileDate.default()

    @rad.field
    def model_type(self) -> ModelType:
        from roman_datamodels.stnode import RDM_NODE_REGISTRY

        if isinstance(self, rad.ImpliedNodeMixin):
            return ModelType(RDM_NODE_REGISTRY.node_datamodel_mapping[self.asdf_implied_by()].__name__)
        else:
            return ModelType.default()

    @rad.field
    def origin(self) -> Origin:
        return Origin.default()

    @rad.field
    def prd_version(self) -> PrdVersion:
        return PrdVersion.default()

    @rad.field
    def sdf_software_version(self) -> SdfSoftwareVersion:
        return SdfSoftwareVersion.default()

    @rad.field
    def telescope(self) -> Telescope:
        return Telescope.default()
