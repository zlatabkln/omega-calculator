import pytest
import main
from my_exception import *


def test_add():
    assert main.run("2+-3") == -1


def test_sub():
    assert main.run("2-2") == 0


def test_mul():
    assert main.run("24*2") == 48


def test_div1():
    assert float("{:.2f}".format(main.run("2/3"))) == 0.67


def test_div2():
    try:
        main.run("3/0")
        assert False
    except SystemExit as se:
        if se.code == "div zero":
            assert True
        else:
            assert False


def test_pow1():
    try:
        main.run("-4^0.5")
        assert False
    except SystemExit as se:
        if se.code == "cmplx num":
            assert True
        else:
            assert False


def test_pow2():
    assert main.run("4^2") == 16


def test_modulo():
    assert main.run("-13%10") == 7


def test_max():
    assert main.run("2$-3") == 2


def test_min():
    assert main.run("9&0.5") == 0.5


def test_avg():
    assert main.run("4@6") == 5


def test_sum_digits():
    assert main.run("-467#") == -17


def test_tilda():
    assert main.run("~9") == -9


def test_factorial1():
    assert main.run("3!") == 6


def test_factorial2():
    try:
        main.run("-3!")
        assert False
    except ValueError:
        assert True


