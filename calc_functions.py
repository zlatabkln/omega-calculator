import math


# a set of calculation functions for each operator

def add_func(oprnd_1, oprnd_2):
    return oprnd_1 + oprnd_2


def sub_func(oprnd_1, oprnd_2):
    return oprnd_1 - oprnd_2


def mul_func(oprnd_1, oprnd_2):
    return oprnd_1 * oprnd_2


def div_func(oprnd_1, oprnd_2):
    return oprnd_1 / oprnd_2


def pow_func(oprnd_1, oprnd_2):
    return math.pow(oprnd_1, oprnd_2)


def modulo_func(oprnd_1, oprnd_2):
    return oprnd_1 % oprnd_2


def max_func(oprnd_1, oprnd_2):
    if oprnd_1 > oprnd_2:
        return oprnd_1
    else:
        return oprnd_2


def min_func(oprnd_1, oprnd_2):
    if oprnd_1 < oprnd_2:
        return oprnd_1
    else:
        return oprnd_2


def avg_func(oprnd_1, oprnd_2):
    return (oprnd_1 + oprnd_2) / 2


def tilda_func(oprnd):
    return oprnd * (-1)


def factorial_func(oprnd: int):
    if oprnd == 1:
        return 1
    else:
        return factorial_func(oprnd - 1) * oprnd


def sum_digits_func(oprnd):
    sign = 1
    if oprnd < 0:
        sign = -1
        oprnd /= -1
    return simple_sum_digits_func(oprnd) * sign


# helping function - returns sum of digits without the sign

def simple_sum_digits_func(oprnd):
    while oprnd - int(oprnd) > 0:
        oprnd *= 10
    if oprnd == 0:
        return 0
    else:
        return simple_sum_digits_func(int(oprnd / 10)) + oprnd % 10
