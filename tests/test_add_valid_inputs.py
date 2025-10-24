import pytest
from calculator import Calculator

def test_add_valid_inputs():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_add_invalid_inputs():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.add("2", 3)

def test_subtract_valid_inputs():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3

def test_subtract_invalid_inputs():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.subtract("5", 2)

def test_multiply_valid_inputs():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_multiply_invalid_inputs():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.multiply("2", 3)

def test_divide_valid_inputs():
    calc = Calculator()
    assert calc.divide(6, 3) == 2

def test_divide_invalid_inputs():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(6, 0)
    
def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(8, 0)