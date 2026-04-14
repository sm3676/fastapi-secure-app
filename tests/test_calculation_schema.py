from app.schemas import CalculationCreate
import pytest

def test_valid():
    calc = CalculationCreate(a=5, b=2, type="Add")
    assert calc.a == 5

def test_invalid_division():
    with pytest.raises(ValueError):
        CalculationCreate(a=5, b=0, type="Divide")