import copy
import threading
from collections.abc import Generator
from contextlib import contextmanager

import asdf
import yaml
from asdf import config as _asdf_config

__all__ = ["config_context", "get_config"]


class _StNodeConfig:
    """
    Class to handle external configuration of StNode objects.
    """

    def __init__(self):
        self._typeguard_enabled = False
        self._asdf_ctx = None
        self._asdf_config = None

    @property
    def typeguard_enabled(self) -> bool:
        """Access the typeguard enabled flag"""
        return self._typeguard_enabled

    @property
    def asdf_ctx(self) -> asdf.AsdfFile:
        """Get the asdf context for the class."""

        if self._asdf_ctx is None:
            self._asdf_ctx = asdf.AsdfFile()

        return self._asdf_ctx

    @property
    def asdf_config(cls) -> _asdf_config.AsdfConfig:
        """Get the asdf config for the class."""
        if cls._asdf_config is None:
            cls._asdf_config = _asdf_config.get_config()

        return cls._asdf_config

    def get_schema(self, uri: str) -> dict:
        """
        Get the schema for the given URI

        Parameters
        ----------
        uri : str
            The URI of the schema to get

        Returns
        -------
        The raw schema dictionary for the given URI
        """
        return yaml.safe_load(self.asdf_config.resource_manager[uri])

    @contextmanager
    def enable_typeguard(self) -> Generator[None, None, None]:
        """
        Context manager to temporarily enable typeguard for testing.
        """
        self._typeguard_enabled = True
        yield
        self._typeguard_enabled = False


class _ConfigLocal(threading.local):
    """
    Local storage for configuration settings.
    """

    def __init__(self):
        super().__init__()
        self.config_stack = []


_global_config = _StNodeConfig()
_local = _ConfigLocal()


def get_config() -> _StNodeConfig:
    """
    Get the global configuration settings.
    """
    """
    Get the current config, which may have been altered by
    one or more surrounding calls to `core.config_context`.

    Returns
    -------
    asdf.config.AsdfConfig
    """
    if len(_local.config_stack) == 0:
        return _global_config

    return _local.config_stack[-1]


@contextmanager
def config_context() -> Generator[_StNodeConfig, None, None]:
    """
    Context manager to temporarily set configuration settings.
    """
    base_config = _global_config if len(_local.config_stack) == 0 else _local.config_stack[-1]

    config = copy.copy(base_config)
    _local.config_stack.append(config)

    try:
        yield config
    finally:
        _local.config_stack.pop()
