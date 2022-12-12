# custom exceptions for the calculator
# lex error - forbidden character exception, shows the problematic character
class LexError(Exception):
    def __init__(self, char):
        pass
        self.char = char

    def __str__(self):
        return f'Unexpected character {self.char}'


class SyntaxException(Exception):
    def __init__(self):
        pass

    def __str__(self, pos: int, case: str):
        if case == "dots":
            return "More than one dot in float"
