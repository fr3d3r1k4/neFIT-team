##  @file   GUI.py
#   @brief  Linking math library with calculator, input assertion, defining background functions of calculator
#           essential for right functioning.
#   @author FREDERIKA KMETOVA
#   @date   2022-04-28

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
