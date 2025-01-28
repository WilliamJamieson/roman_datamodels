from typing import TypeAlias, TypeVar

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

_T = TypeVar("_T")

_TvacBasic: TypeAlias = (
    TvacCalibrationSoftwareVersion
    | TvacFileDate
    | TvacFilename
    | TvacModelType
    | TvacOrigin
    | TvacPrdSoftwareVersion
    | TvacSdfSoftwareVersion
    | TvacTelescope
)


class TvacBasic(rad.SchemaObjectNode[_TvacBasic | _T]):
    @classmethod
    def asdf_schema_uris(self) -> tuple[str]:
        return ("asdf://stsci.edu/datamodels/roman/schemas/tvac/basic-1.0.0",)

    @rad.field
    def calibration_software_version(self) -> TvacCalibrationSoftwareVersion:
        return TvacCalibrationSoftwareVersion.default()

    @rad.field
    def filename(self) -> TvacFilename:
        return TvacFilename.default()

    @rad.field
    def file_date(self) -> TvacFileDate:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return TvacFileDate.default()

    @rad.field
    def model_type(self) -> TvacModelType:
        from roman_datamodels.stnode import RDM_NODE_REGISTRY

        if isinstance(self, rad.ImpliedNodeMixin):
            return TvacModelType(RDM_NODE_REGISTRY.node_datamodel_mapping[self.asdf_implied_by()].__name__)
        else:
            return TvacModelType.default()

    @rad.field
    def origin(self) -> TvacOrigin:
        return TvacOrigin.default()

    @rad.field
    def prd_software_version(self) -> TvacPrdSoftwareVersion:
        return TvacPrdSoftwareVersion.default()

    @rad.field
    def sdf_software_version(self) -> TvacSdfSoftwareVersion:
        return TvacSdfSoftwareVersion.default()

    @rad.field
    def telescope(self) -> TvacTelescope:
        return TvacTelescope.default()
