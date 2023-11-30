from typing import Annotated, Any, Optional

import astropy.units as u
from numpy.typing import DTypeLike
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from pydantic_numpy.helper.annotation import NpArrayPydanticAnnotation

from roman_datamodels.pydantic._adaptors._astropy_unit import Unit, _AstropyUnitPydanticAnnotation

__all__ = ["AstropyQuantity"]


class _AstropyQuantityPydanticAnnotation(NpArrayPydanticAnnotation, _AstropyUnitPydanticAnnotation):
    @classmethod
    def factory(
        cls, *, dtype: DTypeLike, unit: Optional[Unit] = None, dimensions: Optional[int] = None, strict_data_typing: bool = False
    ) -> type:
        symbol = cls._get_unit_symbol(unit)
        ndarray_type = super().factory(data_type=dtype, dimensions=dimensions, strict_data_typing=strict_data_typing)
        return type(
            f"_{ndarray_type.__name__}_{symbol}",
            (cls,),
            {"symbol": symbol, "data_type": dtype, "dimensions": dimensions, "strict_data_typing": strict_data_typing},
        )

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        ndarray_schema = super().__get_pydantic_core_schema__(_source_type, _handler)
        unit_schema = super(NpArrayPydanticAnnotation, cls).__get_pydantic_core_schema__(_source_type, _handler).copy()

        astropy_quantity_schema = core_schema.typed_dict_schema(
            {
                "value": core_schema.typed_dict_field(ndarray_schema["python_schema"]),
                "unit": core_schema.typed_dict_field(unit_schema["python_schema"]),
            }
        )

        def validate_from_json(value: tuple) -> Any:
            return u.Quantity(value["value"], value["unit"], dtype=value["value"].dtype)

        from_json_schema = core_schema.chain_schema(
            [
                astropy_quantity_schema,
                core_schema.no_info_plain_validator_function(validate_from_json),
            ]
        )

        def validate_from_python(value: u.Quantity) -> dict:
            return {
                "value": value.value,
                "unit": value.unit,
            }

        from_python_schema = core_schema.union_schema(
            [
                core_schema.chain_schema(
                    [
                        core_schema.is_instance_schema(u.Quantity),
                        core_schema.no_info_before_validator_function(
                            function=validate_from_python,
                            schema=from_json_schema,
                        ),
                    ]
                ),
                from_json_schema,
            ]
        )

        serializer_schema = core_schema.plain_serializer_function_ser_schema(validate_from_python)

        return core_schema.json_or_python_schema(
            json_schema=from_json_schema,
            python_schema=from_python_schema,
            serialization=serializer_schema,
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _core_schema: core_schema.CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        ndarray_ref = f"Np{'N' if cls.dimensions is None else cls.dimensions}dArray{cls.data_type.__name__.capitalize()}"
        unit_ref = f"unit_{cls.symbol}"

        ndarray_schema = core_schema.model_fields_schema(
            {
                "ndim": core_schema.model_field(core_schema.literal_schema([cls.dimensions])),
                "datatype": core_schema.model_field(core_schema.literal_schema([cls.data_type.__name__])),
            },
            ref=ndarray_ref,
        )

        unit_schema = cls._unit_schema()
        unit_schema["ref"] = unit_ref

        json_schema = core_schema.definitions_schema(
            core_schema.model_fields_schema(
                {
                    "value": core_schema.model_field(core_schema.definition_reference_schema(ndarray_ref)),
                    "unit": core_schema.model_field(core_schema.definition_reference_schema(unit_ref)),
                }
            ),
            [
                ndarray_schema,
                unit_schema,
            ],
        )
        return handler(json_schema)


class _AstropyQuantity:
    @staticmethod
    def __getitem__(factory: tuple[DTypeLike, Unit, Optional[int], Optional[bool]]) -> type:
        if len(factory) < 1:
            raise TypeError("AstropyQuantity requires a dtype.")

        dtype: DTypeLike = factory[0]
        unit: Optional[Unit] = factory[1] if len(factory) > 1 else None
        dimensions: Optional[int] = factory[2] if len(factory) > 2 else None
        strict_data_typing: bool = factory[3] if len(factory) > 3 else False

        return Annotated[
            u.Quantity,
            _AstropyQuantityPydanticAnnotation.factory(
                dtype=dtype, unit=unit, dimensions=dimensions, strict_data_typing=strict_data_typing
            ),
        ]


AstropyQuantity = _AstropyQuantity()
