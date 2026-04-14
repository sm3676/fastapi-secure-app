from app.calculation_factory import CalculationFactory
import pytest

def test_add():
    assert CalculationFactory.calculate(2, 3, "Add") == 5

def test_sub():
    assert CalculationFactory.calculate(5, 3, "Sub") == 2

def test_multiply():
    assert CalculationFactory.calculate(2, 3, "Multiply") == 6

def test_divide():
    assert CalculationFactory.calculate(6, 3, "Divide") == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        CalculationFactory.calculate(5, 0, "Divide")