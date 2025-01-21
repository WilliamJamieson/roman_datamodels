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

    @property
    @rad.field
    def calibration_software_version(self: rad.Node) -> TvacCalibrationSoftwareVersion:
        return TvacCalibrationSoftwareVersion.default()

    @property
    @rad.field
    def filename(self: rad.Node) -> TvacFilename:
        return TvacFilename.default()

    @property
    @rad.field
    def file_date(self: rad.Node) -> TvacFileDate:
        # Astropy has not implemented type hints for Time so MyPy will complain about this
        # until they do.
        return TvacFileDate.default()  # type: ignore[no-any-return]

    @property
    @rad.field
    def model_type(self: rad.Node) -> TvacModelType:
        from roman_datamodels.stnode import RDM_NODE_REGISTRY

        if isinstance(self, rad.ImpliedNodeMixin):
            return TvacModelType(RDM_NODE_REGISTRY.node_datamodel_mapping[self.asdf_implied_by()].__name__)
        else:
            return TvacModelType.default()

    @property
    @rad.field
    def origin(self: rad.Node) -> TvacOrigin:
        return TvacOrigin.default()

    @property
    @rad.field
    def prd_software_version(self: rad.Node) -> TvacPrdSoftwareVersion:
        return TvacPrdSoftwareVersion.default()

    @property
    @rad.field
    def sdf_software_version(self: rad.Node) -> TvacSdfSoftwareVersion:
        return TvacSdfSoftwareVersion.default()

    @property
    @rad.field
    def telescope(self: rad.Node) -> TvacTelescope:
        return TvacTelescope.default()
