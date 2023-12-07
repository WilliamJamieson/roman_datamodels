def get_extensions():
    """
    Get the extension instances for the various astropy
    extensions.  This method is registered with the
    `asdf.extension` entry point.

    Returns
    -------
    List[`asdf.extension.Extension`]
    """
    from roman_datamodels.pydantic._extension import RomanPydanticExtension

    from ._converters import NODE_EXTENSIONS

    return [*NODE_EXTENSIONS, RomanPydanticExtension()]
