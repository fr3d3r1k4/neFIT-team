import mathLibrary as math


def number(value):
    if type(value) == int:
        return True


def solve(operator, a, b):
    if operator == '*':
        return math.multiplication(a, b)
    elif operator == '/':
        return math.division(a, b)

    elif operator == '+':
        return math.addition(a, b)

    elif operator == '-':
        return math.subtraction(a, b)

