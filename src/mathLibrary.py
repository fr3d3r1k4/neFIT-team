

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
    return result


# TODO: osetrit delenie nulou na errorovy vystup, nie trapny print
def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero!")
    else:
        result = a / b
        return result


division(45, 0)

# ------ End of file mathLibrary.py ------
