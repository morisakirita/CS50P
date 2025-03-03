# P.S. fuel.py  was left without Error Handling on purpose
'''
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(percentage)
    g = gauge(percentage)
    print(g)


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if (0 <= x <= 100) and (0 <= y <= 100):
        percentage = (x / y) * 100
        return int(percentage)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
'''

import pytest
from fuel import convert, gauge


def test_convert():
    assert convert('1/4') == 25


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert('10/0')


def test_value_error():
    with pytest.raises(ValueError):
        assert convert('a/b')
        assert convert('1+2')


def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(25) == '25%'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
