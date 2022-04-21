# ======== Copyright (c) 2021, FIT VUT Brno, All rights reserved. ============//
#
# Purpose:     Math library for calculator
#
# $Author:     ROMANA DURACIOVA <xdurac01@stud.fit.vutbr.cz>, FILIP PLANKA <xplank03@stud.fit.vutbr.cz>
# $Date:       $2022-04-28
# ============================================================================//
#
# @file mathLibrary.py
# @author ROMANA DURACIOVA, FILIP PLANKA
#
# @brief Implementation of mathematical operations for calculator.


import math


def addition(a, b):
    result = a + b
    result = round(result, 2)
    return result


def subtraction(a, b):
    result = a - b
    result = round(result, 2)
    return result


def multiplication(a, b):
    result = a * b
    result = round(result, 8)
    return result


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero!")
    else:
        result = a / b
        result = round(result, 4)
        return result


# ------ End of file mathLibrary.py ------
