##  @file   mathLibrary.py
#   @brief  Implementation of mathematical operations for calculator.
#   @author ROMANA DURACIOVA, FILIP PLANKA
#   @date   2022-04-28


import math


def addition(a, b):
    result: float = 0.0
    result = float(a) + float(b)
    return result


def subtraction(a, b):
    result: float = 0.0
    result = float(a) - float(b)
    return result


def multiplication(a, b):
    result: float = 0.0
    result = float(a) * float(b)
    return result


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero!")
    else:
        result: float = 0.0
        result = float(a) / float(b)
        return result


# ------ End of file mathLibrary.py ------
