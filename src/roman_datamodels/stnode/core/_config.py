import copy
import threading
from collections.abc import Generator
from contextlib import contextmanager

__all__ = ["config_context", "get_config"]


class _StNodeConfig:
    """
    Class to handle external configuration of StNode objects.
    """

    def __init__(self):
        self._TYPEGUARD_ENABLED = False

    @property
    def TYPEGUARD_ENABLED(self) -> bool:
        """Access the typeguard enabled flag"""
        return self._TYPEGUARD_ENABLED

    @contextmanager
    def enable_typeguard(self) -> Generator[None, None, None]:
        """
        Context manager to temporarily enable typeguard for testing.
        """
        self._TYPEGUARD_ENABLED = True
        yield
        self._TYPEGUARD_ENABLED = False


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
