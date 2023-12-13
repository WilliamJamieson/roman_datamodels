from __future__ import annotations

from typing import Any, Callable, TypeVar

import astropy.units as u
import numpy as np
from numpy.typing import DTypeLike

from ._adaptors import Units

__all__ = [
    "check_shape",
    "fill_shape",
    "ndarray_maker",
    "quantity_maker",
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
    maker: Callable[[tuple[int]], T] | None = None,
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

    if maker:
        return maker(shape)

    raise ValueError(f"If {name} is None, factory must be provided")


def fill_shape(
    data: dict[str, Any],
    name: str,
    shape: tuple[int] | None,
    *,
    n_shape: int | None = None,
    border: str | None = None,
    fill_border: bool = True,
    maker: Callable[[tuple[int]], T] | None = None,
) -> None:
    if (
        value := check_shape(
            name,
            shape,
            n_shape=n_shape,
            border=border,
            fill_border=fill_border,
            value=data.get(name, None),
            maker=maker,
        )
    ) is not None:
        data[name] = value


def ndarray_maker(dtype: DTypeLike, fill: float = 0) -> Callable[[tuple[int]], np.ndarray]:
    def _maker(shape: tuple[int]) -> np.ndarray:
        return np.full(shape, fill, dtype=dtype)

    return _maker


def quantity_maker(unit: Units, dtype: DTypeLike, fill: float = 0) -> Callable[[tuple[int]], u.Quantity]:
    _ndarray = ndarray_maker(dtype, fill)

    def _maker(shape: tuple[int]) -> u.Quantity:
        return u.Quantity(_ndarray(shape), unit=unit, dtype=dtype)

    return _maker
