from typing import Union

from pydantic import BaseModel

__all__ = ["BaseDataModel", "BaseRomanRefModel", "BaseRomanDataModel", "Number"]

Number = Union[int, float]


class BaseDataModel(BaseModel):
    class Config:
        use_enum_values = True
        validate_assignment = True


class BaseRomanModel(BaseDataModel):
    pass


class BaseRomanRefModel(BaseDataModel):
    pass


class BaseRomanDataModel(BaseDataModel):
    pass
