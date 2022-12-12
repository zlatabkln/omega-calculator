class Token:
    #class of tokens, represented as type:value
    #example 2+3->[TT_INT:2,TT_ADD,TT_INT:3]
    def __init__(self, type_, value, level, side):
        self.type = type_
        self.value = value
        self.level = level
        self.side = side

    def __repr__(self):
        if(self.value):
            return f'{self.type}:{self.value}'
        return f'{self.type}'
