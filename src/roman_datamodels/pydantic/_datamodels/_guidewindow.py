from typing import Annotated, ClassVar

import astropy.units as u
import numpy as np
from astropy.time import Time
from pydantic import ConfigDict, Field

from .._adaptors import AstropyQuantity, AstropyTime
from .._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from .._config import create_shape_config
from .._core import BaseRomanDataModel, Number
from .._defaults import (
    default_constant_factory,
    default_model_factory,
    default_num_value,
    default_quantity_factory,
    default_str_value,
)
from .._uri import asdf_tag_uri, asdf_uri
from ._common import Common, GuidewindowModes, guidewindow_modes

__all__ = ["GuidewindowModel"]


_SHAPE, guidewindow_shape_context = create_shape_config((2, 8, 16, 32, 32))


class GuidewindowMeta(Common):
    gw_start_time: Annotated[
        AstropyTime,
        Field(
            default_factory=default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="UTC time at the start of the guide window exposure",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="datetime2",
                    destination=[
                        "GuideWindow.gw_start_time",
                    ],
                ),
            ),
        ),
    ]
    gw_end_time: Annotated[
        AstropyTime,
        Field(
            default_factory=default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="UTC time at the end of the guide window exposure",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="datetime2",
                    destination=[
                        "GuideWindow.gw_end_time",
                    ],
                ),
            ),
        ),
    ]
    gw_frame_readout_time: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="The readout time for the guide window frame",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "GuideWindow.gw_frame_readout_time",
                    ],
                ),
            ),
        ),
    ]
    gw_function_start_time: Annotated[
        AstropyTime,
        Field(
            default_factory=default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="Observatory UTC time at guider function start",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="datetime2",
                    destination=[
                        "GuideWindow.gw_function_start_time",
                    ],
                ),
            ),
        ),
    ]
    gw_function_end_time: Annotated[
        AstropyTime,
        Field(
            default_factory=default_constant_factory(Time("2020-01-01T00:00:00.0", format="isot", scale="utc")),
            title="Observatory UTC time at guider function end",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="datetime2",
                    destination=[
                        "GuideWindow.gw_function_end_time",
                    ],
                ),
            ),
        ),
    ]
    gw_acq_exec_stat: Annotated[
        str,
        Field(
            default_factory=default_constant_factory("StatusRMTest619"),
            title="Guide star window acquisition status",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(15)",
                    destination=[
                        "GuideWindow.gw_acq_exec_stat",
                    ],
                ),
            ),
        ),
    ]
    pedestal_resultant_exp_time: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Total exposure time for the guide window pedestal frames",
            description=("The cumulative exposure time for all the guide window " "pedestal frames"),
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "GuideWindow.pedestal_resultant_exp_time",
                    ],
                ),
            ),
        ),
    ]
    signal_resultant_exp_time: Annotated[
        Number,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Total exposure time for the guide window resultant frames",
            description=("The cumulative exposure time for all the guide window " "resultant frames"),
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="float",
                    destination=[
                        "GuideWindow.signal_resultant_exp_time",
                    ],
                ),
            ),
        ),
    ]
    gw_acq_number: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title='Guide Window ID "Q"',
            description=("A single digit representing the guide star acquisition " "number within the visit"),
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "GuideWindow.gw_acq_number",
                    ],
                ),
            ),
        ),
    ]
    gw_science_file_source: Annotated[
        str,
        Field(
            default_factory=default_constant_factory(default_str_value.NOSTR.value),
            title="The science data associated with this guide window",
            description=(
                "The science data file that is associated with this guide window, "
                'e.g. "r0000101001001001001_01101_0001_WFI01_uncal.asdf"'
            ),
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(120)",
                    destination=[
                        "GuideWindow.gw_science_file_source",
                    ],
                ),
            ),
        ),
    ]
    gw_mode: Annotated[
        GuidewindowModes,
        Field(
            default_factory=default_constant_factory(guidewindow_modes.WIM_ACQ.value),
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="nvarchar(18)",
                    destination=[
                        "GuideWindow.gw_mode",
                    ],
                ),
            ),
        ),
    ]
    gw_window_xstart: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Guide window x start position on the detector",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "GuideWindow.gw_window_xstart",
                    ],
                ),
            ),
        ),
    ]
    gw_window_ystart: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value),
            title="Guide window y start position on the detector",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "GuideWindow.gw_window_ystart",
                    ],
                ),
            ),
        ),
    ]
    gw_window_xstop: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value + 170),
            title="Guide window x stop position on the detector",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "GuideWindow.gw_window_xstop",
                    ],
                ),
            ),
        ),
    ]
    gw_window_ystop: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(default_num_value.NONUM.value + 24),
            title="Guide window y stop position on the detector",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "GuideWindow.gw_window_ystop",
                    ],
                ),
            ),
        ),
    ]
    gw_window_xsize: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(170),
            title="Guide window size in the x direction in detector coordinates",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "GuideWindow.gw_window_xsize",
                    ],
                ),
            ),
        ),
    ]
    gw_window_ysize: Annotated[
        int,
        Field(
            default_factory=default_constant_factory(24),
            title="Guide window size in the y direction in detector coordinates",
            json_schema_extra=Archive(
                sdf=Sdf(
                    special_processing="VALUE_REQUIRED",
                    source=SdfOrigin(
                        origin="Science Data Formatting",
                    ),
                ),
                archive_catalog=ArchiveCatalog(
                    datatype="int",
                    destination=[
                        "GuideWindow.gw_window_ysize",
                    ],
                ),
            ),
        ),
    ]


class GuidewindowModel(BaseRomanDataModel):
    _uri: ClassVar = asdf_uri.GUIDEWINDOW.value
    _tag_uri: ClassVar = asdf_tag_uri.GUIDEWINDOW.value

    model_config = ConfigDict(
        title="Guide window information",
    )

    meta: Annotated[
        GuidewindowMeta,
        Field(
            default_factory=default_model_factory(GuidewindowMeta),
        ),
    ]
    pedestal_frames: Annotated[
        AstropyQuantity[np.uint16, 5, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.uint16, u.DN),
            title="Pedestal frames",
            description=(
                "Reconstituted and oriented pedestal frame GW images. "
                "Dimensions: num_frames, num_combined_resultants "
                "(or num_uncombined_resultants), num_reads, x, y"
            ),
        ),
    ]
    signal_frames: Annotated[
        AstropyQuantity[np.uint16, 5, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.uint16, u.DN),
            title="Signal frames",
            description=(
                "Reconstituted and oriented signal frames. Dimensions: num_frames, "
                "num_combined_resultants (or num_uncombined_resultants), "
                "num_reads, x, y"
            ),
        ),
    ]
    amp33: Annotated[
        AstropyQuantity[np.uint16, 5, u.DN],
        Field(
            default_factory=default_quantity_factory(_SHAPE, np.uint16, u.DN),
            title="Signal frames",
            description=(
                "Amp 33 reference pixel data. Dimensions: num_frames, "
                "num_combined_resultants (or num_uncombined_resultants), "
                "num_reads, x, y"
            ),
        ),
    ]
