import astropy.units as u
import pytest
from pydantic import BaseModel, ValidationError

from roman_datamodels.pydantic.adaptors._adaptor_tags import asdf_tags
from roman_datamodels.pydantic.adaptors._astropy_unit import AstropyUnit, _get_unit_symbol

units_no_dimensionless = (u.s, u.DN, u.DN / u.s, (u.DN / u.s) ** 2, u.electron)
# units_no_dimensionless = tuple(
#     sorted(
#         {unit for unit in list(u.__dict__.values()) if isinstance(unit, u.UnitBase) and unit != u.dimensionless_unscaled},
#         key=_get_unit_symbol,
#     )
# )
units = units_no_dimensionless + (u.dimensionless_unscaled,)


@pytest.mark.parametrize("unit_type", units)
def test_unit_validate(unit_type):
    """
    Test that unit validates and does not get copied
    """

    class TestModel(BaseModel):
        unit: AstropyUnit[unit_type]

    model = TestModel(unit=unit_type)
    assert model.unit == unit_type
    assert model.unit is unit_type

    # Test all units are valid when the unit is set to None
    class TestNoneModel(BaseModel):
        unit: AstropyUnit[None]

    none_model = TestNoneModel(unit=unit_type)
    assert none_model.unit is unit_type


@pytest.mark.parametrize("unit_type", zip(units, units[1:] + units[:1]))
def test_unit_fail(unit_type):
    """
    Test that an incorrect unit fails to validate
    """
    model_unit, unit = unit_type

    class TestModel(BaseModel):
        unit: AstropyUnit[model_unit]

    # Unit-mismatch fails
    with pytest.raises(ValidationError):
        TestModel(unit=unit)

    TestModel(unit=model_unit)  # Check no error


@pytest.mark.parametrize("unit_type", units)
def test_non_unit_fail(unit_type):
    """
    Test that a non-unit fails to validate when given a non-unit input
    """

    class TestModel(BaseModel):
        unit: AstropyUnit[unit_type]

    with pytest.raises(ValidationError):
        TestModel(unit=1)

    with pytest.raises(ValidationError):
        TestModel(unit="m")

    with pytest.raises(ValidationError):
        TestModel(unit=None)

    with pytest.raises(ValidationError):
        TestModel(unit="")


@pytest.mark.parametrize("unit_type", zip(units, units[1:] + units[:1]))
def test_multi_unit(unit_type):
    """
    Test that a unit can be set to multiple possible unite
    """

    class TestModel(BaseModel):
        unit: AstropyUnit[unit_type]

    for unit in unit_type:
        model = TestModel(unit=unit)
        assert model.unit == unit


@pytest.mark.parametrize("unit_type", zip(units_no_dimensionless, units_no_dimensionless[1:] + units_no_dimensionless[:1]))
def test_multiply_unit(unit_type):
    """
    Test that a multiplied unit can be used
    """
    unit0 = unit_type[0] * unit_type[1]
    unit1 = unit_type[1] * unit_type[0]

    class TestModel0(BaseModel):
        unit: AstropyUnit[unit0]

    model = TestModel0(unit=unit0)
    assert model.unit == unit0

    model = TestModel0(unit=unit1)
    assert model.unit == unit1

    with pytest.raises(ValidationError):
        TestModel0(unit=unit_type[0])

    with pytest.raises(ValidationError):
        TestModel0(unit=unit_type[1])

    # Reverse the unit order
    class TestModel1(BaseModel):
        unit: AstropyUnit[unit1]

    model = TestModel1(unit=unit0)
    assert model.unit == unit0

    model = TestModel1(unit=unit1)
    assert model.unit == unit1

    with pytest.raises(ValidationError):
        TestModel1(unit=unit_type[0])

    with pytest.raises(ValidationError):
        TestModel1(unit=unit_type[1])


@pytest.mark.parametrize("unit_type", zip(units_no_dimensionless, units_no_dimensionless[1:] + units_no_dimensionless[:1]))
def test_divide_unit(unit_type):
    """
    Test that a multiplied unit can be used
    """
    unit0 = unit_type[0] / unit_type[1]
    unit1 = unit_type[1] / unit_type[0]

    class TestModel0(BaseModel):
        unit: AstropyUnit[unit0]

    model = TestModel0(unit=unit0)
    assert model.unit == unit0

    with pytest.raises(ValidationError):
        TestModel0(unit=unit1)

    with pytest.raises(ValidationError):
        TestModel0(unit=unit_type[0])

    with pytest.raises(ValidationError):
        TestModel0(unit=unit_type[1])

    # Reverse the unit order
    class TestModel1(BaseModel):
        unit: AstropyUnit[unit1]

    model = TestModel1(unit=unit1)
    assert model.unit == unit1

    with pytest.raises(ValidationError):
        TestModel1(unit=unit0)

    # There is a single case where unit1 == unit_type[0] accidentally
    if unit1 != unit_type[0]:
        with pytest.raises(ValidationError):
            TestModel1(unit=unit_type[0])

    with pytest.raises(ValidationError):
        TestModel1(unit=unit_type[1])


@pytest.mark.parametrize("unit_type", units_no_dimensionless)
def test_unit_power(unit_type):
    """
    Test that a multiplied unit can be used
    """
    unit0 = unit_type**2
    unit1 = unit_type**-3

    class TestModel0(BaseModel):
        unit: AstropyUnit[unit0]

    model = TestModel0(unit=unit0)
    assert model.unit == unit0

    with pytest.raises(ValidationError):
        TestModel0(unit=unit1)

    with pytest.raises(ValidationError):
        TestModel0(unit=unit_type)

    class TestModel1(BaseModel):
        unit: AstropyUnit[unit1]

    model = TestModel1(unit=unit1)
    assert model.unit == unit1

    with pytest.raises(ValidationError):
        TestModel1(unit=unit0)

    with pytest.raises(ValidationError):
        TestModel1(unit=unit_type)


@pytest.mark.parametrize("unit_type", zip(units_no_dimensionless, units_no_dimensionless[1:] + units_no_dimensionless[:1]))
def test_json_schema_return(unit_type):
    print(unit_type)
    truth_base = {
        "title": None,
        "tag": asdf_tags.ASTROPY_UNIT.value,
    }

    class TestModel0(BaseModel):
        unit: AstropyUnit[unit_type[0]]

    assert TestModel0.model_json_schema()["properties"]["unit"] == {
        **truth_base,
        "enum": [_get_unit_symbol(unit_type[0])],
    }

    class TestModel1(BaseModel):
        unit: AstropyUnit[unit_type]

    assert TestModel1.model_json_schema()["properties"]["unit"] == {
        **truth_base,
        "enum": sorted(_get_unit_symbol(unit) for unit in unit_type),
    }

    class TestModel2(BaseModel):
        unit: AstropyUnit[unit_type[0] * unit_type[1]]

    assert TestModel2.model_json_schema()["properties"]["unit"] == {
        **truth_base,
        "enum": [_get_unit_symbol(unit_type[0] * unit_type[1])],
    }

    class TestModel3(BaseModel):
        unit: AstropyUnit[unit_type[0] / unit_type[1]]

    assert TestModel3.model_json_schema()["properties"]["unit"] == {
        **truth_base,
        "enum": [_get_unit_symbol(unit_type[0] / unit_type[1])],
    }

    class TestModel4(BaseModel):
        unit: AstropyUnit[unit_type[0] ** 2]

    assert TestModel4.model_json_schema()["properties"]["unit"] == {
        **truth_base,
        "enum": [_get_unit_symbol(unit_type[0] ** 2)],
    }
