from my_exception import *
from grammar import *

'''this class defines two types of nodes:
- number node - the leaf node, contains a numeric operand
- operation node - a sub tree from parent node - operator, and sons (two - for the
binary operators, in unary operators - one of the sons will be None) - the operands'''


class NumNode:
    def __init__(self, tok):
        if tok.type not in ['INT', 'FLOAT']:
            raise ValueError("Must be a number")
        self.tok = tok

    def __repr__(self):
        return f'{self.tok}'


class OpNode:
    def __init__(self, left, op_tok, right):
        if any(op_tok.type in subdict.values() for subdict in DU_OPERATORS.values()) or op_tok.type == 'SUB':
            if left is None or right is None:
                raise SyntaxException("near operator", op_tok)
        elif any(op_tok.type in subdict.values() for subdict in L_UN_OPERATORS.values()):
            if left is not None or right is None:
                raise SyntaxException("near operator", op_tok)
        else:
            if left is None or right is not None:
                raise SyntaxException("near operator", op_tok)
        self.op_tok = op_tok
        self.right = right
        self.left = left

    def __repr__(self):
        if self.right is not None and self.left is not None:
            return f'({self.left},{self.op_tok},{self.right})'
        elif self.left is None:
            return f'({self.op_tok},{self.right})'
        else:
            return f'({self.left},{self.op_tok})'
