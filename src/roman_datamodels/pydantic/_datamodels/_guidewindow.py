from __future__ import annotations

from typing import Annotated, Any, ClassVar

import astropy.units as u
import numpy as np
from astropy.time import Time
from pydantic import ConfigDict, Field, ValidationInfo, model_validator

from .._adaptors import AstropyQuantity, AstropyTime
from .._archive import Archive, ArchiveCatalog, Sdf, SdfOrigin
from .._core import BaseRomanStepModel
from .._defaults import (
    check_shape,
    default_constant_factory,
    default_model_factory,
    default_num_factory,
    default_num_value,
    default_quantity_factory,
    default_str_factory,
    fill_shape,
    quantity_factory,
)
from .._uri import asdf_tag_uri, asdf_uri
from ._common import Common, GuidewindowModes, guidewindow_modes

__all__ = ["GuidewindowModel"]


_SHAPE = (2, 8, 16, 32, 32)


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
        float,
        Field(
            default_factory=default_num_factory,
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
        float,
        Field(
            default_factory=default_num_factory,
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
        float,
        Field(
            default_factory=default_num_factory,
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
            default_factory=default_num_factory,
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
            default_factory=default_str_factory,
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
            default_factory=default_num_factory,
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
            default_factory=default_num_factory,
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


class GuidewindowModel(BaseRomanStepModel):
    _uri: ClassVar = asdf_uri.GUIDEWINDOW.value
    _tag_uri: ClassVar = asdf_tag_uri.GUIDEWINDOW.value

    _testing_default: ClassVar = {"shape": (2, 3, 4, 5, 6)}

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
            default_factory=default_quantity_factory(np.uint16, _SHAPE, u.DN),
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
            default_factory=default_quantity_factory(np.uint16, _SHAPE, u.DN),
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
            default_factory=default_quantity_factory(np.uint16, _SHAPE, u.DN),
            title="Signal frames",
            description=(
                "Amp 33 reference pixel data. Dimensions: num_frames, "
                "num_combined_resultants (or num_uncombined_resultants), "
                "num_reads, x, y"
            ),
        ),
    ]

    def _check_shapes(self, shape: tuple[int] | None):
        check_shape("pedestal_frames", shape, value=self.pedestal_frames)
        check_shape("signal_frames", shape, value=self.signal_frames)
        check_shape("amp33", shape, value=self.amp33)

    @model_validator(mode="after")
    def _handle_data_shape(self) -> GuidewindowModel:
        """Ensure that all the data shapes are consistent with that of data."""

        if len(self.pedestal_frames.shape) != 5:
            raise ValueError(f"Expected 5-D data, got {self.pedestal_frames.shape}")

        self._check_shapes(self.pedestal_frames.shape)

        return self

    @model_validator(mode="before")
    @classmethod
    def _handle_input_shape(cls, data: Any, info: ValidationInfo) -> Any:
        """Handle shaping the default input data"""
        context = info.context

        if context:
            if not set(context.keys()).issubset({"shape"}):
                raise ValueError(f"Only 'shape' is allowed in context, got {list(context.keys())}")

            shape = context.get("shape", None)
            if shape and len(shape) != 5:
                raise ValueError(f"Expected 5-D shape, got {shape}")

            if isinstance(data, GuidewindowModel):
                data._check_shapes(shape)

            elif isinstance(data, dict):
                fill_shape(data, "pedestal_frames", shape, factory=quantity_factory(u.DN, np.uint16))
                fill_shape(data, "signal_frames", shape, factory=quantity_factory(u.DN, np.uint16))
                fill_shape(data, "amp33", shape, factory=quantity_factory(u.DN, np.uint16))

        return data
