# ===============================================================================
#
# Purpose:     GUI for calculator
#
# $Author:     FREDERIKA KMETOVA <xkmeto00@stud.fit.vutbr.cz>
# $Date:       $2022-04-28
# ===============================================================================
#
# @file calc_GUI.py
# @author FREDERIKA KMETOVA
#
# @brief Implementation of GUI for calculator.

import mathLibrary as mth


def number(value):
    if isinstance(value, int):
        return True
    elif isinstance(value, float):
        return True
    return False


def solving_operands2(operator, a, b):
    if operator == '*':
        return mth.multiplication(a, b)
    elif operator == '/':
        return mth.division(a, b)

    elif operator == '+':
        return mth.addition(a, b)

    elif operator == '-':
        return mth.subtraction(a, b)


def solving_operands(value):
    return True


def is_numeric(value):
    return value.replace(".", "", 1).isnumeric


def long_number(str_number):
    number = ""
    float_number = False

    for i in range(len(str_number)):
        if str_number[i].isdigit():
            number += str_number[i]

        # Check if it is a float number
        elif str_number[i] == '.' and not float_number and number:
            number += str_number[i]
            float_number = True

        else:
            return False

    return True


def tuple_string(input_str):
    operations = ['+', '-', '*', '/', '!', '^', ')', '(', 'r', 's', 'c', 't', 'g']

    i = 0
    str_number = ""
    result = []

    while i < len(input_str):

        if input_str[i] in operations:

            # check number and add to the result
            if str_number and long_number(str_number):
                if '.' in str_number:
                    result.append(float(str_number))
                else:
                    result.append(int(str_number))

            elif str_number and not long_number(str_number):
                return False

            str_number = ""

            # append operation to the result
            result.append(input_str[i])

        else:
            str_number += input_str[i]

        i += 1

    # Check string number, convert and add to the result
    if str_number:
        if long_number(str_number):
            if '.' in str_number:
                result.append(float(str_number))
            else:
                result.append(int(str_number))

        else:
            return False

    return result


def calculate_value(expression):
    # value: type of instruction
    # key: number of operands
    instructions = {'s': 1, 'c': 1, 't': 1, 'g': 1, 'r': 2, '^': 2, '!': 1, '*': 2, '/': 2, '+': 2, '-': 2}
    before_minus = ('(', '', '+', '/', '-', '*')

    for symbol, count in instructions.items():
        i = 0

        while i < len(expression):
            if (i - 1 >= 0 and expression[i] == '-' and expression[i - 1] in before_minus) \
                    or i == 0 and expression[i] == '-':
                expression[i + 1] = -expression[i + 1]
                expression.pop(i)

            if expression[i] == symbol:

                if count == 1:
                    result = solving_operands(symbol, expression[i - 1])

                    if result is ValueError:
                        return False

                    expression[i - 1] = result
                    expression.pop(i)

                elif count == 2:
                    result = solving_operands2(symbol, expression[i - 1], expression[i + 1])

                    if result is ValueError:
                        return False

                    expression[i - 1] = result

                    expression.pop(i)
                    expression.pop(i)
                    i -= 1

            i += 1

    return expression


def brackets_one_two(value):
    brackets = False
    first_result = []
    counter = 0
    i = 0
    result = []
    while i < len(value):
        if value[i] == '(':
            brackets = True
            if counter:
                first_result.append('(')
            counter += 1
        elif value[i] == ')':
            counter -= 1
            if not counter:
                result += brackets_one_two(first_result)
                first_result = []
                brackets = False
            else:
                first_result.append(')')
        elif brackets:
            first_result.append(value[i])
        else:
            result.append(value[i])
        i += 1
    return calculate_value(result)


def solve(value):
    # convert string to tuple
    value = tuple_string(value)
    if value is False:
        return False
    value = brackets_one_two(value)
    if value is False:
        return False
    # Convert to int or float
    value = value[0]
    if isinstance(value, int) == 0:
        value = int(value)
    elif isinstance(value, float) == 0:
        value = int(value)
    return value
