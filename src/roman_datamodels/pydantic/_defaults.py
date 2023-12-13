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
from ._check import check_shape, fill_shape, ndarray_maker, quantity_maker

__all__ = [
    "check_shape",
    "fill_shape",
    "ndarray_maker",
    "quantity_maker",
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


class default_num_value(IntEnum):
    NONUM = -999999


class default_str_value(StrEnum):
    NOSTR = "dummy value"
    NA = "N/A"


def default_ndarray_factory(dtype: DTypeLike, shape: tuple[int], fill: float = 0) -> Callable[[], np.ndarray]:
    """Factory for a default quantity value.

    This avoids the need to strip the default value from the schema.
    """
    factory = ndarray_maker(dtype, fill)

    def _factory() -> np.ndarray:
        return factory(shape)

    return _factory


def default_quantity_factory(dtype: DTypeLike, shape: tuple[int], unit: Units, fill: float = 0) -> Callable[[], u.Quantity]:
    """Factory for a default quantity value.

    This avoids the need to strip the default value from the schema.
    """
    factory = quantity_maker(unit, dtype, fill)

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
