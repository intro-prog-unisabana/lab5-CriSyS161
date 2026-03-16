def add(num1, num2):
    a = num1 + num2
    return a
def sub(num1, num2):
    b = num2 - num1
    return b
def multiply(num1, num2):
    c = num1 * num2
    return c
def divide(num1, num2):
    if num2 == 0:
        d = "Error: Division by zero is not allowed."
    else:
        d = num1 / num2
    return d
def exponent(base, exp):
    e = base**exp
    return e
def modulo(num1, num2):
    if num2 == 0:
        f = "Error: Modulo by zero is not allowed."
    else:
        f = num1 % num2
    return f
import math
def floor_divide(num1, num2):
    if num2 == 0:
        g = "Error: Division by zero is not allowed."
    else:
        g = math.floor(divide(num1, num2))
def absolute(num):
    h = abs(num)
    return h

