class Token:
    # class of tokens, represented as type:value (numbers) or type (operators)
    # example 2+3->[TT_INT:2,TT_ADD,TT_INT:3]
    def __init__(self, type_, value, level):
        self.type = type_
        self.value = value
        self.level = level

    def __repr__(self):
        if self.value is not None:
            return f'{self.type}:{self.value}'
        return f'{self.type}'


def get_level(tok):
    return tok.level
