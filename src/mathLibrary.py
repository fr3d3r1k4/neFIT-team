

##  @file mathLibrary.py
#   @brief Implementation of mathematical operations for calculator.
#   @author ROMANA DURACIOVA, FILIP PLANKA
#   @date 2022-04-28


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
