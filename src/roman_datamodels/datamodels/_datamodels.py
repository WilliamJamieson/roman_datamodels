"""
This module provides all the specific datamodels used by the Roman pipeline.
    These models are what will be read and written by the pipeline to ASDF files.
    Note that we require each model to specify a tag_pattern that corresponds to
    the ASDF tag pattern for the top-level STNode type that the datamodel wraps.
    This tag pattern is derived from the schema manifest defined by RAD.
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

# NOTE: this module does not have the typical `__all__`` present like most of the other
#    modules in `roman_datamodels``. The presence of the `__all__` variable causes is
#    entirely to control what is imported by the wildcard `*` import. This style of
#    import is used by `spiinx-automodapi` to determine what to document within a given
#    module. However, in this module's case we would have to list every single datamodel
#    in the `__all__` which would become tedious and error-prone. Therefore, we simply
#    omit the `__all__` variable and carefully control what we make publicly available
#    in the module's namespace via the use of `_` prefixes on private classes and avoiding
#    the import of items from other modules directly into this module's namespace and instead
#    importing them as the namespace from that module (e.g. `from astropy import time` and
#    using `time.Time` instead of `from astropy.time import Time` and using `Time` directly).
#    this prevents `spinx-automodapi` from documenting these items which can cause documentation
#    warnings and bloat.

# Define logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class MosaicModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/wfi_mosaic-*"


class ImageModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/wfi_image-*"


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


class MsosStackModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/msos_stack-*"


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


class RampFitOutputModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/ramp_fit_output-*"


class L1FaceGuidewindowModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/l1_face_guidewindow-*"


class GuidewindowModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/guidewindow-*"


class L1DetectorGuidewindowModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/l1_detector_guidewindow-*"


class FlatRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/flat-*"


class AbvegaoffsetRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/abvegaoffset-*"


class ApcorrRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/apcorr-*"


class DarkRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/dark-*"


class DetectorstatusRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/detectorstatus-*"


class DarkdecaysignalRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/darkdecaysignal-*"


class DistortionRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/distortion-*"


class EpsfRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/epsf-*"


class EtcRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/etc-*"


class GainRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/gain-*"


class IpcRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/ipc-*"


class LinearityRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/linearity-*"

    def get_primary_array_name(self):
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        return "coeffs"


class IntegralnonlinearityRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/integralnonlinearity-*"

    def get_primary_array_name(self):
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        return "value"


class InverselinearityRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/inverselinearity-*"

    def get_primary_array_name(self):
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        return "coeffs"


class MaskRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/mask-*"

    def get_primary_array_name(self):
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        return "dq"


class MATableRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/matable-*"


class PixelareaRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/pixelarea-*"


class ReadnoiseRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/readnoise-*"


class SkycellsRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/skycells-*"


class SuperbiasRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/superbias-*"


class SaturationRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/saturation-*"


class WfiImgPhotomRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/wfi_img_photom-*"


class RefpixRefModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/reference_files/refpix-*"


class FpsModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/fps-*"


class TvacModel(DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/tvac-*"


class MosaicSegmentationMapModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/mosaic_segmentation_map-*"


class MultibandSegmentationMapModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/multiband_segmentation_map-*"


class SegmentationMapModel(PipelineStep, DataModel):
    __slots__ = ()
    tag_pattern: ClassVar[str] = "asdf://stsci.edu/datamodels/roman/tags/segmentation_map-*"


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
