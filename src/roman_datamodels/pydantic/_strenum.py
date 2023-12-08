import sys

if sys.version_info < (3, 11):
    from strenum import StrEnum as _StrEnum
else:
    from enum import StrEnum as _StrEnum


__all__ = [
    "StrEnum",
]


class StrEnum(_StrEnum):
    pass
