##  @file   tests.py
#   @brief  Implementation of tests for calculator operations.
#   @author ROMANA DURACIOVA
#   @date   2022-04-28

import pytest
import mathLibrary


def test_addition():
    # positive numbers
    assert mathLibrary.addition(0, 0) == 0
    assert mathLibrary.addition(23, 6) == 29
    assert mathLibrary.addition(34, 68) == 102

    # negative numbers
    assert mathLibrary.addition(-44, -77) == -121
    assert mathLibrary.addition(-8, 12) == 4
    assert mathLibrary.addition(444444, -111111) == 333333

    # decimal numbers
    assert mathLibrary.addition(0.23, 0.6) == 0.83
    assert mathLibrary.addition(0.23, -0.6) == -0.37


def test_subtraction():
    # positive numbers
    assert mathLibrary.subtraction(0, 0) == 0
    assert mathLibrary.subtraction(23, 6) == 17
    assert mathLibrary.subtraction(34, 68) == -34

    # negative numbers
    assert mathLibrary.subtraction(-44, -77) == 33
    assert mathLibrary.subtraction(-8, 12) == -20
    assert mathLibrary.subtraction(444444, -111111) == 555555

    # decimal numbers
    assert mathLibrary.subtraction(0.23, 0.6) == -0.37
    assert mathLibrary.subtraction(-0.77, 0.54) == -1.31
    assert mathLibrary.subtraction(0.4, -0.63) == 1.03


def test_multiplication():
    # positive numbers
    assert mathLibrary.multiplication(6, 4) == 24
    # negative numbers
    assert mathLibrary.multiplication(-8, -7) == 56
    # positive * negative number
    assert mathLibrary.multiplication(-12, 5) == -60
    # multiple by zero
    assert mathLibrary.multiplication(478, 0) == 0
    assert mathLibrary.multiplication(0, 542) == 0
    # decimal numbers
    assert mathLibrary.multiplication(0.23, 0.47) == 0.1081
    assert mathLibrary.multiplication(-0.5437, 0.8076) == -0.43909212
    # big numbers
    assert mathLibrary.multiplication(34590, 1368) == 47319120


def test_division():
    # positive numbers
    assert mathLibrary.division(64, 8) == 8
    # negative numbers
    assert mathLibrary.division(-81, -9) == 9
    # positive, negative number combination
    assert mathLibrary.division(-44, 11) == -4
    assert mathLibrary.division(44, -11) == -4
    # divide by zero
    with pytest.raises(ZeroDivisionError):
        mathLibrary.division(32, 0)
        mathLibrary.division(245.80, 0)
        mathLibrary.division(-99, 0)

def test_factorial():
    # value error
    with pytest.raises(ValueError):
        mathLibrary.factorial(-23)
        mathLibrary.factorial(-3.5)

    assert mathLibrary.factorial(7) == 5040
    assert mathLibrary.factorial(1) == 1
    assert mathLibrary.factorial(0) == 1


def test_power():
    # value error
    with pytest.raises(ValueError):
        mathLibrary.power(4, -2)
        mathLibrary.power(2, 0.456)
        mathLibrary.power(2, -3.56)

    assert mathLibrary.power(4, 0) == 1
    assert mathLibrary.power(-4, 0) == 1
    assert mathLibrary.power(23, 1) == 23
    assert mathLibrary.power(4, 2) == 16
    assert mathLibrary.power(-6, 2) == 36
    assert mathLibrary.power(-6, 3) == -216


def test_root_operation():
    # value error
    with pytest.raises(ValueError):
        mathLibrary.rootMath(-8, 2)
        mathLibrary.rootMath(-8, -3)

    assert mathLibrary.rootMath(0, 6) == 0
    assert mathLibrary.rootMath(1, 6) == 1
    assert mathLibrary.rootMath(16, 2) == 4
    assert mathLibrary.rootMath(6561, 4) == 9
    assert mathLibrary.rootMath(0.0529, 2) == 0.23


def test_log():
    with pytest.raises(ValueError):
        mathLibrary.log(0)
        mathLibrary.log(-23)
        mathLibrary.log(0.246)

    assert mathLibrary.log(10) == 1
    assert mathLibrary.log(100) == 2

# ------ End of file tests.py ------
