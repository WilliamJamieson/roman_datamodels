"""
This model contains all the pipeline DataModels (except for the source catalog models,
    which are defined in _catalog.py).
These are the DataModels that are used as inputs and outputs to the various steps
    of the pipeline. They are also the DataModels that are most commonly used by
    users of the library, and so they have some additional methods and properties
    that are not shared by all DataModels.
"""

from __future__ import annotations

import copy
import itertools
import logging
from typing import ClassVar

import numpy as np
from astropy.modeling import models

from ._core import DataModel, PipelineStep
from ._utils import node_update

__all__ = (
    "FpsModel",
    "GuidewindowModel",
    "ImageModel",
    "L1DetectorGuidewindowModel",
    "L1FaceGuidewindowModel",
    "MosaicModel",
    "MosaicSegmentationMapModel",
    "MsosStackModel",
    "MultibandSegmentationMapModel",
    "RampFitOutputModel",
    "RampModel",
    "ScienceRawModel",
    "SegmentationMapModel",
    "TvacModel",
    "WfiWcsModel",
)

# Define logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class FpsModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/fps-*"


class GuidewindowModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/guidewindow-*"


class ImageModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/wfi_image-*"


class L1DetectorGuidewindowModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/l1_detector_guidewindow-*"


class L1FaceGuidewindowModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/l1_face_guidewindow-*"


class MosaicModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/wfi_mosaic-*"


class MosaicSegmentationMapModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/mosaic_segmentation_map-*"


class MsosStackModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/msos_stack-*"


class MultibandSegmentationMapModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/multiband_segmentation_map-*"


class RampFitOutputModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/ramp_fit_output-*"


class RampModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/ramp-*"

    @classmethod
    def from_science_raw(cls, model):
        """Attempt to construct a RampModel from a DataModel

        If the model has a resultantdq attribute, this is copied into
        the RampModel.groupdq attribute.

        Otherwise, this conversion does not do a detailed mapping between all
        of the new and old metadata, but instead opportunistically looks for
        fields with common names and assigns them. Other metadata with
        non-matching names is simply copied in place. This allows processing to
        proceed and preserves the original metadata, but the resulting files
        have duplicates of many entries.

        Parameters
        ----------
        model : FpsModel, RampModel, ScienceRawModel, TvacModel
            The input data model (a RampModel will also work).

        Returns
        -------
        ramp_model : RampModel
            The RampModel built from the input model. If the input is already
            a RampModel, it is simply returned.

        """
        ALLOWED_MODELS = (FpsModel, RampModel, ScienceRawModel, TvacModel)

        if isinstance(model, cls):
            return model
        if not isinstance(model, ALLOWED_MODELS):
            raise ValueError(f"Input must be one of {ALLOWED_MODELS}")

        # Create base ramp node with dummy values (for validation)
        ramp_model = cls.create_minimal()

        # make cal_step
        ramp_model.meta.cal_step = {}
        for step_name in ramp_model.schema_info("required")["roman"]["meta"]["cal_step"]["required"].info:
            ramp_model.meta.cal_step[step_name] = "INCOMPLETE"

        shape = model.data.shape
        ramp_model.pixeldq = np.zeros(shape[1:], dtype=np.uint32)
        ramp_model.groupdq = np.zeros(shape, dtype=np.uint8)
        ramp_model.data = model.data.astype(np.float32)
        ramp_model.amp33 = model.amp33.copy()

        # check if the input model has a resultantdq from SDF
        if hasattr(model, "resultantdq"):
            ramp_model.groupdq = model.resultantdq.copy()

        node_update(ramp_model._instance, model, ignore=("resultantdq", "meta.model_type"))

        # check for exposure data_problem
        if isinstance(ramp_model.meta.exposure.data_problem, bool):
            if ramp_model.meta.exposure.data_problem:
                ramp_model.meta.exposure.data_problem = "True"
            else:
                ramp_model.meta.exposure.data_problem = None

        return ramp_model


class ScienceRawModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/wfi_science_raw-*"

    @classmethod
    def from_tvac_raw(cls, model):
        """Convert TVAC/FPS into ScienceRawModel

        romancal supports processing a selection of files which use an outdated
        schema. It supports these with a bespoke method that converts the files
        to the new format when they are read in dq_init. This conversion does
        not do a detailed mapping between all of the new and old metadata, but
        instead opportunistically looks for fields with common names and
        assigns them. Other metadata with non-matching names is simply copied
        in place. This allows processing to proceed and preserves the original
        metadata, but the resulting files have duplicates of many entries.

        Parameters
        ----------
        model : ScienceRawModel, TvacModel, FpsModel
          Model to convert from.

        Returns
        -------
        science_raw_model : ScienceRawModel
            The ScienceRawModel built from the input model.
            If the input was a ScienceRawModel, that model is simply returned.

        """
        ALLOWED_MODELS = (FpsModel, ScienceRawModel, TvacModel)

        if isinstance(model, cls):
            return model
        if not isinstance(model, ALLOWED_MODELS):
            raise ValueError(f"Input must be one of {ALLOWED_MODELS}")

        # Create base raw node with dummy values (for validation)
        if isinstance(model, (FpsModel | TvacModel)):
            raw_model = cls.create_fake_data()
        else:
            raw_model = cls.create_minimal()

        node_update(raw_model._instance, model, extras=("meta.statistics",), extras_key="tvac", ignore=("meta.model_type",))

        # check for exposure data_problem
        if isinstance(raw_model.meta.exposure.data_problem, bool):
            if raw_model.meta.exposure.data_problem:
                raw_model.meta.exposure.data_problem = "True"
            else:
                raw_model.meta.exposure.data_problem = None

        return raw_model


class SegmentationMapModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/segmentation_map-*"


class TvacModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/tvac-*"


class WfiWcsModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/wfi_wcs-*"

    @classmethod
    def from_model_with_wcs(cls, model, l1_border=4):
        """Extract the WCS information from an exposure model post-assign_wcs

        Construct a `WfiWcsModel` from any model that is used post-assign_wcs step
        in the ELP pipeline. The WCS information is extracted out of the input model.
        The wcs-related meta information is copied verbatim from the input model.

        However, the WCS object itself is placed into the attribute 'wcs_l2'. Furthermore, a
        modified GWCS, applicable to the Level 1 version of the input model, is created
        and stored in the attribute 'wcs_l1'.

        Parameters
        ----------
        model : ImageModel
            The input data model.

        l1_border : int
            The extra border to add for the L1 wcs.

        Returns
        -------
        wfiwcs_model : WfiWcsModel
            The WfiWcsModel built from the input model.

        """
        if not isinstance(model, ImageModel):
            raise ValueError("Input must be an ImageModel")

        # Retrieve the needed meta components
        wfi_wcs = cls()
        wfi_wcs.meta = {}
        schema = wfi_wcs.get_schema()
        for k in itertools.chain(*(ss["properties"].keys() for ss in schema["properties"]["meta"]["allOf"])):
            if k in model.meta:
                wfi_wcs.meta[k] = copy.deepcopy(model.meta[k])

        # Check that a WCS has been defined.
        if model.meta.wcs is None:
            log.info("Model has no WCS defined. Will not populate the WCS components.")
            return wfi_wcs

        # Assign the model WCS to the L2-specified wcs attribute
        wfi_wcs.wcs_l2 = copy.deepcopy(model.meta.wcs)

        # Create an L1 WCS that accounts for the extra border.
        l1_wcs = copy.deepcopy(model.meta.wcs)
        l1_shift = models.Shift(-l1_border) & models.Shift(-l1_border)
        l1_wcs.insert_transform("detector", l1_shift, after=True)
        bb = wfi_wcs["wcs_l2"].bounding_box
        if bb is not None:
            l1_wcs.bounding_box = ((bb[0][0], bb[0][1] + 2 * l1_border), (bb[1][0], bb[1][1] + 2 * l1_border))
        wfi_wcs.wcs_l1 = l1_wcs

        # Get alignment results, if available
        if hasattr(model.meta, "wcs_fit_results"):
            wfi_wcs.meta.wcs_fit_results = copy.deepcopy(model.meta["wcs_fit_results"])

        # That's all folks.
        return wfi_wcs
