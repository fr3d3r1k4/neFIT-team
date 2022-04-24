import mathLibrary as mth


def number(value):
    if type(value) == int:
        return True


def solving(operator, a, b):
    if operator == '*':
        return mth.multiplication(a, b)
    elif operator == '/':
        return mth.division(a, b)

    elif operator == '+':
        return mth.addition(a, b)

    elif operator == '-':
        return mth.subtraction(a, b)

