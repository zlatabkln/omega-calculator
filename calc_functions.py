import math


# a set of calculation functions for each operator

def add_func(oprnd_1, oprnd_2):
    res = oprnd_1 + oprnd_2
    if type(res) == float:
        res = float(format(res, '.17f'))
    return res


def sub_func(oprnd_1, oprnd_2):
    res = oprnd_1 - oprnd_2
    if type(res) == float:
        res = float(format(res, '.17f'))
    return res


def mul_func(oprnd_1, oprnd_2):
    res = oprnd_1 * oprnd_2
    if type(res) == float:
        res = float(format(res, '.17f'))
    return res


def div_func(oprnd_1, oprnd_2):
    res = oprnd_1 / oprnd_2
    if type(res) == float:
        res = float(format(res, '.17f'))
    return res


def pow_func(oprnd_1, oprnd_2):
    res = math.pow(oprnd_1, oprnd_2)
    if type(res) == float:
        res = float(format(res, '.17f'))
    return res


def modulo_func(oprnd_1, oprnd_2):
    res = oprnd_1 % oprnd_2
    if type(res) == float:
        res = float(format(res, '.17f'))
    return res


def max_func(oprnd_1, oprnd_2):
    if oprnd_1 > oprnd_2:
        res = oprnd_1
    else:
        res = oprnd_2
    if type(res) == float:
        res = float(format(res, '.17f'))
    return res


def min_func(oprnd_1, oprnd_2):
    if oprnd_1 < oprnd_2:
        res = oprnd_1
    else:
        res = oprnd_2
    if type(res) == float:
        res = float(format(res, '.17f'))
    return res


def avg_func(oprnd_1, oprnd_2):
    res = (oprnd_1 + oprnd_2) / 2
    if type(res) == float:
        res = float(format(res, '.17f'))
    return res


def tilda_func(oprnd):
    res = oprnd * (-1)
    if type(res) == float:
        res = float(format(res, '.17f'))
    return res


def factorial_func(oprnd: int) -> int:
    if oprnd == 1:
        return 1
    else:
        return factorial_func(oprnd - 1) * oprnd


def sum_digits_func(oprnd) -> int:
    sign = 1
    if oprnd < 0:
        sign = -1
        oprnd /= -1
    return simple_sum_digits_func(oprnd) * sign


# helping function - returns sum of digits without the sign

def simple_sum_digits_func(oprnd) -> int:
    while oprnd - int(oprnd) > 0:
        oprnd *= 10
    if oprnd == 0:
        return 0
    else:
        return simple_sum_digits_func(int(oprnd / 10)) + oprnd % 10
