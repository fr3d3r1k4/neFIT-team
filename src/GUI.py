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


def long_number(number_value):
    num = ""
    float_num = False
    for i in range(len(number_value)):
        if number_value[i].number():
            num += number_value[i]
        elif number_value[i] == '.' and not float_num and num:
            num += number_value[i]
            float_num = True
        else:
            return False
    return True


def tuple_string(input_value):
    operations = ['+', '-', '*', '/', '!', '^', ')', '(', 'r', 's', 'c', 't', 'g']

    i = 0
    input_value = ""
    result = []

    while i < len(input_value):

        if input_value[i] in operations:

            # check number and add to the result
            if input_value and long_number(input_value):
                if '.' in input_value:
                    result.append(float(input_value))
                else:
                    result.append(int(input_value))

            elif input_value and not long_number(input_value):
                return False

            input_value = ""

            # append operation to the result
            result.append(input_value[i])

        else:
            input_value += input_value[i]

        i += 1

    # Check string number, convert and add to the result
    if input_value:
        if long_number(input_value):
            if '.' in input_value:
                result.append(float(input_value))
            else:
                result.append(int(input_value))

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


def brackets_one_two(value):
    brackets = False
    first_part = []
    counter_of_bracket = 0
    i = 0
    new_result = []
    while i < len(value):
        if value[i] == '(':
            brackets = True
            if counter_of_bracket:
                first_part.append('(')
            counter_of_bracket += 1
        elif value[i] == ')':
            counter_of_bracket -= 1
            if not counter_of_bracket:
                new_result += brackets_one_two(first_part)
                first_part = []
                brackets = False
            else:
                first_part.append(')')
        elif brackets:
            first_part.append(value[i])
        else:
            new_result.append(value[i])
        i += 1
    return calculate_value(new_result)


def solve(value):


    # Finally calculate the expression
    value = brackets_one_two(value)
    if value is False:
        return False

    # Convert to int or float
    value = value[0]
    if int(value) - float(value) == 0:
        value = int(value)

    return value
