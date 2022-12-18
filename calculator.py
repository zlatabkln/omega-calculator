from node_classes import *
from my_token import *

'''This is the calculator module
It gets an expression tree from parser and goes through from the leaves to the roots. In the end, the function returns
a numeric result (if possible)'''


def calculate(tree, res=0):
    """In the end, the operands that are passed to the commit_operation() can be tokens - if the tree has a leaf on
     the first level; or numeric types (int or float), that we get as a result of operations that were
     committed earlier"""
    if type(tree) == int or type(tree) == float:
        return res
    if type(tree) == NumNode:
        return tree.tok
    else:
        if (tree.left is None or type(tree.left) == NumNode) and (tree.right is None or type(tree.right) == NumNode):
            if tree.right is None:
                res += commit_operation(tree.op_tok, calculate(tree.left, res), None)
            elif tree.left is None:
                res += commit_operation(tree.op_tok, None, calculate(tree.right, res))
            else:
                res += commit_operation(tree.op_tok, tree.left.tok, tree.right.tok)
            return res
        elif tree.right is None or type(tree.right) == NumNode:
            if tree.right is None:
                res += commit_operation(tree.op_tok, calculate(tree.left, res), None)
            else:
                res += commit_operation(tree.op_tok, calculate(tree.left, res), tree.right.tok)
            return res
        elif tree.left is None or type(tree.left) == NumNode:
            if tree.left is None:
                res += commit_operation(tree.op_tok, None, calculate(tree.right, res))
            else:
                res += commit_operation(tree.op_tok, tree.left.tok, calculate(tree.right, res))
            return res
        else:
            res += commit_operation(tree.op_tok, calculate(tree.left, res), calculate(tree.right, res))
            return res


'''As we get to the leaf, we call to this function. It takes the operands and calls directly to the required
calculation function, and returns the numeric result'''


def commit_operation(operator, oprnd1, oprnd2):
    if oprnd1 is None:
        if type(oprnd2) != Token:
            return operator.func(oprnd2)
        return operator.func(oprnd2.value)
    elif oprnd2 is None:
        if type(oprnd1) != Token:
            return operator.func(oprnd1)
        return operator.func(oprnd1.value)
    else:
        if type(oprnd1) != Token and type(oprnd2) != Token:
            return operator.func(oprnd1, oprnd2)
        if type(oprnd1) != Token:
            return operator.func(oprnd1, oprnd2.value)
        elif type(oprnd2) != Token:
            return operator.func(oprnd1.value, oprnd2)
        return operator.func(oprnd1.value, oprnd2.value)
