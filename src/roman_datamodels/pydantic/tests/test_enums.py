import pytest

from roman_datamodels.pydantic import _enums
from roman_datamodels.pydantic._strenum import StrEnum


@pytest.mark.parametrize("enum", StrEnum.__subclasses__())
def test_enums_in_enums(enum):
    assert issubclass(enum, StrEnum)
    assert enum.__name__ in _enums.__all__
    assert hasattr(_enums, enum.__name__)
    assert enum is getattr(_enums, enum.__name__)
