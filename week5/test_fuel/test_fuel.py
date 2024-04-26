import pytest
from fuel import convert, gauge


def test_x_greater_than_y():
    with pytest.raises(Exception):
        convert("5/2")

def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_correct_fraction():
    assert convert("1/100") == 1
    assert gauge(1) == "E"
    assert convert("99/100") == 99
    assert gauge(99) == "F"
    assert convert("1/2") == 50
    assert gauge(50) == "50%"


