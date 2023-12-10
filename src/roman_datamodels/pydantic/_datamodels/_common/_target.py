from typing import Annotated, ClassVar

from pydantic import ConfigDict, Field

from ..._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from ..._core import BaseRomanTaggedModel
from ..._defaults import default_constant_factory, default_num_value, default_str_value
from ..._strenum import StrEnum
from ..._uri import asdf_tag_uri, asdf_uri

__all__ = ["Target"]


class target_type(StrEnum):
    FIXED = "FIXED"
    MOVING = "MOVING"
    GENERIC = "GENERIC"


class source_type(StrEnum):
    POINT = "POINT"
    EXTENDED = "EXTENDED"
    UNKNOWN = "UNKNOWN"


class Target(BaseRomanTaggedModel):
    _uri: ClassVar = asdf_uri.TARGET.value
    _tag_uri: ClassVar = asdf_tag_uri.TARGET.value

    model_config = ConfigDict(
        title="Target information",
    )

    proposer_name: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Proposer's name for the target",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.target_name",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Standard astronomical catalog name for target",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.standard_target_name",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(target_type.FIXED.value),
            title="Type of target",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.target_type",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Target RA at mid time of exposure",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.ra_computed",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Target Dec at mid time of exposure",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.dec_computed",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Target RA uncertainty",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.ra_uncertainty_computed",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Target Dec uncertainty",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.dec_uncertainty_computed",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Target proper motion in RA",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.ra_proper_motion",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Target proper motion in Dec",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.dec_proper_motion",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="Target proper motion epoch",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.epoch",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Proposer's target RA",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.ra_literal",
                        function="hms_to_degrees",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Proposer's target Dec",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="PSS:dms_target.dec_literal",
                        function="hms_to_degrees",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
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
            default_factory=default_constant_factory(source_type.POINT.value),
            title="Source type used for calibration",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="TBD",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(8)",
                    destination=[
                        "ScienceCommon.source_type",
                        "GuideWindow.source_type",
                    ],
                ),
            ),
        ),
    ]
