from enum import auto
from sys import version_info

from pydantic_core import core_schema

if version_info < (3, 11):
    from strenum import StrEnum
else:
    from enum import StrEnum


__all__ = ["astropy_time_schema"]


class formats(StrEnum):
    byear = auto()
    cxcsec = auto()
    decimalyear = auto()
    gps = auto()
    iso = auto()
    jd = auto()
    jyear = auto()
    mjd = auto()
    unix = auto()
    unix_tai = auto()
    yday = auto()


class other_formats(StrEnum):
    byear_str = auto()
    datetime = auto()
    fits = auto()
    isot = auto()
    jyear_str = auto()
    plot_date = auto()
    ymdhms = auto()
    datetime64 = auto()


class scale(StrEnum):
    utc = auto()
    tai = auto()
    tcb = auto()
    tcg = auto()
    tdb = auto()
    tt = auto()
    ut1 = auto()


astropy_time_schema = core_schema.definitions_schema(
    core_schema.union_schema(
        [
            core_schema.definition_reference_schema("string_formats"),
            core_schema.definition_reference_schema("array_of_strings"),
            core_schema.definition_reference_schema("time_object"),
        ]
    ),
    [
        core_schema.model_fields_schema(
            {
                "value": core_schema.model_field(
                    core_schema.union_schema(
                        [
                            core_schema.definition_reference_schema("string_formats"),
                            core_schema.definition_reference_schema("array_of_strings"),
                            core_schema.definition_reference_schema("number"),
                            # Add numpy array latter
                        ]
                    )
                ),
                "format": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.definition_reference_schema("format"),
                        default=None,
                    )
                ),
                "base_format": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.union_schema(
                            [
                                core_schema.definition_reference_schema("format"),
                                core_schema.definition_reference_schema("other_format"),
                            ]
                        ),
                        default=None,
                    )
                ),
                "scale": core_schema.model_field(
                    core_schema.with_default_schema(
                        core_schema.definition_reference_schema("scale"),
                        default=None,
                    )
                ),
                # add location later
            },
            ref="time_object",
        ),
        core_schema.literal_schema([e.value for e in formats], ref="format"),
        core_schema.literal_schema([e.value for e in other_formats], ref="other_format"),
        core_schema.literal_schema([e.value for e in scale], ref="scale"),
        core_schema.union_schema([core_schema.int_schema(), core_schema.float_schema()], ref="number"),
        core_schema.list_schema(
            core_schema.union_schema(
                [
                    core_schema.definition_reference_schema("string_formats"),
                    core_schema.list_schema(core_schema.definition_reference_schema("string_formats")),
                ]
            ),
            ref="array_of_strings",
        ),
        core_schema.union_schema(
            [
                core_schema.definition_reference_schema("iso_time"),
                core_schema.definition_reference_schema("byear"),
                core_schema.definition_reference_schema("jyear"),
                core_schema.definition_reference_schema("yday"),
            ],
            ref="string_formats",
        ),
        core_schema.str_schema(
            pattern="[0-9]{4}-(0[1-9])|(1[0-2])-(0[1-9])|([1-2][0-9])|(3[0-1])[T ]([0-1][0-9])|(2[0-4]):[0-5][0-9]:[0-5][0-9](.[0-9]+)?",
            ref="iso_time",
        ),
        core_schema.str_schema(pattern="B[0-9]+(.[0-9]+)?", ref="byear"),
        core_schema.str_schema(pattern="J[0-9]+(.[0-9]+)?", ref="jyear"),
        core_schema.str_schema(
            pattern="[0-9]{4}:(00[1-9])|(0[1-9][0-9])|([1-2][0-9][0-9])|(3[0-5][0-9])|(36[0-5]):([0-1][0-9])|([0-1][0-9])|(2[0-4]):[0-5][0-9]:[0-5][0-9](.[0-9]+)?",
            ref="yday",
        ),
    ],
)
