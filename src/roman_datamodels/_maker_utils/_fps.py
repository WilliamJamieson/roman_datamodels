from roman_datamodels.stnode import FlushOptions

from ._base import save_node


def mk_fps_groundtest(**kwargs):
    """
    Create a dummy GroundGroundtest instance with valid values for attributes
    required by the schema. Utilized by the model maker utilities below.

    This adds the fps fields

    Returns
    -------
    roman_datamodels.stnode.FpsGroundtest
    """
    from roman_datamodels.nodes import FpsGroundtest

    ground = FpsGroundtest(kwargs)
    ground.flush(FlushOptions.EXTRA, recurse=True)

    return ground


def mk_fps_common_meta(**kwargs):
    """
    Create a dummy common metadata dictionary with valid values for attributes

    Returns
    -------
    dict (defined by the ground_common-1.0.0 schema)
    """
    from roman_datamodels.nodes import FpsCommonMeta

    meta = FpsCommonMeta(kwargs)
    meta.flush(FlushOptions.EXTRA, recurse=True)

    return meta


def mk_fps_meta(**kwargs):
    """
    Create a dummy common metadata dictionary with valid values for attributes

    Returns
    -------
    dict (defined by the fps-1.0.0.meta schema)
    """
    from roman_datamodels.nodes.fps.fps import Fps_Meta

    meta = Fps_Meta(kwargs)
    meta.flush(FlushOptions.EXTRA, recurse=True)

    return meta


def mk_fps(*, shape=None, filepath=None, **kwargs):
    """
    Create a dummy Fps instance (or file) with arrays and valid
    values for attributes required by the schema.

    Parameters
    ----------
    shape : tuple, int
        (optional, keyword-only) (z, y, x) Shape of data array. This includes a
        four-pixel border representing the reference pixels. Default is
            (8, 4096, 4096)
        (8 integrations, 4088 x 4088 represent the science pixels, with the
        additional being the border reference pixels).

    filepath : str
        (optional, keyword-only) File name and path to write model to.

    Returns
    -------
    roman_datamodels.stnode.Fps
    """
    from roman_datamodels.nodes import Fps

    if shape is not None:
        kwargs["_array_shape"] = shape

    fps = Fps(kwargs)
    fps.flush(FlushOptions.EXTRA, recurse=True)

    return save_node(fps, filepath=filepath)