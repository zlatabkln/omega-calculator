# custom exceptions for the calculator
# lex error - forbidden character exception, shows the problematic character
class LexError(Exception):
    def __init__(self, char):
        pass
        self.char = char

    def __str__(self):
        return f'Unexpected character {self.char}'


# syntax error - forbidden characters order exception, has different cases
class SyntaxException(Exception):
    def __init__(self, case: str, op_tok=None):
        self.case = case
        self.op_tok = op_tok

    def __str__(self):
        if self.case == "dots":  # example - 2..2
            return "More than one dot in float"
        elif self.case == "near operator":  # example - 2~3
            return f'Invalid syntax near operator {self.op_tok.value}'
        elif self.case == "null parentheses":  # example - ()-2
            return f'Null parentheses'
        elif self.case == "rp":
            return f'Unexpected right parentheses'
        elif self.case == "lp":
            return f'Missing right parentheses'


# absent operator exception - has different cases (default - no operator in expression at all)
# also raised when there is an absent right parentheses
class AbsentOperatorException(Exception):
    def __init__(self):
        self.message = 'There is no operator in expression'

    def __str__(self):
        return f'{self.message}'
