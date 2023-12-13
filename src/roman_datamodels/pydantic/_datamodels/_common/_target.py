from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from roman_datamodels.pydantic import _archive, _core, _defaults, _strenum
from roman_datamodels.pydantic import _uri as uri

__all__ = ["Target"]


class target_type(_strenum.StrEnum):
    FIXED = "FIXED"
    MOVING = "MOVING"
    GENERIC = "GENERIC"


class source_type(_strenum.StrEnum):
    POINT = "POINT"
    EXTENDED = "EXTENDED"
    UNKNOWN = "UNKNOWN"


class Target(_core.BaseRomanTaggedModel):
    _uri: ClassVar = uri.asdf_uri.TARGET.value
    _tag_uri: ClassVar = uri.asdf_tag_uri.TARGET.value

    model_config = ConfigDict(
        title="Target information",
    )

    proposer_name: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Proposer's name for the target",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.target_name",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(100)",
                    destination=[
                        "ScienceCommon.proposer_target_name",
                        "GuideWindow.proposer_target_name",
                    ],
                ),
            ),
        ),
    ]
    catalog_name: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Standard astronomical catalog name for target",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.standard_target_name",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(256)",
                    destination=[
                        "ScienceCommon.catalog_name",
                        "GuideWindow.catalog_name",
                    ],
                ),
            ),
        ),
    ]
    type: Annotated[
        target_type,
        Field(
            default_factory=_defaults.default_constant_factory(target_type.FIXED.value),
            title="Type of target",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.target_type",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(10)",
                    destination=[
                        "ScienceCommon.target_type",
                        "GuideWindow.target_type",
                    ],
                ),
            ),
        ),
    ]
    ra: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Target RA at mid time of exposure",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.ra_computed",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.ra",
                        "GuideWindow.ra",
                    ],
                ),
            ),
        ),
    ]
    dec: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Target Dec at mid time of exposure",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.dec_computed",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.dec",
                        "GuideWindow.dec",
                    ],
                ),
            ),
        ),
    ]
    ra_uncertainty: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Target RA uncertainty",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.ra_uncertainty_computed",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.ra_uncertainty",
                        "GuideWindow.ra_uncertainty",
                    ],
                ),
            ),
        ),
    ]
    dec_uncertainty: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Target Dec uncertainty",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.dec_uncertainty_computed",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.dec_uncertainty",
                        "GuideWindow.dec_uncertainty",
                    ],
                ),
            ),
        ),
    ]
    proper_motion_ra: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Target proper motion in RA",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.ra_proper_motion",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.proper_motion_ra",
                        "GuideWindow.proper_motion_ra",
                    ],
                ),
            ),
        ),
    ]
    proper_motion_dec: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Target proper motion in Dec",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.dec_proper_motion",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.proper_motion_dec",
                        "GuideWindow.proper_motion_dec",
                    ],
                ),
            ),
        ),
    ]
    proper_motion_epoch: Annotated[
        str,
        Field(
            default_factory=_defaults.default_str_factory,
            title="Target proper motion epoch",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.epoch",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(10)",
                    destination=[
                        "ScienceCommon.proper_motion_epoch",
                        "GuideWindow.proper_motion_epoch",
                    ],
                ),
            ),
        ),
    ]
    proposer_ra: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Proposer's target RA",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.ra_literal",
                        function="hms_to_degrees",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.proposer_ra",
                        "GuideWindow.proposer_ra",
                    ],
                ),
            ),
        ),
    ]
    proposer_dec: Annotated[
        float,
        Field(
            default_factory=_defaults.default_num_factory,
            title="Proposer's target Dec",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="PSS:dms_target.dec_literal",
                        function="hms_to_degrees",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "ScienceCommon.proposer_dec",
                        "GuideWindow.proposer_dec",
                    ],
                ),
            ),
        ),
    ]
    source_type: Annotated[
        source_type,
        Field(
            default_factory=_defaults.default_constant_factory(source_type.POINT.value),
            title="Source type used for calibration",
            json_schema_extra=_archive.Archive(
                sdf=_archive.Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=_archive.SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=_archive.ArchiveCatalog(
                    datatype="nvarchar(8)",
                    destination=[
                        "ScienceCommon.source_type",
                        "GuideWindow.source_type",
                    ],
                ),
            ),
        ),
    ]
