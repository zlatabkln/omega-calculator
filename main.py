import input_modul
from my_lexer import *
from my_parser import *
from calculator import *


def run(text):
    lex = MyLexer(text)
    tokens = lex.make_token_list()
    pars = MyParser(tokens)
    tree = pars.parse()
    res = calculate(tree)
    return res

# print(run(input_modul.input_func()))
