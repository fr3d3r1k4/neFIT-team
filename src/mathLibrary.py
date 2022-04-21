

import math


def addition(a, b):
    result = a + b
    return result


def subtraction(a, b):
    result = a - b
    return result


def multiplication(a, b):
    result = a * b
    return result


# TODO: osetrit delenie nulou na errorovy vystup, nie trapny print
def division(a, b):
    if b == 0:
        print("Error: Division by zero")
    else:
        result = a / b
        return result


