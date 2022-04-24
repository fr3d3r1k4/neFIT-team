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
    if type(value) == int:
        return True

    elif type(value) == float:
        return True
    return False


def solving(operator, a, b):
    if operator == '*':
        return mth.multiplication(a, b)
    elif operator == '/':
        return mth.division(a, b)

    elif operator == '+':
        return mth.addition(a, b)

    elif operator == '-':
        return mth.subtraction(a, b)


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


def calculate_value(value):
    instructions = {'s': 1, 'c': 1, 't': 1, 'g': 1, 'r': 2, '^': 2, '!': 1, '*': 2, '/': 2, '+': 2, '-': 2}
    before_minus = ('(', '', '+', '/', '-', '*')
    for symbol, count in instructions.items():
        i = 0
        while i < len(value):
            if (i - 1 >= 0 and value[i] == '-' and value[i - 1] in before_minus) \
                    or i == 0 and value[i] == '-':
                value[i + 1] = -value[i + 1]
                value.pop(i)
            if value[i] == symbol:
                if count == 1:
                    result = solving(symbol, value[i - 1])
                    if result is ValueError:
                        return False
                    value[i - 1] = result
                    value.pop(i)
                elif count == 2:
                    result = solving(symbol, value[i - 1], value[i + 1])
                    if result is ValueError:
                        return False
                    value[i - 1] = result

                    value.pop(i)
                    value.pop(i)
                    i -= 1
            i += 1
    return value


def brackets_one_two(expression):
    used_bracket = False
    cut_result = []
    cnt_bracket = 0
    i = 0
    new_result = []  # Final result

    while i < len(expression):
        if expression[i] == '(':
            used_bracket = True

            if cnt_bracket:
                cut_result.append('(')

            cnt_bracket += 1

        elif expression[i] == ')':
            cnt_bracket -= 1

            if not cnt_bracket:

                # call priority_brackets function to simplify expression
                new_result += brackets_one_two(cut_result)
                cut_result = []
                used_bracket = False

            else:
                cut_result.append(')')

        elif used_bracket:
            cut_result.append(expression[i])

        else:
            new_result.append(expression[i])

        i += 1

    return calculate_value(new_result)


def solve(expression):
    # convert string to tuple
    expression = tuple_string(expression)

    if expression is False:
        return False


    # Finally calculate the expression
    expression = brackets_one_two(expression)
    if expression is False:
        return False

    # Convert to int or float
    expression = expression[0]
    if int(expression) - float(expression) == 0:
        expression = int(expression)

    return expression
