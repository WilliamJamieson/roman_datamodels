import os

import pytest
from pydantic import ConfigDict

from roman_datamodels.pydantic import datamodels, reference_files
from roman_datamodels.pydantic._registry import REF_MODELS, STEP_MODELS


def test_science_raw_model_maker():
    """Test that the ScienceRawModel maker system works"""
    # Create a testing default model via the maker
    model = datamodels.ScienceRawModel.maker(testing=True)
    assert model.data.shape == datamodels.ScienceRawModel._testing_default["shape"]
    assert model.amp33.shape == datamodels.ScienceRawModel._testing_default["shape"]
    assert model.resultantdq.shape == datamodels.ScienceRawModel._testing_default["shape"]

    # Create a non-testing model with different shape via the maker
    model = datamodels.ScienceRawModel.maker(shape=(3, 5, 5))
    assert model.data.shape == (3, 5, 5)
    assert model.amp33.shape == (3, 5, 5)
    assert model.resultantdq.shape == (3, 5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        datamodels.ScienceRawModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 3-D shape, got.*"):
        datamodels.ScienceRawModel.maker(shape=(3, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        datamodels.ScienceRawModel.maker(shape=(3, 5), foo="bar")


def test_mosaic_model_make():
    """Test that the MosaicModel maker system works"""

    # Create a testing default model via the maker
    model = datamodels.MosaicModel.maker(testing=True)
    assert model.data.shape == (8, 8)
    assert model.err.shape == (8, 8)
    assert model.context.shape == (2, 8, 8)
    assert model.weight.shape == (8, 8)
    assert model.var_poisson.shape == (8, 8)
    assert model.var_rnoise.shape == (8, 8)
    assert model.var_flat.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = datamodels.MosaicModel.maker(shape=(5, 5), n_images=3)
    assert model.data.shape == (5, 5)
    assert model.err.shape == (5, 5)
    assert model.context.shape == (3, 5, 5)
    assert model.weight.shape == (5, 5)
    assert model.var_poisson.shape == (5, 5)
    assert model.var_rnoise.shape == (5, 5)
    assert model.var_flat.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        datamodels.MosaicModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        datamodels.MosaicModel.maker(shape=(3, 5, 5))

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"If shape is provided, n_images must also be provided"):
        datamodels.MosaicModel.maker(shape=(5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' and 'n_images' are allowed in context.*"):
        datamodels.MosaicModel.maker(shape=(3, 5), foo="bar")


def test_image_model_make():
    """Test that the ImageModel maker system works"""

    # Create a testing default model via the maker
    model = datamodels.ImageModel.maker(testing=True)
    assert model.data.shape == (8, 8)
    assert model.err.shape == (8, 8)
    assert model.var_poisson.shape == (8, 8)
    assert model.var_rnoise.shape == (8, 8)
    assert model.var_flat.shape == (8, 8)
    assert model.amp33.shape == (2, 16, 128)
    assert model.border_ref_pix_left.shape == (2, 16, 4)
    assert model.border_ref_pix_right.shape == (2, 16, 4)
    assert model.border_ref_pix_top.shape == (2, 4, 16)
    assert model.border_ref_pix_bottom.shape == (2, 4, 16)
    assert model.dq_border_ref_pix_left.shape == (16, 4)
    assert model.dq_border_ref_pix_right.shape == (16, 4)
    assert model.dq_border_ref_pix_top.shape == (4, 16)
    assert model.dq_border_ref_pix_bottom.shape == (4, 16)

    # Create a non-testing model with different shape via the maker
    model = datamodels.ImageModel.maker(shape=(5, 5), n_groups=3)
    assert model.data.shape == (5, 5)
    assert model.err.shape == (5, 5)
    assert model.var_poisson.shape == (5, 5)
    assert model.var_rnoise.shape == (5, 5)
    assert model.var_flat.shape == (5, 5)
    assert model.amp33.shape == (3, 13, 128)
    assert model.border_ref_pix_left.shape == (3, 13, 4)
    assert model.border_ref_pix_right.shape == (3, 13, 4)
    assert model.border_ref_pix_top.shape == (3, 4, 13)
    assert model.border_ref_pix_bottom.shape == (3, 4, 13)
    assert model.dq_border_ref_pix_left.shape == (13, 4)
    assert model.dq_border_ref_pix_right.shape == (13, 4)
    assert model.dq_border_ref_pix_top.shape == (4, 13)
    assert model.dq_border_ref_pix_bottom.shape == (4, 13)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        datamodels.ImageModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        datamodels.ImageModel.maker(shape=(3, 5, 5))

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"If shape is provided, n_groups must also be provided"):
        datamodels.ImageModel.maker(shape=(5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' and 'n_groups' are allowed in context.*"):
        datamodels.ImageModel.maker(shape=(3, 5), foo="bar")


def test_ramp_model_make():
    """Test that the RampModel maker system works"""

    # Create a testing default model via the maker
    model = datamodels.RampModel.maker(testing=True)
    assert model.data.shape == (2, 8, 8)
    assert model.pixeldq.shape == (8, 8)
    assert model.groupdq.shape == (2, 8, 8)
    assert model.err.shape == (2, 8, 8)
    assert model.amp33.shape == (2, 8, 128)
    assert model.border_ref_pix_left.shape == (2, 8, 4)
    assert model.border_ref_pix_right.shape == (2, 8, 4)
    assert model.border_ref_pix_top.shape == (2, 4, 8)
    assert model.border_ref_pix_bottom.shape == (2, 4, 8)
    assert model.dq_border_ref_pix_left.shape == (8, 4)
    assert model.dq_border_ref_pix_right.shape == (8, 4)
    assert model.dq_border_ref_pix_top.shape == (4, 8)
    assert model.dq_border_ref_pix_bottom.shape == (4, 8)

    # Create a non-testing model with different shape via the maker
    model = datamodels.RampModel.maker(shape=(3, 5, 5))
    assert model.data.shape == (3, 5, 5)
    assert model.pixeldq.shape == (5, 5)
    assert model.groupdq.shape == (3, 5, 5)
    assert model.err.shape == (3, 5, 5)
    assert model.amp33.shape == (3, 5, 128)
    assert model.border_ref_pix_left.shape == (3, 5, 4)
    assert model.border_ref_pix_right.shape == (3, 5, 4)
    assert model.border_ref_pix_top.shape == (3, 4, 5)
    assert model.border_ref_pix_bottom.shape == (3, 4, 5)
    assert model.dq_border_ref_pix_left.shape == (5, 4)
    assert model.dq_border_ref_pix_right.shape == (5, 4)
    assert model.dq_border_ref_pix_top.shape == (4, 5)
    assert model.dq_border_ref_pix_bottom.shape == (4, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        datamodels.RampModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 3-D shape, got.*"):
        datamodels.RampModel.maker(shape=(5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        datamodels.RampModel.maker(shape=(3, 5), foo="bar")


def test_ramp_fit_output_model_make():
    """Test that the RampFitOutputModel maker system works"""

    # Create a testing default model via the maker
    model = datamodels.RampFitOutputModel.maker(testing=True)
    assert model.slope.shape == (2, 8, 8)
    assert model.sigslope.shape == (2, 8, 8)
    assert model.yint.shape == (2, 8, 8)
    assert model.sigyint.shape == (2, 8, 8)
    assert model.pedestal.shape == (8, 8)
    assert model.weights.shape == (2, 8, 8)
    assert model.crmag.shape == (2, 8, 8)
    assert model.var_poisson.shape == (2, 8, 8)
    assert model.var_rnoise.shape == (2, 8, 8)

    # Create a non-testing model with different shape via the maker
    model = datamodels.RampFitOutputModel.maker(shape=(3, 5, 5))
    assert model.slope.shape == (3, 5, 5)
    assert model.sigslope.shape == (3, 5, 5)
    assert model.yint.shape == (3, 5, 5)
    assert model.sigyint.shape == (3, 5, 5)
    assert model.pedestal.shape == (5, 5)
    assert model.weights.shape == (3, 5, 5)
    assert model.crmag.shape == (3, 5, 5)
    assert model.var_poisson.shape == (3, 5, 5)
    assert model.var_rnoise.shape == (3, 5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        datamodels.RampFitOutputModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 3-D shape, got.*"):
        datamodels.RampFitOutputModel.maker(shape=(5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        datamodels.RampFitOutputModel.maker(shape=(3, 5), foo="bar")


def test_msos_stack_model_make():
    """Test that the MsosStackModel maker system works"""

    # Create a testing default model via the maker
    model = datamodels.MsosStackModel.maker(testing=True)
    assert model.data.shape == (8, 8)
    assert model.uncertainty.shape == (8, 8)
    assert model.mask.shape == (8, 8)
    assert model.coverage.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = datamodels.MsosStackModel.maker(shape=(5, 5))
    assert model.data.shape == (5, 5)
    assert model.uncertainty.shape == (5, 5)
    assert model.mask.shape == (5, 5)
    assert model.coverage.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        datamodels.MsosStackModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        datamodels.MsosStackModel.maker(shape=(3, 5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        datamodels.MsosStackModel.maker(shape=(3, 5), foo="bar")


def test_guidewindow_model_make():
    """Test that the GuidewindowModel maker system works"""

    # Create a testing default model via the maker
    model = datamodels.GuidewindowModel.maker(testing=True)
    assert model.pedestal_frames.shape == (2, 3, 4, 5, 6)
    assert model.signal_frames.shape == (2, 3, 4, 5, 6)
    assert model.amp33.shape == (2, 3, 4, 5, 6)

    # Create a non-testing model with different shape via the maker
    model = datamodels.GuidewindowModel.maker(shape=(6, 5, 4, 3, 2))
    assert model.pedestal_frames.shape == (6, 5, 4, 3, 2)
    assert model.signal_frames.shape == (6, 5, 4, 3, 2)
    assert model.amp33.shape == (6, 5, 4, 3, 2)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        datamodels.GuidewindowModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 5-D shape, got.*"):
        datamodels.GuidewindowModel.maker(shape=(3, 5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        datamodels.GuidewindowModel.maker(shape=(3, 5), foo="bar")


def test_dark_ref_model_make():
    """Test that the DarkRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.DarkRefModel.maker(testing=True)
    assert model.data.shape == (2, 8, 8)
    assert model.dq.shape == (8, 8)
    assert model.dark_slope.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.DarkRefModel.maker(shape=(3, 5, 5))
    assert model.data.shape == (3, 5, 5)
    assert model.dq.shape == (5, 5)
    assert model.dark_slope.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.DarkRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 3-D shape, got.*"):
        reference_files.DarkRefModel.maker(shape=(3, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.DarkRefModel.maker(shape=(3, 5), foo="bar")


def test_flat_ref_model_make():
    """Test that the FlatRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.FlatRefModel.maker(testing=True)
    assert model.data.shape == (8, 8)
    assert model.dq.shape == (8, 8)
    assert model.err.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.FlatRefModel.maker(shape=(5, 5))
    assert model.data.shape == (5, 5)
    assert model.dq.shape == (5, 5)
    assert model.err.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.FlatRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        reference_files.FlatRefModel.maker(shape=(3, 5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.FlatRefModel.maker(shape=(3, 5), foo="bar")


def test_gain_ref_model_make():
    """Test that the GainRefModel maker system works"""

    # Create a non-testing default model via the maker
    model = reference_files.GainRefModel.maker()
    assert model.data.shape == (4096, 4096)

    # Create a testing default model via the maker
    model = reference_files.GainRefModel.maker(testing=True)
    assert model.data.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.GainRefModel.maker(shape=(5, 5))
    assert model.data.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.GainRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        reference_files.GainRefModel.maker(shape=(3, 5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.GainRefModel.maker(shape=(3, 5), foo="bar")


def test_inverselinearity_ref_model_make():
    """Test that the InverselinearityRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.InverselinearityRefModel.maker(testing=True)
    assert model.coeffs.shape == (2, 8, 8)
    assert model.dq.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.InverselinearityRefModel.maker(shape=(3, 5, 5))
    assert model.coeffs.shape == (3, 5, 5)
    assert model.dq.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.InverselinearityRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 3-D shape, got.*"):
        reference_files.InverselinearityRefModel.maker(shape=(3, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.InverselinearityRefModel.maker(shape=(3, 5), foo="bar")


def test_ipc_ref_model_make():
    """Test that the IpcRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.IpcRefModel.maker(testing=True)
    assert model.data.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.IpcRefModel.maker(shape=(5, 5))
    assert model.data.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.IpcRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        reference_files.IpcRefModel.maker(shape=(3, 5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.IpcRefModel.maker(shape=(3, 5), foo="bar")


def test_linearity_ref_model_make():
    """Test that the LinearityRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.LinearityRefModel.maker(testing=True)
    assert model.coeffs.shape == (2, 8, 8)
    assert model.dq.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.LinearityRefModel.maker(shape=(3, 5, 5))
    assert model.coeffs.shape == (3, 5, 5)
    assert model.dq.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.LinearityRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 3-D shape, got.*"):
        reference_files.LinearityRefModel.maker(shape=(3, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.LinearityRefModel.maker(shape=(3, 5), foo="bar")


def test_mask_ref_model_make():
    """Test that the MaskRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.MaskRefModel.maker(testing=True)
    assert model.dq.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.MaskRefModel.maker(shape=(5, 5))
    assert model.dq.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.MaskRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        reference_files.MaskRefModel.maker(shape=(3, 5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.MaskRefModel.maker(shape=(3, 5), foo="bar")


def test_pixelarea_ref_model_make():
    """Test that the PixelareaRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.PixelareaRefModel.maker(testing=True)
    assert model.data.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.PixelareaRefModel.maker(shape=(5, 5))
    assert model.data.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.PixelareaRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        reference_files.PixelareaRefModel.maker(shape=(3, 5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.PixelareaRefModel.maker(shape=(3, 5), foo="bar")


def test_readnoise_ref_model_make():
    """Test that the ReadnoiseRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.ReadnoiseRefModel.maker(testing=True)
    assert model.data.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.ReadnoiseRefModel.maker(shape=(5, 5))
    assert model.data.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.ReadnoiseRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        reference_files.ReadnoiseRefModel.maker(shape=(3, 5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.ReadnoiseRefModel.maker(shape=(3, 5), foo="bar")


def test_refpix_ref_model_make():
    """Test that the RefpixRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.RefpixRefModel.maker(testing=True)
    assert model.gamma.shape == (12, 781)
    assert model.zeta.shape == (12, 781)
    assert model.alpha.shape == (12, 781)

    # Create a non-testing model with different shape via the maker
    model = reference_files.RefpixRefModel.maker(shape=(3, 5))
    assert model.gamma.shape == (3, 5)
    assert model.zeta.shape == (3, 5)
    assert model.alpha.shape == (3, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.RefpixRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        reference_files.RefpixRefModel.maker(shape=(3, 5, 7))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.RefpixRefModel.maker(shape=(3, 5), foo="bar")


def test_saturation_ref_model_make():
    """Test that the SaturationRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.SaturationRefModel.maker(testing=True)
    assert model.data.shape == (8, 8)
    assert model.dq.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.SaturationRefModel.maker(shape=(5, 5))
    assert model.data.shape == (5, 5)
    assert model.dq.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.SaturationRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        reference_files.SaturationRefModel.maker(shape=(3, 5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.SaturationRefModel.maker(shape=(3, 5), foo="bar")


def test_superbias_ref_model_make():
    """Test that the SuperbiasRefModel maker system works"""

    # Create a testing default model via the maker
    model = reference_files.SuperbiasRefModel.maker(testing=True)
    assert model.data.shape == (8, 8)
    assert model.dq.shape == (8, 8)
    assert model.err.shape == (8, 8)

    # Create a non-testing model with different shape via the maker
    model = reference_files.SuperbiasRefModel.maker(shape=(5, 5))
    assert model.data.shape == (5, 5)
    assert model.dq.shape == (5, 5)
    assert model.err.shape == (5, 5)

    # Check error for testing and shape
    with pytest.raises(ValueError, match=r"Cannot use context and testing together"):
        reference_files.SuperbiasRefModel.maker(shape=(3, 5, 5), testing=True)

    # Check error if shape is wrong number of dimensions
    with pytest.raises(ValueError, match=r"Expected 2-D shape, got.*"):
        reference_files.SuperbiasRefModel.maker(shape=(3, 5, 5))

    # Check error if extra context is passed
    with pytest.raises(ValueError, match=r"Only 'shape' is allowed in context.*"):
        reference_files.SuperbiasRefModel.maker(shape=(3, 5), foo="bar")


@pytest.mark.skipif(os.environ.get("CI") == "true", reason="Skipping due to memory issues on CI")
@pytest.mark.parametrize("model", {**STEP_MODELS, **REF_MODELS}.values())
def test_default_shapes(model):
    """
    Test that we can get an instance of the model with default shape, the after validator
    ensures that the shape is correct.
    This is a semi-repeat of the test_datamodels_defaults_validate but it allows for full shape
    """

    class TestModel(model):
        model_config = ConfigDict(
            # This forces the model to validate the default values when its instantiated
            # Normally, this is off for performance reasons.
            validate_default=True,
        )

    TestModel.maker()
