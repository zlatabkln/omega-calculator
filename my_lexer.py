from grammar import *
from my_exception import *
from my_token import *


# lexer will convert string expression to the list of tokens - object that'll represent char as type and, if it's a number, value
class MyLexer:
    def __init__(self, expression):
        self.expression = expression  # given expression
        self.pos = -1  # current position
        self.curr_char = None  # char on current position
        self.prev_char = None  # char on previous position (for minus token)
        self.get_next()  # goes to the next character in expression

    # returns the value of the next char if exists
    def check_next(self):
        if self.pos + 1 < len(self.expression):
            return self.expression[self.pos + 1]

    # goes to the next char if exists
    def get_next(self):
        self.pos += 1
        self.prev_char = self.curr_char
        if self.pos < len(self.expression):
            self.curr_char = self.expression[self.pos]
        else:
            self.curr_char = None

    # make_number function - gets all the digits of the number and returns signed int or float
    def make_number(self, sign):
        num_str = ""
        dots = 0
        while self.curr_char is not None and (self.curr_char in DIGITS or self.curr_char == '.'):
            if self.curr_char == '.':
                if dots != 0:
                    raise SyntaxException("dots")
                else:
                    if num_str == " " or num_str == "-":
                        num_str += '0'
                    dots += 1
                    num_str += '.'
            else:
                num_str += self.curr_char
            self.get_next()
        if dots == 0:
            return int(num_str) * sign
        else:
            if num_str[-1] == '.':
                num_str += '0'
            return float(num_str) * sign

    # make_token_from_num - gets a number(int or float) and returns a token matching number's type
    def make_token_from_num(self, num):
        if type(num) == int:
            t_type = 'INT'
        else:
            t_type = 'FLOAT'
        return Token(t_type, num, 0)

    # token_minus - counts minuses and optimises to final operator - + or -, creates matching token
    def token_minus(self, tokens):
        count = 0
        while self.curr_char is not None and self.curr_char == '-':
            if self.prev_char is None and self.check_next() not in DIGITS:
                tokens.append(Token('INT', 0, 0))
            elif count == 0 and self.is_sign():
                self.get_next()
                return self.make_token_from_num(self.make_number(-1))
            count += 1
            self.get_next()
        if count % 2 == 0:
            return Token('ADD', None, 1)
        else:
            return Token('SUB', None, 1)

    # checks if minus is a sign or an operator
    def is_sign(self):
        if self.prev_char in DIGITS or self.prev_char == ')' or self.prev_char in R_UN_OPERATORS:
            return False
        else:
            return True

    # create a list of tokens from the expression
    def make_token_list(self):
        tokens = []
        while self.curr_char is not None:
            if str(self.curr_char).isspace():  # if char is blanc character, get next character
                self.get_next()
            elif self.curr_char in MINUS:  # '-'
                tokens.append(self.token_minus(tokens))
            elif self.curr_char in DIGITS or self.curr_char == '.':  # number
                tokens.append(self.make_token_from_num(self.make_number(1)))
            else:  # different operators
                if any(self.curr_char in sublist for sublist in DU_OPERATORS.keys()):
                    t_d = DU_OPERATORS.get(self.curr_char)
                elif any(self.curr_char in sublist for sublist in L_UN_OPERATORS.keys()):
                    t_d = L_UN_OPERATORS.get(self.curr_char)
                elif any(self.curr_char in sublist for sublist in R_UN_OPERATORS.keys()):
                    t_d = R_UN_OPERATORS.get(self.curr_char)
                elif any(self.curr_char in sublist for sublist in PAR.keys()):
                    t_d = PAR.get(self.curr_char)
                else:  # forbidden character
                    raise LexError(self.curr_char)
                tokens.append(Token(t_d.get("type"), None, t_d.get("level")))
                self.get_next()
        return tokens
