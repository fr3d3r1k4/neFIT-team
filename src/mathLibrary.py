##  @file   mathLibrary.py
#   @brief  Implementation of mathematical operations for calculator.
#   @author ROMANA DURACIOVA, FILIP PLANKA
#   @date   2022-04-28


from ast import Param
from distutils.log import error
import math

##
# @brief Addition of two numbers
# @param a First adddend
# @param b Second addend
# 
# @return Sum of two numbers a, b
def addition(a, b):
    result: float = 0.0
    result = float(a) + float(b)
    #result = round(result, 2)
    return result


##
# @brief Substraction of two numbers 
#
# @param a First substractor
# @param b Second Substractor
#
#@return Diff of two numbers
def subtraction(a, b):
    result: float = 0.0
    result = float(a) - float(b)
    #result = round(result, 2)
    return result


##
# @brief Multiplication of two numbers
#
# @param a Multiplicand
# @param b Multiplier
#
# @return Multiplication of two numbers
def multiplication(a, b):
    result: float = 0.0
    result = float(a) * float(b)
    #result = round(result, 8)
    return result


##
# @brief Division of two numbers
#
# @param a Dividend
# @param b Divisor
#
# @exception Division by zero
#
# @return Division of two numbers
def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero!")
    else:
        result: float = 0.0
        result = float(a) / float(b)
        #result = round(result, 4)
        return result


##
# @brief Factorial of a positive integer
#
# @param n
#
# @exception Input number is negative
# @exception Input number is not an integer
#
# @return Factorial of 0 or 1
# @return Factorial of a positive integer n
def factorial(n):
    if n < 0 or isinstance(n, float):
        raise ValueError("Math Error")
    if n == 0 or n == 1:
        return 1
    
    if n > 0:
        fact = 1
   
    for i in range(1,n+1):
        fact = fact * i
    return fact


##
# 
# @brief Power by natural exponent
#
# @param n The base
# @param m Exponenet
#
# @exception Input number is lesser than 0
# @exception Input number is not an integer
#
# @return Power by 0
# @return n to the power of m
def power(n, m):
    if m < 0 or isinstance (m, float):
        raise ValueError ("Math Error")
    if m == 0 :
        return 1
    else:
        return n ** m


##
#
# @brief Nth root of a number
#
# @param n The base
# @param m Exponent
#
# @exception Input number is 0
# @exception Input number is lesser than 0 and exponent is mulptiplier of 2
#
# @return Nth root with positive base 
# @return Nth root with negative base
def rootMath(n, m):
    if n == 0 or (n % 2 == 0 and n < 0):
        raise ValueError ("Math Error")
    elif n > 0:
        return n **(m**-1)
    else:
        return (-(n))**(m**-1)


##
#
# @brief Decimal logarithm 
#
# @param n Exponent
#
# @exception Input number is 0 or lesser than 0
#
# @return The result of logarithm 
def log(n):
    if n <= 0:
        raise ValueError ("Math Error")
    else:
        return math.log10(n)


# ------ End of file mathLibrary.py ------ 
