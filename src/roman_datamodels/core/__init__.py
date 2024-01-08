"""
This represents the public interface for the roman_datamodels.core sub-package
"""
__all__ = [
    "BaseRomanDataModel",
    "RomanDataModel",
    "RomanExtendedDataModel",
    "Archive",
    "open",
]

from ._base import BaseRomanDataModel
from ._extended import RomanExtendedDataModel
from ._metadata import Archive
from ._model import RomanDataModel
from ._open import rdm_open as open
