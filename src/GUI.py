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

subtraction = ('+', '-',  '*', '/', '(', '')
option = {'+': 2, '-': 2,  '*': 2, '/': 2, 'sin': 1, 'cos': 1, 'tan': 1, 'square': 2, '^': 2, '!': 1}
operators = ['+', '-', '*', '/', '!', '^', '(', ')', 'square', 'sin', 'cos', 'tan']


def number(value):
    if isinstance(value, int):
        return True
    elif isinstance(value, float):
        return True
    return False


def solving_operands(operator, a, b):
    if operator == '+':
        return mth.addition(a, b)
    elif operator == '-':
        return mth.subtraction(a, b)
    elif operator == '*':
        return mth.multiplication(a, b)
    elif operator == '/':
        return mth.division(a, b)


def solving_operands2(operator, a):
    return True


def is_numeric(value):
    return value.replace(".", "", 1).isnumeric


def long_number(value):
    num = ""
    long = False
    for i in range(len(value)):
        if value[i].isdigit():
            num += value[i]
        elif value[i] == '.' and not long and num:
            num += value[i]
            long = True
        else:
            return False
    return True


def tuple_string(in_string):
    global operators
    i = 0
    num_string = ""
    result = []
    while i < len(in_string):
        if in_string[i] in operators:
            if num_string and long_number(num_string):
                if '.' in num_string:
                    result.append(float(num_string))
                else:
                    result.append(int(num_string))
            elif num_string and not long_number(num_string):
                return False
            num_string = ""
            result.append(in_string[i])
        else:
            num_string += in_string[i]
        i += 1
    if num_string:
        if long_number(num_string):
            if '.' in num_string:
                result.append(float(num_string))
            else:
                result.append(int(num_string))
        else:
            return False

    return result


def calculate_value(value):
    global option
    global subtraction
    for operand, count in option.items():
        i = 0
        while i < len(value):
            if (i - 1 >= 0 and value[i] == '-' and value[i - 1] in subtraction) \
                    or i == 0 and value[i] == '-':
                value[i + 1] = -value[i + 1]
                value.pop(i)
            if value[i] == operand:
                if count == 1:
                    result = solving_operands2(operand, value[i - 1])
                    if result is ValueError:
                        return False
                    value[i - 1] = result
                    value.pop(i)
                elif count == 2:
                    result = solving_operands(operand, value[i - 1], value[i + 1])
                    if result is ValueError:
                        return False
                    value[i - 1] = result
                    value.pop(i)
                    value.pop(i)
                    i -= 1
            i += 1
    return value


def brackets_first_second(value):
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
                result += brackets_first_second(first_result)
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
    value = tuple_string(value)
    if value is False:
        return False
    value = brackets_first_second(value)
    if value is False:
        return False
    value = value[0]
    if float(value) - int(value) == 0:
        value = int(value)
    return value
