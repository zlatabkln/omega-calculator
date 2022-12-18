from calc_functions import *

'''This is a module of validations - it calls to the calculation functions and handles exceptions that may
occur'''


def valid_add(oprnd1, oprnd2):
    return add_func(oprnd1, oprnd2)


def valid_sub(oprnd1, oprnd2):
    return sub_func(oprnd1, oprnd2)


def valid_mul(oprnd1, oprnd2):
    return mul_func(oprnd1, oprnd2)


def valid_div(oprnd1, oprnd2):
    try:
        return div_func(oprnd1, oprnd2)
    except ZeroDivisionError:
        print("Division by zero")
        exit(1)


def valid_pow(oprnd1, oprnd2):
    try:
        return pow_func(oprnd1, oprnd2)
    except ValueError:
        print("Unable to calculate complex number")
        exit(1)


def valid_modulo(oprnd1, oprnd2):
    try:
        return modulo_func(oprnd1, oprnd2)
    except ArithmeticError:
        print("Modulo by zero")
        exit(1)


def valid_max(oprnd1, oprnd2):
    return max_func(oprnd1, oprnd2)


def valid_min(oprnd1, oprnd2):
    return min_func(oprnd1, oprnd2)


def valid_avg(oprnd1, oprnd2):
    return avg_func(oprnd1, oprnd2)


def valid_tilda(oprnd):
    return tilda_func(oprnd)


def valid_sum_digits(oprnd):
    return sum_digits_func(oprnd)


def valid_factorial(oprnd):
    if type(oprnd) != int:
        raise TypeError("Factorial requires integer operand")
    if oprnd < 0:
        raise ValueError("Factorial requires positive operand")
    return factorial_func(oprnd)
