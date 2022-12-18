import input_modul
from my_lexer import *
from my_parser import *
from calculator import *


def run(text):
  #1.Lexer
    lex = MyLexer(text) 
    tokens = lex.make_token_list() 
  #2.Parser
    pars = MyParser(tokens)
    tree = pars.parse()
  #3.Calculation
    res = calculate(tree)
    return res


print(run(input_modul.input_func()))

