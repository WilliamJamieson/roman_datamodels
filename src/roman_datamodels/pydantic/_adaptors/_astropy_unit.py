import warnings
from typing import Annotated, Any, ClassVar, Optional, Union

import astropy.units as u
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import SchemaValidator, core_schema

from ._adaptor_tags import asdf_tags

__all__ = ["Unit", "AstropyUnit"]


Unit = Union[
    u.CompositeUnit,
    u.IrreducibleUnit,
    u.NamedUnit,
    u.PrefixUnit,
    u.Unit,
    u.UnrecognizedUnit,
    u.function.mixin.IrreducibleFunctionUnit,
    u.function.mixin.RegularFunctionUnit,
]
Units = Optional[Union[Unit, list[Unit], tuple[Unit, ...]]]

astropy_unit_schema = core_schema.str_schema(pattern="[\x00-\x7f]*")


def _get_unit_symbol(unit: Union[Unit, str]) -> str:
    if isinstance(unit, str):
        return unit

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=u.UnitsWarning)

        try:
            return unit.to_string(format="vounit")
        except (u.UnitsError, ValueError):
            return unit.to_string()


class _AstropyUnitPydanticAnnotation:
    symbols: ClassVar[Optional[list[str]]] = None

    @classmethod
    def _get_unit_symbol(cls, unit: Unit) -> str:
        symbol = None if unit is None else _get_unit_symbol(unit)
        v = SchemaValidator(core_schema.nullable_schema(astropy_unit_schema))
        v.validate_python(symbol)

        return symbol

    @classmethod
    def _get_unit_symbols(cls, unit=Units) -> Optional[list[str]]:
        if unit is None:
            return
        else:
            if not isinstance(unit, (list, tuple)):
                unit = [unit]
            return [cls._get_unit_symbol(_unit) for _unit in unit]

    @classmethod
    def factory(cls, *, unit: Units = None) -> type:
        symbols = cls._get_unit_symbols(unit)
        return type(cls.__name__ if symbols is None else f"{cls.__name__}_{'_'.join(symbols)}", (cls,), {"symbols": symbols})

    @classmethod
    def _unit_schema(cls) -> core_schema.CoreSchema:
        return astropy_unit_schema if cls.symbols is None else core_schema.literal_schema(cls.symbols)

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        def validate_from_json(value: tuple) -> Unit:
            return u.Unit(value[0], parse_strict="silent")

        from_json_schema = core_schema.chain_schema(
            [
                cls._unit_schema(),
                core_schema.no_info_plain_validator_function(validate_from_json),
            ]
        )

        from_python_schema = core_schema.union_schema(
            [
                core_schema.chain_schema(
                    [
                        core_schema.is_instance_schema(Unit),
                        core_schema.no_info_before_validator_function(
                            function=_get_unit_symbol,
                            schema=cls._unit_schema(),
                        ),
                        from_json_schema,
                    ]
                ),
                from_json_schema,
            ]
        )

        return core_schema.json_or_python_schema(
            json_schema=from_json_schema,
            python_schema=from_python_schema,
            serialization=core_schema.plain_serializer_function_ser_schema(lambda value: value),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        _core_schema: core_schema.CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        schema = {
            "title": None,
            "tag": asdf_tags.ASTROPY_UNIT.value,
        }
        if cls.symbols is None:
            return schema

        if len(cls.symbols) == 1:
            return {**schema, "enum": cls.symbols}

        schema = {**schema, **handler(cls._unit_schema())}
        del schema["type"]
        return schema


class _AstropyUnit:
    """Hack to make it look like it has the style of a type annotation."""

    @staticmethod
    def __getitem__(unit: Units = None) -> type:
        return Annotated[Unit, _AstropyUnitPydanticAnnotation.factory(unit=unit)]


AstropyUnit = _AstropyUnit()
