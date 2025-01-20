from typing import TypeAlias, TypeVar

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

_T = TypeVar("_T")

_FpsBasic: TypeAlias = (
    FpsCalibrationSoftwareVersion
    | FpsFileDate
    | FpsFilename
    | FpsModelType
    | FpsOrigin
    | FpsPrdSoftwareVersion
    | FpsSdfSoftwareVersion
    | FpsTelescope
)


class FpsBasic(rad.SchemaObjectNode[_FpsBasic | _T]):
    @classmethod
    def asdf_schema_uris(cls) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/fps/basic-1.0.0",)

    @property
    @rad.field
    def calibration_software_version(self: rad.Node) -> FpsCalibrationSoftwareVersion:
        return FpsCalibrationSoftwareVersion.default()

    @property
    @rad.field
    def filename(self: rad.Node) -> FpsFilename:
        return FpsFilename.default()

    @property
    @rad.field
    def file_date(self: rad.Node) -> FpsFileDate:
        return FpsFileDate.default()

    @property
    @rad.field
    def model_type(self: rad.Node) -> FpsModelType:
        from roman_datamodels.stnode import RDM_NODE_REGISTRY

        if isinstance(self, rad.ImpliedNodeMixin):
            return FpsModelType(RDM_NODE_REGISTRY.node_datamodel_mapping[self.asdf_implied_by()].__name__)
        else:
            return FpsModelType.default()

    @property
    @rad.field
    def origin(self: rad.Node) -> FpsOrigin:
        return FpsOrigin.default()

    @property
    @rad.field
    def prd_software_version(self: rad.Node) -> FpsPrdSoftwareVersion:
        return FpsPrdSoftwareVersion.default()

    @property
    @rad.field
    def sdf_software_version(self: rad.Node) -> FpsSdfSoftwareVersion:
        return FpsSdfSoftwareVersion.default()

    @property
    @rad.field
    def telescope(self: rad.Node) -> FpsTelescope:
        return FpsTelescope.default()
