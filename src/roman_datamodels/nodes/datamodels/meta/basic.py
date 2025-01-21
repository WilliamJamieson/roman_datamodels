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

    @property
    @rad.field
    def calibration_software_name(self: rad.Node) -> CalibrationSoftwareName:
        return CalibrationSoftwareName.default()

    @property
    @rad.field
    def calibration_software_version(self: rad.Node) -> CalibrationSoftwareVersion:
        return CalibrationSoftwareVersion.default()

    @property
    @rad.field
    def product_type(self: rad.Node) -> ProductType:
        return ProductType.default()

    @property
    @rad.field
    def filename(self: rad.Node) -> Filename:
        return Filename.default()

    @property
    @rad.field
    def file_date(self: rad.Node) -> FileDate:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return FileDate.default()  # type: ignore[no-any-return]

    @property
    @rad.field
    def model_type(self: rad.Node) -> ModelType:
        from roman_datamodels.stnode import RDM_NODE_REGISTRY

        if isinstance(self, rad.ImpliedNodeMixin):
            return ModelType(RDM_NODE_REGISTRY.node_datamodel_mapping[self.asdf_implied_by()].__name__)
        else:
            return ModelType.default()

    @property
    @rad.field
    def origin(self: rad.Node) -> Origin:
        return Origin.default()

    @property
    @rad.field
    def prd_version(self: rad.Node) -> PrdVersion:
        return PrdVersion.default()

    @property
    @rad.field
    def sdf_software_version(self: rad.Node) -> SdfSoftwareVersion:
        return SdfSoftwareVersion.default()

    @property
    @rad.field
    def telescope(self: rad.Node) -> Telescope:
        return Telescope.default()
