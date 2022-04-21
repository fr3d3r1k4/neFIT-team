# =========================================================================
#
# Purpose:     Calculator tests
#
# $Author:     ROMANA DURACIOVA <xdurac01@stud.fit.vutbr.cz>
# $Date:       $2022-04-28
# =========================================================================
#
# @file tests.py
# @author ROMANA DURACIOVA
#
# @brief Implementation of tests for calculator and math library.


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


# ------ End of file tests.py ------
