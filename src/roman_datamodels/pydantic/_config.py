from contextlib import contextmanager
from copy import copy
from typing import Any, Callable, Optional, Tuple

__all__ = ["ShapeConfigManager", "create_shape_config"]


class ShapeConfig:
    _DEFAULT_SHAPE = None
    _DEFAULT_FILL = None

    def __init__(self):
        self._shape = self._DEFAULT_SHAPE
        self._fill = self._DEFAULT_FILL

    @property
    def shape(self) -> Tuple[int, ...]:
        if self._shape is None:
            raise ValueError("Shape must be set")
        return self._shape

    @shape.setter
    def shape(self, new_shape: Tuple[int, ...]):
        if self._shape is not None and len(new_shape) != len(self.shape):
            raise ValueError(f"Shape must be {len(self.shape)}D")

        self._shape = new_shape

    @property
    def fill(self) -> Tuple[int, ...]:
        if self._fill is None:
            raise ValueError("fill must be set")
        return self._fill

    @fill.setter
    def fill(self, new_fill: Tuple[int, ...]):
        if self._fill is not None and len(new_fill) != len(self.fill):
            raise ValueError(f"fill must be {len(self.fill)}D")

        self._fill = new_fill


class ShapeConfigManager:
    _GLOBAL_CONFIG = None

    def __init__(self):
        self._config_stack: list[ShapeConfig] = []

    @property
    def config(self) -> ShapeConfig:
        if len(self._config_stack) == 0:
            if self._GLOBAL_CONFIG is None:
                raise ValueError("No global config set")
            return self._GLOBAL_CONFIG

        return self._config_stack[-1]

    @property
    def shape(self) -> Tuple[int, ...]:
        return self.config.shape

    @property
    def fill(self) -> Any:
        return self.config.fill

    def add(self, config: ShapeConfig):
        self._config_stack.append(config)

    def pop(self) -> ShapeConfig:
        return self._config_stack.pop()


def create_shape_config(
    input_shape: Tuple[int, ...], input_fill: Optional[Any] = 0
) -> tuple[Any, Callable[[Any,], Any]]:
    class _ShapeConfig(ShapeConfig):
        _DEFAULT_SHAPE = input_shape
        _DEFAULT_FILL = input_fill

    class _ShapeConfigManager(ShapeConfigManager):
        _GLOBAL_CONFIG = _ShapeConfig()

    SHAPE = _ShapeConfigManager()

    @contextmanager
    def shape_context():
        config = copy(SHAPE.config)
        SHAPE.add(config)

        try:
            yield config
        finally:
            SHAPE.pop()

    return SHAPE, shape_context
