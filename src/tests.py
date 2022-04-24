# =========================================================================
#
# Purpose:     Calculator tests
#
# $Author:     ROMANA DURACIOVA <xdurac01@stud.fit.vutbr.cz>
# $Date:       $2022-04-28
# =========================================================================


## @file tests.py
# @author ROMANA DURACIOVA
#
# @brief Implementation of tests for calculator and math library.

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
    assert mathLibrary.addition(-0.77, 0.54) == -0.23
    assert mathLibrary.addition(0.4, -0.63) == -0.23


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
    assert mathLibrary.multiplication(0.4, 3) == 1.2
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

# ------ End of file tests.py ------
