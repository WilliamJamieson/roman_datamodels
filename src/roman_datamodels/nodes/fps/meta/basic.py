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

    @rad.field
    def calibration_software_version(self) -> FpsCalibrationSoftwareVersion:
        return FpsCalibrationSoftwareVersion.default()

    @rad.field
    def filename(self) -> FpsFilename:
        return FpsFilename.default()

    @rad.field
    def file_date(self) -> FpsFileDate:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return FpsFileDate.default()

    @rad.field
    def model_type(self) -> FpsModelType:
        from roman_datamodels.stnode import RDM_NODE_REGISTRY

        if isinstance(self, rad.ImpliedNodeMixin):
            return FpsModelType(RDM_NODE_REGISTRY.node_datamodel_mapping[self.asdf_implied_by()].__name__)
        else:
            return FpsModelType.default()

    @rad.field
    def origin(self) -> FpsOrigin:
        return FpsOrigin.default()

    @rad.field
    def prd_software_version(self) -> FpsPrdSoftwareVersion:
        return FpsPrdSoftwareVersion.default()

    @rad.field
    def sdf_software_version(self) -> FpsSdfSoftwareVersion:
        return FpsSdfSoftwareVersion.default()

    @rad.field
    def telescope(self) -> FpsTelescope:
        return FpsTelescope.default()
