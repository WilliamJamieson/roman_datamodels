from __future__ import annotations

import sys
from enum import IntEnum
from typing import Any, Callable, TypeVar

if sys.version_info < (3, 11):
    from strenum import StrEnum
else:
    from enum import StrEnum

import astropy.units as u
import numpy as np
from numpy.typing import DTypeLike

from ._adaptors import Units

__all__ = [
    "check_shape",
    "fill_shape",
    "ndarray_factory",
    "quantity_factory",
    "default_num_value",
    "default_str_value",
    "default_ndarray_factory",
    "default_quantity_factory",
    "default_model_factory",
    "default_constant_factory",
    "default_num_factory",
    "default_str_factory",
]

T = TypeVar("T")


def check_shape(
    name: str,
    shape: tuple[int] | None,
    *,
    n_shape: int | None = None,
    border: str | None = None,
    fill_border: bool = True,
    value: T | None = None,
    factory: Callable[[tuple[int]], T] | None = None,
) -> T:
    if shape is None:
        return value

    fill = 8 if fill_border else 0

    if border == "lr":
        shape = (shape[0] + fill, 4)
    elif border == "tb":
        shape = (4, shape[1] + fill)
    elif border == "amp33":
        shape = (shape[0] + fill, 128)

    if n_shape is not None:
        shape = (n_shape, *shape)

    if value is not None:
        if value.shape == shape:
            return value

        raise ValueError(f"Expected shape {shape} for {name}, got {value.shape}")

    if factory:
        return factory(shape)

    raise ValueError(f"If {name} is None, factory must be provided")


def fill_shape(
    data: dict[str, Any],
    name: str,
    shape: tuple[int] | None,
    *,
    n_shape: int | None = None,
    border: str | None = None,
    fill_border: bool = True,
    factory: Callable[[tuple[int]], T] | None = None,
) -> None:
    if (
        value := check_shape(
            name,
            shape,
            n_shape=n_shape,
            border=border,
            fill_border=fill_border,
            value=data.get(name, None),
            factory=factory,
        )
    ) is not None:
        data[name] = value


def ndarray_factory(dtype: DTypeLike, fill: float = 0) -> Callable[[tuple[int]], np.ndarray]:
    def _factory(shape: tuple[int]) -> np.ndarray:
        return np.full(shape, fill, dtype=dtype)

    return _factory


def quantity_factory(unit: Units, dtype: DTypeLike, fill: float = 0) -> Callable[[tuple[int]], u.Quantity]:
    _ndarray = ndarray_factory(dtype, fill)

    def _factory(shape: tuple[int]) -> u.Quantity:
        return u.Quantity(_ndarray(shape), unit=unit, dtype=dtype)

    return _factory


class default_num_value(IntEnum):
    NONUM = -999999


class default_str_value(StrEnum):
    NOSTR = "dummy value"
    NA = "N/A"


def default_ndarray_factory(dtype: DTypeLike, shape: tuple[int], fill: float = 0) -> Callable[[], np.ndarray]:
    """Factory for a default quantity value.

    This avoids the need to strip the default value from the schema.
    """
    factory = ndarray_factory(dtype, fill)

    def _factory() -> np.ndarray:
        return factory(shape)

    return _factory


def default_quantity_factory(dtype: DTypeLike, shape: tuple[int], unit: Units, fill: float = 0) -> Callable[[], u.Quantity]:
    """Factory for a default quantity value.

    This avoids the need to strip the default value from the schema.
    """
    factory = quantity_factory(unit, dtype, fill)

    def _factory() -> u.Quantity:
        return factory(shape)

    return _factory


def default_model_factory(cls: type[T]) -> Callable[[], T]:
    """Factory for a default model value.

    This avoids the need to strip the default value from the schema.
    """

    def _default_model_factory() -> T:
        return cls()

    return _default_model_factory


def default_constant_factory(constant: Any) -> Callable[[], Any]:
    """Factory for a default constant value.

    This avoids the need to strip the default value from the schema.
    """

    def _default_constant_factory() -> Any:
        return constant

    return _default_constant_factory


default_num_factory = default_constant_factory(default_num_value.NONUM.value)


default_str_factory = default_constant_factory(default_str_value.NOSTR.value)
