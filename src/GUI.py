##  @file   GUI.py
#   @brief  Linking math library with calculator, input assertion, defining background functions of calculator
#           essential for right functioning.
#   @author FREDERIKA KMETOVA
#   @date   2022-04-28

import mathLibrary as mth

# @brief Global functions used later in this code
subtraction = ('+', '-',  '*', '/', '(', '')
option = {'+': 2, '-': 2,  '*': 2, '/': 2, '^': 2, '!': 1, 'log': 1, '\u221A': 2}
operators = ['+', '-', '*', '/', '!', '^', '(', ')', 'log', '\u221A']
before = {'+': ('num', ')', '!'), '-': ('num', '(', ')', '+', '*', '/', '!', ''), '*': ('num', ')', '!'), '/': ('num',
          ')', '!'), '^': ('num', ')'), '!': ('num', ')'), '(': ('+', '-', '*', '/', '^', '(', 'log', '\u221A', ''),
          ')': ('num', ')', '!'), 'num': ('+', '-', '*', '/', '^', '(', '', 'log', '\u221A'), 'log': ('num', '+', '-',
          '*', '/', '^', '(', ''), '\u221A': ('num', ')')}
after = {'+': ('num', '-', '(', 'log'), '-': ('num', '-', '(', 'log'), '*': ('num', '-', '(', 'log'), '/': ('num', '-',
         '(', 'log'), '^': ('num', '(', 'log'), '!': ('+', '-', '*', '/',
         '^', ')', ''), '(': ('num', '-', '(', '!', 'log'), ')': ('+', '-', '*', '/', '^', '', ')', '\u221A'),
         'num': ('+', '-', '*', '/', '^', '', '!', ')', '\u221A'), 'log': ('num', '('), '\u221A': ('num', '(')}

# @brief Checking if the input value is float or int
# @param Value which needs to be converted
# @return Returns value in int or float form
def number(value):
    if isinstance(value, int):
        return True
    elif isinstance(value, float):
        return True
    return False

# @brief Solving the input if the operator with two operands is one of mentioned
# @param Used operator that is string
# @param First input that is int or float
# @param Second input that is int or float
# @return Solved functions from mathLibrary.py
def solving_operands(operator, a, b):
    if operator == '+':
        return mth.addition(a, b)
    elif operator == '-':
        return mth.subtraction(a, b)
    elif operator == '*':
        return mth.multiplication(a, b)
    elif operator == '/':
        return mth.division(a, b)
    elif operator == '^':
        return mth.power(a, b)
    elif operator == '\u221A':
        return mth.rootMath(a, b)

# @brief Solving the input if the operator is one of mentioned
# @param Used operator that is string
# @param First input that is int or float
# @return Solved functions from mathLibrary.py
def solving_operands2(operator, a):
    if operator == '!':
        return mth.factorial(a)
    elif operator == 'log(':
        return mth.log(a)

# @brief Checking if the input value is numeric
# @param Input value int or float
# @return True if it is a numeric or False if not
def is_numeric(value):
    return value.replace(".", "", 1).isnumeric

# @brief Checking if a string can be changed to int or float
# @param Input value as a string
# @return True if it can be changed and False if not
def long_number(in_value):
    num = ""
    long = False
    for i in range(len(in_value)):
        if in_value[i].isdigit():
            num += in_value[i]
        elif in_value[i] == '.' and not long and num:
            num += in_value[i]
            long = True
        else:
            return False
    return True

# @brief Changing input string into tuple string
# @param Input value as a string
# @return Changed string
def tuple_string(in_string):
    global operators
    i = 0
    num_string = ""
    result = []
    while i < len(in_string):
        if in_string[i] in operators:
            if num_string and long_number(num_string):
                if '.' not in num_string:
                    result.append(int(num_string))
                else:
                    result.append(float(num_string))
            elif num_string and not long_number(num_string):
                return False
            num_string = ""
            result.append(in_string[i])
        else:
            num_string += in_string[i]
        i += 1
    if num_string:
        if long_number(num_string):
            if '.' not in num_string:
                result.append(int(num_string))
            else:
                result.append(float(num_string))
        else:
            return False

    return result

# @brief Solving the value formed on priority of option
# @param Value as tuple
# @return Solved tuple value
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

# @brief Solving the equation formed on prioritised brackets
# @param Value as tuple
# @return Solved tuple value
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

# @brief Checking if the input is written correctly
# @param Value as tuple
# @return True if the tuple value is written correct and False if not
def repeating_symbols(value):
    counter = 0
    global before
    global after
    not_repeat = ['num' if number(value[i]) else value[i] for i in range(len(value))]
    for i in range(len(not_repeat)):
        if counter < 0:
            return False
        if (i - 1) >= 0 and not_repeat[i - 1] not in before[not_repeat[i]]:
            return False
        if (i + 1) < len(not_repeat) and not_repeat[i + 1] not in after[not_repeat[i]]:
            return False
        elif (i + 1) == len(not_repeat) and '' not in after[not_repeat[i]]:
            return False
        elif (i - 1) < 0 and '' not in before[not_repeat[i]]:
            return False
        if not_repeat[i] == '(':
            counter += 1
        elif not_repeat[i] == ')':
            counter -= 1
    if counter:
        return False
    return True

# @brief Solving the input values
# @param Value as a string
# @return Result as int or float
def solve(value):
    value = tuple_string(value)
    if value is False:
        return False
    if repeating_symbols(value) is False:
        return False
    value = brackets_first_second(value)
    if value is False:
        return False
    value = value[0]
    if float(value) - int(value) == 0:
        value = int(value)
    return value
