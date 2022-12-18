class Token:
    # class of tokens, represented as type:value (numbers) or type (operators)
    # example 2+3->[TT_INT:2,TT_ADD,TT_INT:3]
    def __init__(self, type_tok, value, level, func):
        self.type = type_tok
        self.value = value
        self.level = level
        self.func = func

    def __repr__(self):
        if self.type == 'INT' or self.type == 'FLOAT':
            return f'{self.type}:{self.value}'
        return f'{self.type}'



