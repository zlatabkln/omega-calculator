import pytest
import main


def test1():
    assert main.run("-(32.551-(600-7$\n\v3^2)   *10^-3)") == -32


def test2():
    assert main.run("1*(6-   ~42 \t#)^2/10-0.40") == 14


def test3():
    assert main.run("(~(4!#&3)*\r\v(211#!/ -2))^0.5%10") == 6


def test4():
    assert main.run("(((8@~2$1-124))/-11)@(81^0.25)") == 7


def test5():
    assert main.run("2---(3!) + 4!-~3 - 09 * 0.001 * 10 ^ 3 * (2-1)") == 14


def test6():
    assert main.run("(2 ---(1!)) + (4!)# + ((4!#!))") == 727


def test7():
    assert main.run("-~(5!)# * 3 @ 1 + -1 ^ 4 + ((2)) * ((4 ^ (-~-2.00))) ") == 7.125


def test8():
    assert main.run("(2*~(-244.4*\v\r ~3@(5 +2^3)) )# #") == 5


def test9():
    assert main.run("(\n\n~(24!&(3^ 24*0) +12))^34@-30") == 144


def test10():
    assert main.run("(5.12*2*(-23  + 13)^\r2\v)^0.1") == 2


def test11():
    assert main.run("~(~(3!#!)/(144^0.5*((2%10)$4!#+2^2)))") == 6


def test12():
    assert main.run("2^~(~(1.5*\v(4^0.5) @(((2 %33) ))))") == 8


def test13():
    assert main.run("325/(4!/12 \n+(27 ^(1 $-3/3)))") == 65


def test14():
    assert main.run("((450 +(2^2) ! #)/~(0&12-81)^0.25)#/20") == 0.4


def test15():
    assert main.run("(55.55*(-300+400)/125$(4^3)^(1/3))#") == 4


def test16():
    assert main.run("(235.567-0.25^0.5)#  #@(3^2)") == 7


def test17():
    assert main.run("((236.15 +-.75))@((8*2)/10$6)") == 118.5


def test18():
    assert main.run("(~123456#$((3!))+8^2)#/2") == 3.5


def test19():
    assert main.run("~(~(-234*-2\n)@0&8)#&(0-(13#-2^2))") == 0


def test20():
    assert main.run("~((-268#*\n 2^-3)  *2$3)!#/\t\r99#") == 0.5

